from concurrent import futures
import os, glob, threading, grpc, gRPC_pb2_grpc, gRPC_pb2, logging

# Press the green button in the gutter to run the script.


def Calculate(stub, filename):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            text = gRPC_pb2.TextToCount(text=str(f.read()))
            response = stub.Calculate(text)
            count = response.WordOccurrence
            return dict(count)


def Combine(stub, allwords):
    responecombine = stub.Combine(gRPC_pb2.TextToCombine(WordOccurrence=allwords))
    return dict(responecombine.WordOccurrence)


def Merge(dict1, dict2):
    res = dict1 + dict2
    return res


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    allwords = dict()
    i = 0
    with grpc.insecure_channel("localhost:50052") as channel:
        for filename in glob.glob('input/*.txt'):
            stub = gRPC_pb2_grpc.FrequencyCalculatorStub(channel)
            temp = Calculate(stub, filename)
            if i == 0:
                allwords = temp
                print(allwords)
                i += 1
                continue
            else:
                print("else")
                allwords = Merge(list(temp.items()), list(allwords.items()))
            print(allwords)

        print(allwords)

        for key, value in allwords:
            if key in allwords:
                allwords[key] += value
            else:
                allwords[key] = value
        allwords = Combine(stub, allwords)
        allwords = dict(sorted(allwords.items(), key=lambda x: x[1], reverse=True))
        print(allwords)


if __name__ == '__main__':
    logging.basicConfig()
    run()
    n = len(glob.glob('input/*.txt'))  # sets n to the amount of .txt files in the sub folder input
    i = 0

