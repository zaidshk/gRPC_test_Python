import pytest
from grpc_client_f.client import GRPCClient
from db_client.database import DatabaseClient

@pytest.fixture  # GRPCClient ficture
def grpc_client():

    client = GRPCClient()
    yield client

@pytest.fixture # DatabaseClient ficture
def db_client():

    client = DatabaseClient()
    yield client
    client.close()
