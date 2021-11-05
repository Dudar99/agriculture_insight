CREATE EXTERNAL TABLE `agriculture_atlas_extract`(
  `dataset` string,
  `path` string,
  `country` string,
  `country_iso_code` string,
  `topic` string,
  `subtopic` string,
  `indicator` string,
  `description` string,
  `source` string,
  `uri` string,
  `year` bigint,
  `month` int,
  `unit` string,
  `date` date,
  `value` float)
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY '\t'
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://agriculture-insight/snowflake/snowflake_export_stage'
TBLPROPERTIES (
  'has_encrypted_data'='false',
  'transient_lastDdlTime'='1634590724')