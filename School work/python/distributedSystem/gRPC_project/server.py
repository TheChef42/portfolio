from concurrent import futures
import os, glob, threading, grpc, gRPC_pb2_grpc, gRPC_pb2, logging

# Press the green button in the gutter to run the script.


class FrequencyCalculatorServicer(gRPC_pb2_grpc.FrequencyCalculatorServicer):

    def Calculate(self, request, context):
        print(request.text)
        print("Calculate")
        return "calculate"

    def Combine(self, request, context):
        print("Combine")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    gRPC_pb2_grpc.add_FrequencyCalculatorServicer_to_server(
        FrequencyCalculatorServicer(), server
    )
    server.add_insecure_port("[::]:50052")
    server.start()
    print("server running")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()