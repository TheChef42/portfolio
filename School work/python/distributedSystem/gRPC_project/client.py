from concurrent import futures
import os, glob, threading, grpc, gRPC_pb2_grpc, gRPC_pb2, logging


def Calculate(stub, filename, results):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            text = gRPC_pb2.TextToCount(text=str(f.read()))
            response = stub.Calculate(text)
            count = response.WordOccurrence
            return list(count.items())


def Combine(stub, allwords):
    grpclist = []
    for x in allwords:
        grpclist.append(gRPC_pb2.tuples(key=x[0], value=x[1]))
    responecombine = stub.Combine(gRPC_pb2.TextToCombine(allwords=grpclist))
    return dict(responecombine.WordOccurrence)


def worker(threadname, filenames, results, channel, lock):
    stub = gRPC_pb2_grpc.FrequencyCalculatorStub(channel)
    thread_results = []

    for filename in filenames:
        thread_results = Calculate(stub, filename, thread_results) + thread_results

    with lock:
        results.extend(list(thread_results))

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    allwords = []
    with (grpc.insecure_channel("localhost:50052") as channel):
        n = len(glob.glob('input/*.txt')) # sets n to the amount of .txt files in the sub folder input
        filenames = glob.glob('input/*.txt')
        threads = []
        lock = threading.Lock()
        for i in range(n):
            thread = threading.Thread(name=str(i), target=worker, args=(i, filenames[i::n], allwords, channel, lock))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        stub = gRPC_pb2_grpc.FrequencyCalculatorStub(channel)
        allwords = Combine(stub, allwords)
        allwords = dict(sorted(allwords.items(), key=lambda x: x[1], reverse=True))
        print(allwords)


if __name__ == '__main__':
    logging.basicConfig()
    run()


