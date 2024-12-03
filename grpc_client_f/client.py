import grpc
from unittest.mock import MagicMock
from grpc_client_f.chart_pb2 import SubscribeRequest, Timeframe, Candlestick # classes not found in gRPC stub generated, therefore mocked the response using MagicMock
from grpc_client_f.chart_pb2_grpc import ChartServiceStub

class GRPCClient:
    # initialize stub/services
    def __init__(self, host="localhost", port=50051):

        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.client = ChartServiceStub(self.channel)


        # Mocked implementation of the Subscribe method.
    def mock_subscribe(self, symbols, timeframe=Timeframe.TIMEFRAME_MINUTE_1):

        mock_response = MagicMock()
        mock_response.symbol = symbols[0]
        mock_response.bar = Candlestick(
            timestamp_msec=1703930400000,
            open=1.1000000,
            high=1.2000000,
            low=1.0500000,
            close=1.1500000,
        )
        return [mock_response]
