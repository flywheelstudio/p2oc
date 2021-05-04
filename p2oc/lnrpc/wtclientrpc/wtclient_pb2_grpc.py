# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from wtclientrpc import wtclient_pb2 as wtclientrpc_dot_wtclient__pb2


class WatchtowerClientStub(object):
    """WatchtowerClient is a service that grants access to the watchtower client
    functionality of the daemon.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTower = channel.unary_unary(
                '/wtclientrpc.WatchtowerClient/AddTower',
                request_serializer=wtclientrpc_dot_wtclient__pb2.AddTowerRequest.SerializeToString,
                response_deserializer=wtclientrpc_dot_wtclient__pb2.AddTowerResponse.FromString,
                )
        self.RemoveTower = channel.unary_unary(
                '/wtclientrpc.WatchtowerClient/RemoveTower',
                request_serializer=wtclientrpc_dot_wtclient__pb2.RemoveTowerRequest.SerializeToString,
                response_deserializer=wtclientrpc_dot_wtclient__pb2.RemoveTowerResponse.FromString,
                )
        self.ListTowers = channel.unary_unary(
                '/wtclientrpc.WatchtowerClient/ListTowers',
                request_serializer=wtclientrpc_dot_wtclient__pb2.ListTowersRequest.SerializeToString,
                response_deserializer=wtclientrpc_dot_wtclient__pb2.ListTowersResponse.FromString,
                )
        self.GetTowerInfo = channel.unary_unary(
                '/wtclientrpc.WatchtowerClient/GetTowerInfo',
                request_serializer=wtclientrpc_dot_wtclient__pb2.GetTowerInfoRequest.SerializeToString,
                response_deserializer=wtclientrpc_dot_wtclient__pb2.Tower.FromString,
                )
        self.Stats = channel.unary_unary(
                '/wtclientrpc.WatchtowerClient/Stats',
                request_serializer=wtclientrpc_dot_wtclient__pb2.StatsRequest.SerializeToString,
                response_deserializer=wtclientrpc_dot_wtclient__pb2.StatsResponse.FromString,
                )
        self.Policy = channel.unary_unary(
                '/wtclientrpc.WatchtowerClient/Policy',
                request_serializer=wtclientrpc_dot_wtclient__pb2.PolicyRequest.SerializeToString,
                response_deserializer=wtclientrpc_dot_wtclient__pb2.PolicyResponse.FromString,
                )


class WatchtowerClientServicer(object):
    """WatchtowerClient is a service that grants access to the watchtower client
    functionality of the daemon.
    """

    def AddTower(self, request, context):
        """
        AddTower adds a new watchtower reachable at the given address and
        considers it for new sessions. If the watchtower already exists, then
        any new addresses included will be considered when dialing it for
        session negotiations and backups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveTower(self, request, context):
        """
        RemoveTower removes a watchtower from being considered for future session
        negotiations and from being used for any subsequent backups until it's added
        again. If an address is provided, then this RPC only serves as a way of
        removing the address from the watchtower instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTowers(self, request, context):
        """ListTowers returns the list of watchtowers registered with the client.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTowerInfo(self, request, context):
        """GetTowerInfo retrieves information for a registered watchtower.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stats(self, request, context):
        """Stats returns the in-memory statistics of the client since startup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Policy(self, request, context):
        """Policy returns the active watchtower client policy configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WatchtowerClientServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTower': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTower,
                    request_deserializer=wtclientrpc_dot_wtclient__pb2.AddTowerRequest.FromString,
                    response_serializer=wtclientrpc_dot_wtclient__pb2.AddTowerResponse.SerializeToString,
            ),
            'RemoveTower': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveTower,
                    request_deserializer=wtclientrpc_dot_wtclient__pb2.RemoveTowerRequest.FromString,
                    response_serializer=wtclientrpc_dot_wtclient__pb2.RemoveTowerResponse.SerializeToString,
            ),
            'ListTowers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTowers,
                    request_deserializer=wtclientrpc_dot_wtclient__pb2.ListTowersRequest.FromString,
                    response_serializer=wtclientrpc_dot_wtclient__pb2.ListTowersResponse.SerializeToString,
            ),
            'GetTowerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTowerInfo,
                    request_deserializer=wtclientrpc_dot_wtclient__pb2.GetTowerInfoRequest.FromString,
                    response_serializer=wtclientrpc_dot_wtclient__pb2.Tower.SerializeToString,
            ),
            'Stats': grpc.unary_unary_rpc_method_handler(
                    servicer.Stats,
                    request_deserializer=wtclientrpc_dot_wtclient__pb2.StatsRequest.FromString,
                    response_serializer=wtclientrpc_dot_wtclient__pb2.StatsResponse.SerializeToString,
            ),
            'Policy': grpc.unary_unary_rpc_method_handler(
                    servicer.Policy,
                    request_deserializer=wtclientrpc_dot_wtclient__pb2.PolicyRequest.FromString,
                    response_serializer=wtclientrpc_dot_wtclient__pb2.PolicyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'wtclientrpc.WatchtowerClient', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WatchtowerClient(object):
    """WatchtowerClient is a service that grants access to the watchtower client
    functionality of the daemon.
    """

    @staticmethod
    def AddTower(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wtclientrpc.WatchtowerClient/AddTower',
            wtclientrpc_dot_wtclient__pb2.AddTowerRequest.SerializeToString,
            wtclientrpc_dot_wtclient__pb2.AddTowerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveTower(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wtclientrpc.WatchtowerClient/RemoveTower',
            wtclientrpc_dot_wtclient__pb2.RemoveTowerRequest.SerializeToString,
            wtclientrpc_dot_wtclient__pb2.RemoveTowerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListTowers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wtclientrpc.WatchtowerClient/ListTowers',
            wtclientrpc_dot_wtclient__pb2.ListTowersRequest.SerializeToString,
            wtclientrpc_dot_wtclient__pb2.ListTowersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTowerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wtclientrpc.WatchtowerClient/GetTowerInfo',
            wtclientrpc_dot_wtclient__pb2.GetTowerInfoRequest.SerializeToString,
            wtclientrpc_dot_wtclient__pb2.Tower.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wtclientrpc.WatchtowerClient/Stats',
            wtclientrpc_dot_wtclient__pb2.StatsRequest.SerializeToString,
            wtclientrpc_dot_wtclient__pb2.StatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Policy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wtclientrpc.WatchtowerClient/Policy',
            wtclientrpc_dot_wtclient__pb2.PolicyRequest.SerializeToString,
            wtclientrpc_dot_wtclient__pb2.PolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
