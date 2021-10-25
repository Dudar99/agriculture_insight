from scripts.metadata import STAR_TABLES, DIM_TABLES, FACT_TABLES
from unitls.snowflake_connect import SnowflakeDB


def snowflake_create_table(table_metadata):
    db = SnowflakeDB()
    db.create_table_from_metadata_dict(table_metadata)


def snowflake_drop_table(table_name):
    db = SnowflakeDB()
    db.drop_table(table_name)


def generate_snowflake_star_schema():
    for table_metadata in STAR_TABLES:
        snowflake_create_table(table_metadata)


def drop_star_schema():
    for table_name in map(lambda x: x["name"], STAR_TABLES):
        snowflake_drop_table(table_name)


def load_dimensions_data_from_s3():
    db = SnowflakeDB()
    for table_metadata in DIM_TABLES:
        db.load_data_from_s3(table_metadata, stage="@DATA_LAKE_S3_STAGE/dimensions")
    for table_metadata in FACT_TABLES:
        db.load_data_from_s3(table_metadata, stage="@DATA_LAKE_S3_STAGE/facts")



if __name__ == '__main__':
    # drop_star_schema()
    # generate_snowflake_star_schema()
    load_dimensions_data_from_s3()