from common.settings import COUNTRY_DIM, ATLAS_TABLE_NAME, DATE_DIM, INDICATOR_DIM, DIM_TABLES_LOCATION, SOURCE_DIM, \
    TOPIC_DIM, \
    UNIT_DIM


def fieldify(columns: list):
    return ", ".join(columns)


def generate_select_distinct_values_query(table_metadata: dict) -> str:
    pks = table_metadata.get('pk').keys()
    cols = table_metadata.get('cols').keys()
    cols_string = fieldify(cols)
    pks_string = fieldify(pks)

    sql = f"""with tmp as (SELECT distinct  {cols_string}  FROM {ATLAS_TABLE_NAME} )

        select row_number() over () as {pks_string}, {cols_string} from tmp
        """
    return sql


def ctas_athena(table_metadata: dict):
    table_name = table_metadata['name']
    location = DIM_TABLES_LOCATION + table_name
    ctas_sql = f"""CREATE TABLE {table_name} WITH (
                format = 'Parquet',
                write_compression = 'SNAPPY',
                external_location = '{location}'
            ) AS """

    select_sql = generate_select_distinct_values_query(table_metadata)

    final_sql = ctas_sql + select_sql
    return final_sql


def generate_athena_tables():
    # CONNECT to Athena using pyathena and execute infrustructure building
    pass
