This is a Python automation framework I created as part of a test assessment for validating candlestick data in a trading system.
The framework interacts with a MySQL database (candlesticks_m1 table) and a mocked gRPC service for testing the subscription and validation of candlestick data.

Prerequisite:
1 - Before running the project, create a MySQL database 'candlestick_db' and table 'candlestick_m1'
CREATE TABLE `candlesticks_m1` (
 `symbol` VARCHAR(32) NOT NULL,
 `timestamp_msec` BIGINT(20) unsigned NOT NULL,
 `open` DECIMAL(24,6) NOT NULL,
 `high` DECIMAL(24,6) NOT NULL,
 `low` DECIMAL(24,6) NOT NULL,
 `close` DECIMAL(24,6) NOT NULL,
 PRIMARY KEY (`symbol`,`timestamp`)
)
2 - You will need Python setup and IDE (Pycharm)
3 - Make sure your MySQL server is running locally on localhost with port 3307.

Folder and files:
1. db_client/database.py - Handles the connection to the MySQL database (candlestick_db).
2. grpc_client_f/client.py - Implements the gRPC client. Due to issues with the chart.proto file, I created a mock_subscribe method to simulate the Subscribe functionality.
3. tests/conftest.py - Contains pytest fixtures for initializing and tearing down the DatabaseClient and GRPCClient objects.
4. tests/test_grpc_api.py - Contains test cases
5. chart.proto - proto file provided with the test assesment
6. requirements.txt - Lists the Python libraries required for the project.
7. pytest.ini - Configures pytest to locate test files and apply default options for test runs.


Clone the project from the Repo link -


Install dependencies
pip install -r requirements.txt


Run Tests: Execute the test_grpc_api.py file using pytest
Syntax: pytest tests/test_grpc_api.py
(Might encounter some issues as the SubscribeRequest method throws error in the client.py file) - Individual test can be executed by clicking on the play button on the test file in pycharm




Thank you
It gave me great learning opportunities to work with:
MySQL database integration.
Mocking in Python.
Testing frameworks like pytest.
Handling gRPC service challenges.
