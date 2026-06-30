"""Checks whether a table partition has already landed"""
from airflow.sensors.base import BaseSensorOperator
from airflow.utils.context import Context
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from utils.constants import AirflowConstants

class SnowflakeSignalSensor(BaseSensorOperator):
    """Checks the signal table to see if a table partition has landed"""
    def __init__(
        self,
        conn_id: str,
        schema: str,
        table_name: str,
        database: str = AirflowConstants.DEFAULT_DATABASE,
        partition_id: str = AirflowConstants.DEFAULT_PARTITION_ID,
        status: str = AirflowConstants.SUCCESS_STATUS,
        *args,
        **kwargs
    ) -> None:
        raise NotImplementedError

    def poke(self, context: Context) -> bool:
        """
        Returns True if the signal table has a success row corresponding to the
        given database/schema/table/partition and False otherwise.
        """
        hook = SnowflakeHook(snowflake_conn_id=self.snowflake_conn_id)
        sql = f"""
        SELECT 1 FROM {self.database}.{self.schema}.{self.table}
        WHERE partition_id = '{self.partition_id}' AND status = 'ready'
        LIMIT 1;
        """
        result = hook.get_first(sql)
        return result is not None
