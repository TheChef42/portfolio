# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gRPC_pb2 as gRPC__pb2


class FrequencyCalculatorStub(object):
    """The greeter service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Calculate = channel.unary_unary(
                '/FrequencyCalculator/Calculate',
                request_serializer=gRPC__pb2.TextToCount.SerializeToString,
                response_deserializer=gRPC__pb2.WordCount.FromString,
                )
        self.Combine = channel.unary_unary(
                '/FrequencyCalculator/Combine',
                request_serializer=gRPC__pb2.TextToCombine.SerializeToString,
                response_deserializer=gRPC__pb2.TotalCount.FromString,
                )


class FrequencyCalculatorServicer(object):
    """The greeter service definition.
    """

    def Calculate(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Combine(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FrequencyCalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Calculate': grpc.unary_unary_rpc_method_handler(
                    servicer.Calculate,
                    request_deserializer=gRPC__pb2.TextToCount.FromString,
                    response_serializer=gRPC__pb2.WordCount.SerializeToString,
            ),
            'Combine': grpc.unary_unary_rpc_method_handler(
                    servicer.Combine,
                    request_deserializer=gRPC__pb2.TextToCombine.FromString,
                    response_serializer=gRPC__pb2.TotalCount.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FrequencyCalculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FrequencyCalculator(object):
    """The greeter service definition.
    """

    @staticmethod
    def Calculate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FrequencyCalculator/Calculate',
            gRPC__pb2.TextToCount.SerializeToString,
            gRPC__pb2.WordCount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Combine(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FrequencyCalculator/Combine',
            gRPC__pb2.TextToCombine.SerializeToString,
            gRPC__pb2.TotalCount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)