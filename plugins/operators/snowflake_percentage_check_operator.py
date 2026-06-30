"""
Checks that a set of column names are valid percentages/fractions, i.e., have a
value between 0-100 (percentages) or 0-1 (fractions).
"""
from typing import List, Optional

from airflow.providers.common.sql.operators.sql import SQLCheckOperator
from utils.constants import AirflowConstants

class SnowflakePercentageCheckOperator(SQLCheckOperator):
    """
    Generates a set of SQL statements to ensure all the given columns fall in
    the correct range and then passes that into its superclass.
    """
    def __init__(
        self,
        column_names: List[str],
        table_name: str,
        schema: str,
        is_fraction: bool = True,  # True if range is 0-1, False if 0-100
        database: str = AirflowConstants.DEFAULT_DATABASE,
        partition_id: Optional[str] = None,
        *args,
        **kwargs
    ) -> None:
        raise NotImplementedError
