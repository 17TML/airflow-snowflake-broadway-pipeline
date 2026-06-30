"""
Inserts data from the given SQL query/queries into a historical table
(idempotently), inserts a row into the signal table, and recreates the view for
this table's most recent data (if the execution date is no more than a week
before the actual date).
"""
from typing import List
from datetime import datetime, timedelta
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from dags.utils.constants import AirflowConstants

class SnowflakeHistoricalOperator(SQLExecuteQueryOperator):
    """
    Generates a transaction with the SQL to do the above described jobs and
    passes that into its superclass.
    """
    def __init__(
        self,
        select_sql: str,  # SQL query generating data to insert
        view_name: str,  # Same as the table name without _historical
        schema: str,
        database: str = AirflowConstants.DEFAULT_DATABASE,
        *args,
        **kwargs
    ) -> None:
        super().__init__(
            sql=self._generate_transaction(
                select_sql=select_sql,
                view_name=view_name,
                schema=schema,
                database=database,
            ),
            *args,
            **kwargs,
        )

    def _generate_transaction(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        sql_statements = [
            f"USE WAREHOUSE {self.warehouse};",
            f"DELETE FROM {self.historical_table} WHERE ds = '{current_date}';",
            f"INSERT INTO {self.historical_table} (ds, ...) {self.select_sql};",
            f"INSERT INTO {self.signal_table} VALUES ('{self.historical_table}', '{current_date}', 'success');"
        ]

        one_week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        if current_date > one_week_ago:
            view_name = self.historical_table.replace('_historical', '')
            sql_statements += [
                f"DROP VIEW IF EXISTS {view_name};",
                f"CREATE VIEW {view_name} AS SELECT * FROM {self.historical_table} WHERE ds = '{current_date}';",
                f"INSERT INTO {self.signal_table} VALUES ('{view_name}', '{current_date}', 'updated');"
            ]

        return sql_statements
