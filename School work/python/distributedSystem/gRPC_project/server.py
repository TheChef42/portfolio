from concurrent import futures
import os, glob, threading, grpc, gRPC_pb2_grpc, gRPC_pb2, logging

# Press the green button in the gutter to run the script.


class FrequencyCalculatorServicer(gRPC_pb2_grpc.FrequencyCalculatorServicer):

    def Calculate(self, request, context):
        counts = dict()
        words = request.text.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        count = gRPC_pb2.WordCount(WordOccurrence=counts)
        return count

    def Combine(self, request, context):
        totalcount = {}
        print(request.WordOccurrence)
        for key, value in request.WordOccurrence:
            if key in totalcount:
                totalcount[key] += value
            else:
                totalcount[key] = value
        print(totalcount)
        return gRPC_pb2.TotalCount(WordOccurrence=totalcount)



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
