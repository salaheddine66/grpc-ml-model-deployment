# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import model_service_pb2 as model__service__pb2


class ModelgRPCServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.iris_model_predict = channel.unary_unary(
        '/model_grpc_service.ModelgRPCService/iris_model_predict',
        request_serializer=model__service__pb2.iris_model_input.SerializeToString,
        response_deserializer=model__service__pb2.iris_model_output.FromString,
        )


class ModelgRPCServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def iris_model_predict(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ModelgRPCServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'iris_model_predict': grpc.unary_unary_rpc_method_handler(
          servicer.iris_model_predict,
          request_deserializer=model__service__pb2.iris_model_input.FromString,
          response_serializer=model__service__pb2.iris_model_output.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'model_grpc_service.ModelgRPCService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
