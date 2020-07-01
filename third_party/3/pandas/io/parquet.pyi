from pandas import DataFrame as DataFrame, get_option as get_option
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import get_filepath_or_buffer as get_filepath_or_buffer, is_gcs_url as is_gcs_url, is_s3_url as is_s3_url
from typing import Any, Optional

def get_engine(engine: str) -> BaseImpl: ...

class BaseImpl:
    @staticmethod
    def validate_dataframe(df: DataFrame) -> Any: ...
    def write(self, df: DataFrame, path: Any, compression: Any, **kwargs: Any) -> Any: ...
    def read(self, path: Any, columns: Optional[Any] = ..., **kwargs: Any) -> None: ...

class PyArrowImpl(BaseImpl):
    api: Any = ...
    def __init__(self) -> None: ...
    def write(self, df: DataFrame, path: Any, compression: Any = ..., coerce_timestamps: Any = ..., index: Optional[bool]=..., partition_cols: Any = ..., **kwargs: Any) -> Any: ...
    def read(self, path: Any, columns: Optional[Any] = ..., **kwargs: Any) -> Any: ...

class FastParquetImpl(BaseImpl):
    api: Any = ...
    def __init__(self) -> None: ...
    def write(self, df: DataFrame, path: Any, compression: Any = ..., index: Any = ..., partition_cols: Any = ..., **kwargs: Any) -> Any: ...
    def read(self, path: Any, columns: Optional[Any] = ..., **kwargs: Any) -> Any: ...

def to_parquet(df: DataFrame, path: Any, engine: str=..., compression: Any = ..., index: Optional[bool]=..., partition_cols: Any = ..., **kwargs: Any) -> Any: ...
def read_parquet(path: Any, engine: str=..., columns: Any = ..., **kwargs: Any) -> Any: ...