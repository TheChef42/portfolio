from concurrent import futures
import os, glob, threading, grpc, gRPC_pb2_grpc, gRPC_pb2, logging

# Press the green button in the gutter to run the script.


def Calculate(stub):
    for filename in glob.glob('input/*.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            print(f.read())
            text = gRPC_pb2.TextToCount(text=f.read())
        stub.Calculate(text)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = gRPC_pb2_grpc.FrequencyCalculatorStub(channel)
        print("-------------- GetFeature --------------")
        Calculate(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
    n = len(glob.glob('input/*.txt'))  # sets n to the amount of .txt files in the sub folder input
    i = 0

