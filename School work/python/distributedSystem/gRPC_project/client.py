import os, glob, threading, grpc, gRPC_pb2_grpc, gRPC_pb2, logging


def Calculate(stub, filename):  # a gRPC function that calls the calculate function on the server
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            text = gRPC_pb2.TextToCount(text=str(f.read()))
            response = stub.Calculate(text)  # calling the calculate function on the server
            count = response.WordOccurrence  # extracting the WordOccurrence from the response
            return list(count.items())


def Combine(stub, allwords):  # a gRPC function that calls the combine function on the server
    grpclist = []
    for x in allwords:  # converts the dictionary to a list of the gRPC structure called tuples
        grpclist.append(gRPC_pb2.tuples(key=x[0], value=x[1]))
    responecombine = stub.Combine(gRPC_pb2.TextToCombine(allwords=grpclist))  # calling the combine function on the server
    return dict(responecombine.WordOccurrence)  # extracting the WordOccurence from response and converting it to a dictionary


def worker(threadname, filenames, results, stub, lock):  # a worker function that defines what each thread should do
    thread_results = []

    thread_results = Calculate(stub, filenames) + thread_results  # call the calculate function

    with lock:  # preventing race conditions when modifying the result list
        results.extend(list(thread_results))

def run():
    allwords = []
    with (grpc.insecure_channel("localhost:50052") as channel):
        n = len(glob.glob('input/*.txt'))  # sets n to the amount of .txt files in the sub folder input
        filenames = glob.glob('input/*.txt')
        threads = []
        lock = threading.Lock()  # creates a lock, to be used in the worker function
        stub = gRPC_pb2_grpc.FrequencyCalculatorStub(channel)

        # creating a thread for each file
        for i in range(n):
            thread = threading.Thread(name=str(i), target=worker, args=(i, filenames[i], allwords, stub, lock))
            threads.append(thread)

        # running all the threads
        for thread in threads:
            thread.start()

        # waiting for all the threads to finish
        for thread in threads:
            thread.join()

        # when all threads are done I call the Combine function and overwrite the allwords with the result
        allwords = Combine(stub, allwords)
        allwords = dict(sorted(allwords.items(), key=lambda x: x[1], reverse=True))  # here I sort the result
        print("freq = " + str(allwords))
        channel.close()


if __name__ == '__main__':
    logging.basicConfig()
    run()


