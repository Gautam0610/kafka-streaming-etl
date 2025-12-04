import psycopg2
from sinks.base_sink import BaseSink

class PostgreSQLSink(BaseSink):
    def __init__(self, config):
        super().__init__(config)
        self.host = config['host']
        self.port = config['port']
        self.database = config['database']
        self.user = config['user']
        self.password = config['password']
        self.table = config['table']

        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
            print("Connected to PostgreSQL")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def write(self, data):
        """
        Writes data to a PostgreSQL table.
        """
        if not self.conn or not self.cursor:
            self.connect()

        try:
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql = f"INSERT INTO {self.table} ({columns}) VALUES ({values})"
            self.cursor.execute(sql, list(data.values()))
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error writing to PostgreSQL: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Closed PostgreSQL connection")