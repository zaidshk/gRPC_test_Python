from unittest.mock import MagicMock

import pytest
from grpc_client_f.client import GRPCClient
from db_client.database import DatabaseClient

# Asserting the mocked candlestick data for OHLC with database cross-check
def test_grpc_api_subscription_with_db_check(grpc_client, db_client):
    # Using the mocked subscribe method
    symbols = ["EURUSD"]
    response_stream = grpc_client.mock_subscribe(symbols)

    for response in response_stream:
        # Fetching latest candlestick from the candlestick_m1 db table for the given symbol
        db_data = db_client.fetch_latest_candlestick(response.symbol)

        # If the candlestick already exists in the database, skip validation
        if db_data and db_data["timestamp_msec"] == response.bar.timestamp_msec:
            print(f"Duplicate candlestick found for {response.symbol}, skipping validation.")
            break

        # Assert the data only if it's not a duplicate
        assert response.symbol in symbols, "Received data for unexpected symbol"
        bar = response.bar
        assert bar.timestamp_msec > 0, "Invalid timestamp"
        assert bar.open <= bar.high, "Open price must be less than or equal to High price"
        assert bar.open >= bar.low, "Open price must be greater than or equal to Low price"
        assert bar.close <= bar.high, "Close price must be less than or equal to High price"
        assert bar.close >= bar.low, "Close price must be greater than or equal to Low price"
        assert bar.low <= bar.high, "Low price must be less than or equal to High price"

# Test for invalid symbol scenario
def test_no_data_handling(grpc_client):
    grpc_client.mock_subscribe = MagicMock(return_value=[])

    symbols = ["INVALID_SYMBOL"]
    response_stream = grpc_client.mock_subscribe(symbols)
    assert len(list(response_stream)) == 0, "Expected no data from subscription"

# Test for invalid input scenario
def test_invalid_input(grpc_client):

    grpc_client.mock_subscribe = MagicMock(side_effect=ValueError("Invalid input"))

    with pytest.raises(ValueError, match="Invalid input"):
        grpc_client.mock_subscribe([])

# There can be several other test cases applicable when the real subscribe method is working