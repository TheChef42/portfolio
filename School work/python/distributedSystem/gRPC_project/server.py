from concurrent import futures
import grpc, gRPC_pb2_grpc, gRPC_pb2, logging


class FrequencyCalculatorServicer(gRPC_pb2_grpc.FrequencyCalculatorServicer):


    def Calculate(self, request, context):
        counts = dict()
        words = request.text.split()  # splits the recived text into words in a list

        for word in words:  # looks at each word and sees if it is in the dictionary counts, if yes adds one to the value
            word = ''.join(letter for letter in word if letter.isalnum()).lower()  # sanitizing each word and removing symbols
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        count = gRPC_pb2.WordCount(WordOccurrence=counts)
        return count


    def Combine(self, request, context):
        totalcount = {}
        # runs over the list containing the message structure tuples
        # they have a key(string, the word) and a value(int64 the occurence of the word)
        # it checks if the dict totalcount has the word if yes then adds the value of the new word (can be duplicate)
        for tuple_item in request.allwords:
            key = tuple_item.key
            value = tuple_item.value
            if key in totalcount:
                totalcount[key] += value
            else:
                totalcount[key] = value
        return gRPC_pb2.TotalCount(WordOccurrence=totalcount)


def serve():  # creates a server that can handle multiple threads
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
