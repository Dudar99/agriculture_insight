from snowflake import connector
import os

from common.settings import SNOWFLAKE_ACCOUNT_NAME, DEFAULT_SNOWFLAKE_ROLE, DEFAULT_SNOWFLAKE_WAREHOUSE, \
    DEFAULT_SNOWFLAKE_DATABASE, DEFAULT_SNOWFLAKE_SCHEMA, INDICATOR_DIM


class SnowflakeConnector:
    def __init__(self, account: str = SNOWFLAKE_ACCOUNT_NAME, role: str = DEFAULT_SNOWFLAKE_ROLE,
                 warehouse=DEFAULT_SNOWFLAKE_WAREHOUSE, database=DEFAULT_SNOWFLAKE_DATABASE,
                 schema=DEFAULT_SNOWFLAKE_SCHEMA):
        self.__user = os.environ.get('SNOWFLAKE_USER')
        self.__password = os.environ.get('SNOWFLAKE_PASSWORD')
        self.conn = connector.connect(user=self.__user, password=self.__password, account=account,
                                      role=role,
                                      warehouse=warehouse,
                                      database=database,
                                      schema=schema)
        self.cursor = self.conn.cursor()

    def query(self, query_str):
        return self.cursor.execute(query_str)


class SnowflakeDB:
    def __init__(self):
        self.conn = SnowflakeConnector()

    def create_table_from_metadata_dict(self, table_metadata: dict):
        cols = []
        for k, v in list(table_metadata['cols'].items()) + list(table_metadata['pk'].items()):
            cols.append(f"{k} {customize_to_snow_type(v)}")

        cols = ", ".join(cols)
        sql = f"""CREATE TABLE {table_metadata['name']} ({cols});"""
        self.conn.query(sql)

    def drop_table(self, table_name):
        self.conn.query(f"DROP TABLE IF EXISTS {table_name}")

    def load_data_from_s3(self, table_metadata, stage="@DATA_LAKE_S3_STAGE"):

        table_name = table_metadata["name"]
        cols = []
        for col, dtype in list(table_metadata['cols'].items()) + list(table_metadata['pk'].items()):
            cols.append(f"$1:{col}::{customize_to_snow_type(dtype)}")
        cols = ", ".join(cols)
        sql = f"""
        copy into {table_name} from (
        select
              {cols}
              from {stage}/{table_name}/)
              file_format =  PARQUET_FILE_FORMAT
        """
        self.conn.query(sql)


def customize_to_snow_type(t: str) -> str:
    if t == 'bigint':
        return "decimal(38, 0)"
    return t
