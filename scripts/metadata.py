ATLAS_TABLE_NAME = "agriculture_atlas_transformed"
DIM_TABLES_LOCATION = 's3://agriculture-insight/snowflake/dimensions/'
FACT_TABLES_LOCATION = 's3://agriculture-insight/snowflake/facts/'
SNOWFLAKE_ACCOUNT_NAME = 'iqa83018.us-east-1'
DEFAULT_SNOWFLAKE_ROLE = 'SYSADMIN'
DEFAULT_SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
DEFAULT_SNOWFLAKE_DATABASE = 'AGRICULTURE_INSIGHT'
DEFAULT_SNOWFLAKE_SCHEMA = 'PUBLIC'

AGR_FACT = {
    'pk': {'measure_id': 'bigint'},
    'cols': {
        'value': 'float',
        'country_id': 'bigint',
        'date_id': 'bigint',
        'indicator_id': 'bigint',
        'source_id': 'bigint',
        'topic_id': 'bigint',
        'unit_id': 'bigint'
    },
    'name': 'agr_fact'
}
COUNTRY_DIM = {
    'pk': {
        'country_id': 'bigint'
    },
    'cols': {
        'country': 'string',
        'country_iso_code': 'string'
    },
    "name": 'country_dim'
}
DATE_DIM = {
    'pk': {
        'date_id': 'bigint'
    },
    'cols': {
        'year': 'int',
        'month': 'int'
    },
    "name": 'date_dim'

}
UNIT_DIM = {
    'pk': {
        'unit_id': 'bigint'
    },
    'cols': {
        'unit': 'string'
    },
    "name": 'unit_dim'

}

TOPIC_DIM = {
    'pk': {
        'topic_id': 'bigint'
    },
    'cols': {
        'subtopic': 'string'
    },
    "name": 'topic_dim'

}

INDICATOR_DIM = {
    'pk': {
        'indicator_id': 'bigint'
    },
    'cols': {
        'indicator': 'string',
        'description': 'string'
    },
    "name": 'indicator_dim'

}

SOURCE_DIM = {
    'pk': {
        'source_id': 'bigint'
    },
    'cols': {
        'source': 'string',
        'uri': 'string'
    },
    "name": 'source_dim'

}

DIM_TABLES = [SOURCE_DIM, INDICATOR_DIM, TOPIC_DIM, UNIT_DIM, DATE_DIM, COUNTRY_DIM]
FACT_TABLES = [AGR_FACT]
STAR_TABLES = DIM_TABLES + FACT_TABLES
