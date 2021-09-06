# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import walletunlocker_pb2 as v0131beta_dot_walletunlocker__pb2


class WalletUnlockerStub(object):
    """
    Comments in this file will be directly parsed into the API
    Documentation as descriptions of the associated method, message, or field.
    These descriptions should go right above the definition of the object, and
    can be in either block or // comment format.

    An RPC method can be matched to an lncli command by placing a line in the
    beginning of the description in exactly the following format:
    lncli: `methodname`

    Failure to specify the exact name of the command will cause documentation
    generation to fail.

    More information on how exactly the gRPC documentation is generated from
    this proto file can be found here:
    https://github.com/lightninglabs/lightning-api

    WalletUnlocker is a service that is used to set up a wallet password for
    lnd at first startup, and unlock a previously set up wallet.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenSeed = channel.unary_unary(
                '/lnrpc.WalletUnlocker/GenSeed',
                request_serializer=v0131beta_dot_walletunlocker__pb2.GenSeedRequest.SerializeToString,
                response_deserializer=v0131beta_dot_walletunlocker__pb2.GenSeedResponse.FromString,
                )
        self.InitWallet = channel.unary_unary(
                '/lnrpc.WalletUnlocker/InitWallet',
                request_serializer=v0131beta_dot_walletunlocker__pb2.InitWalletRequest.SerializeToString,
                response_deserializer=v0131beta_dot_walletunlocker__pb2.InitWalletResponse.FromString,
                )
        self.UnlockWallet = channel.unary_unary(
                '/lnrpc.WalletUnlocker/UnlockWallet',
                request_serializer=v0131beta_dot_walletunlocker__pb2.UnlockWalletRequest.SerializeToString,
                response_deserializer=v0131beta_dot_walletunlocker__pb2.UnlockWalletResponse.FromString,
                )
        self.ChangePassword = channel.unary_unary(
                '/lnrpc.WalletUnlocker/ChangePassword',
                request_serializer=v0131beta_dot_walletunlocker__pb2.ChangePasswordRequest.SerializeToString,
                response_deserializer=v0131beta_dot_walletunlocker__pb2.ChangePasswordResponse.FromString,
                )


class WalletUnlockerServicer(object):
    """
    Comments in this file will be directly parsed into the API
    Documentation as descriptions of the associated method, message, or field.
    These descriptions should go right above the definition of the object, and
    can be in either block or // comment format.

    An RPC method can be matched to an lncli command by placing a line in the
    beginning of the description in exactly the following format:
    lncli: `methodname`

    Failure to specify the exact name of the command will cause documentation
    generation to fail.

    More information on how exactly the gRPC documentation is generated from
    this proto file can be found here:
    https://github.com/lightninglabs/lightning-api

    WalletUnlocker is a service that is used to set up a wallet password for
    lnd at first startup, and unlock a previously set up wallet.
    """

    def GenSeed(self, request, context):
        """
        GenSeed is the first method that should be used to instantiate a new lnd
        instance. This method allows a caller to generate a new aezeed cipher seed
        given an optional passphrase. If provided, the passphrase will be necessary
        to decrypt the cipherseed to expose the internal wallet seed.

        Once the cipherseed is obtained and verified by the user, the InitWallet
        method should be used to commit the newly generated seed, and create the
        wallet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitWallet(self, request, context):
        """
        InitWallet is used when lnd is starting up for the first time to fully
        initialize the daemon and its internal wallet. At the very least a wallet
        password must be provided. This will be used to encrypt sensitive material
        on disk.

        In the case of a recovery scenario, the user can also specify their aezeed
        mnemonic and passphrase. If set, then the daemon will use this prior state
        to initialize its internal wallet.

        Alternatively, this can be used along with the GenSeed RPC to obtain a
        seed, then present it to the user. Once it has been verified by the user,
        the seed can be fed into this RPC in order to commit the new wallet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnlockWallet(self, request, context):
        """lncli: `unlock`
        UnlockWallet is used at startup of lnd to provide a password to unlock
        the wallet database.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangePassword(self, request, context):
        """lncli: `changepassword`
        ChangePassword changes the password of the encrypted wallet. This will
        automatically unlock the wallet database if successful.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WalletUnlockerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenSeed': grpc.unary_unary_rpc_method_handler(
                    servicer.GenSeed,
                    request_deserializer=v0131beta_dot_walletunlocker__pb2.GenSeedRequest.FromString,
                    response_serializer=v0131beta_dot_walletunlocker__pb2.GenSeedResponse.SerializeToString,
            ),
            'InitWallet': grpc.unary_unary_rpc_method_handler(
                    servicer.InitWallet,
                    request_deserializer=v0131beta_dot_walletunlocker__pb2.InitWalletRequest.FromString,
                    response_serializer=v0131beta_dot_walletunlocker__pb2.InitWalletResponse.SerializeToString,
            ),
            'UnlockWallet': grpc.unary_unary_rpc_method_handler(
                    servicer.UnlockWallet,
                    request_deserializer=v0131beta_dot_walletunlocker__pb2.UnlockWalletRequest.FromString,
                    response_serializer=v0131beta_dot_walletunlocker__pb2.UnlockWalletResponse.SerializeToString,
            ),
            'ChangePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangePassword,
                    request_deserializer=v0131beta_dot_walletunlocker__pb2.ChangePasswordRequest.FromString,
                    response_serializer=v0131beta_dot_walletunlocker__pb2.ChangePasswordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lnrpc.WalletUnlocker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WalletUnlocker(object):
    """
    Comments in this file will be directly parsed into the API
    Documentation as descriptions of the associated method, message, or field.
    These descriptions should go right above the definition of the object, and
    can be in either block or // comment format.

    An RPC method can be matched to an lncli command by placing a line in the
    beginning of the description in exactly the following format:
    lncli: `methodname`

    Failure to specify the exact name of the command will cause documentation
    generation to fail.

    More information on how exactly the gRPC documentation is generated from
    this proto file can be found here:
    https://github.com/lightninglabs/lightning-api

    WalletUnlocker is a service that is used to set up a wallet password for
    lnd at first startup, and unlock a previously set up wallet.
    """

    @staticmethod
    def GenSeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lnrpc.WalletUnlocker/GenSeed',
            v0131beta_dot_walletunlocker__pb2.GenSeedRequest.SerializeToString,
            v0131beta_dot_walletunlocker__pb2.GenSeedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitWallet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lnrpc.WalletUnlocker/InitWallet',
            v0131beta_dot_walletunlocker__pb2.InitWalletRequest.SerializeToString,
            v0131beta_dot_walletunlocker__pb2.InitWalletResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnlockWallet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lnrpc.WalletUnlocker/UnlockWallet',
            v0131beta_dot_walletunlocker__pb2.UnlockWalletRequest.SerializeToString,
            v0131beta_dot_walletunlocker__pb2.UnlockWalletResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lnrpc.WalletUnlocker/ChangePassword',
            v0131beta_dot_walletunlocker__pb2.ChangePasswordRequest.SerializeToString,
            v0131beta_dot_walletunlocker__pb2.ChangePasswordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
