CREATE DATABASE agriculture_insight;

create or replace file format csv_file_format
    type = 'CSV'
    field_delimiter = ','
    field_optionally_enclosed_by='"'
    ;

CREATE OR REPLACE STAGE "AGRICULTURE_INSIGHT"."PUBLIC".agriculture_stage
    URL = 's3://agriculture-insight/snowflake'
    CREDENTIALS = (AWS_KEY_ID = ' AKIAVFTBAWJ7QQ44VRXO ' AWS_SECRET_KEY = '****************************************')
    FILE_FORMAT = CSV_FILE_FORMAT;

COPY INTO @Agriculture_stage from "AGRICULTURE_DATA_ATLAS"."AGRICULTURE"."DATA_ATLAS"


-- create Snowflake Star schema

CREATE FILE FORMAT "AGRICULTURE_INSIGHT"."PUBLIC".parquet_file_format TYPE = 'PARQUET' COMPRESSION = 'SNAPPY' BINARY_AS_TEXT = TRUE;

CREATE STAGE "AGRICULTURE_INSIGHT"."PUBLIC".data_lake_s3_stage URL = 's3://agriculture-insight/snowflake/dimensions/' CREDENTIALS = (AWS_KEY_ID = 'AKIAVFTBAWJ73EFEP6FY' AWS_SECRET_KEY = '****************************************');

CREATE STAGE "AGRICULTURE_INSIGHT"."PUBLIC".DATA_LAKE_S3_FACT_STAGE URL = 's3://agriculture-insight/snowflake/facts/' CREDENTIALS = (AWS_KEY_ID = 'AKIAVFTBAWJ73EFEP6FY' AWS_SECRET_KEY = '****************************************');