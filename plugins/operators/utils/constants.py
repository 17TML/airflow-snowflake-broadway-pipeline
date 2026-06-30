"""Constants shared across airflow dags/operators"""
class AirflowConstants:
    # TODO: replace this constant with your Snowflake user animal
    ANIMAL = 'DRAGON'

    SNOWFLAKE_CONN_ID = f'{ANIMAL}_conn'
    STAGE_NAME = f'{ANIMAL}_stg'
    DEFAULT_DATABASE = f'{ANIMAL}_db'
    DEFAULT_WAREHOUSE = f'{ANIMAL}_wh'
    DEFAULT_PARTITION_ID = "ds='{{ ds }}'"
    SUCCESS_STATUS = 'success'
