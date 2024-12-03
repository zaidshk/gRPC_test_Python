import mysql.connector

class DatabaseClient:
    # mysql db connection
    def __init__(self, host="localhost", user="root", password="root", database="candlestick_db"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3307 # this is not the regular default port, change it if required
        )
        self.cursor = self.conn.cursor(dictionary=True)

# fetching data from the mysql db candlesticks_m1 tabe
    def fetch_latest_candlestick(self, symbol):
        query = f"""
        SELECT * FROM candlesticks_m1 
        WHERE symbol = %s 
        ORDER BY timestamp_msec DESC LIMIT 1
        """
        self.cursor.execute(query, (symbol,))
        return self.cursor.fetchone()

# close conn
    def close(self):
        self.cursor.close()
        self.conn.close()
