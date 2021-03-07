import pyodbc
from infrastructor.data.connectors.ConnectorStrategy import ConnectorStrategy
from models.configs.DatabaseConfig import DatabaseConfig


class MssqlDbConnector(ConnectorStrategy):
    def __init__(self, database_config: DatabaseConfig):
        self.database_config: DatabaseConfig = database_config
        self.database_config.driver = 'ODBC Driver 17 for SQL Server'
        # ;Client_CSet=UTF-8;Server_CSet=WINDOWS-1251
        self.connection_string = 'DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;Client_CSet=UTF-8;Server_CSet=WINDOWS-1251' % (
            self.database_config.driver, self.database_config.host, self.database_config.database,
            self.database_config.username, self.database_config.password)

        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = pyodbc.connect(self.connection_string)  # ,ansi=True)
        self.connection.setencoding(encoding='utf-8')
        self.cursor = self.connection.cursor()
        self.cursor.setinputsizes([(pyodbc.SQL_WVARCHAR, 0, 0)])

    def disconnect(self):
        try:
            if self.cursor is not None:
                self.cursor.close()

            if self.connection is not None:
                self.connection.close()
        except Exception:
            pass

    def execute_many(self, query, data):
        self.cursor.fast_executemany = True
        try:
            self.cursor.executemany(query, data)
            self.connection.commit()
        except Exception as error:
            try:
                self.connection.rollback()
                self.cursor.fast_executemany = False
                self.cursor.executemany(query, data)
                self.connection.commit()
            except Exception as error:
                self.connection.rollback()
                self.cursor.close()
                raise

    def get_target_query_indexer(self):
        indexer = '?'
        return indexer
