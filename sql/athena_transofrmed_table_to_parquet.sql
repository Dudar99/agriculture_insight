CREATE EXTERNAL TABLE `agriculture_atlas_transformed`(
  `dataset` string COMMENT '',
  `path` string COMMENT '',
  `country` string COMMENT '',
  `country_iso_code` string COMMENT '',
  `topic` string COMMENT '',
  `subtopic` string COMMENT '',
  `indicator` string COMMENT '',
  `description` string COMMENT '',
  `source` string COMMENT '',
  `uri` string COMMENT '',
  `year` bigint COMMENT '',
  `month` int COMMENT '',
  `unit` string COMMENT '',
  `date` date COMMENT '',
  `value` float COMMENT '')
ROW FORMAT SERDE
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://agriculture-insight/snowflake/transformed/'
TBLPROPERTIES (
  'has_encrypted_data'='false',
  'parquet.compression'='SNAPPY',
  'presto_query_id'='20211018_210428_00018_izjw8')