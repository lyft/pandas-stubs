from pandas.io.excel._base import ExcelWriter as ExcelWriter
from typing import Any, Optional

class _XlwtWriter(ExcelWriter):
    engine: str = ...
    supported_extensions: Any = ...
    book: Any = ...
    fm_datetime: Any = ...
    fm_date: Any = ...
    def __init__(self, path: Any, engine: Optional[Any] = ..., encoding: Optional[Any] = ..., mode: str = ..., **engine_kwargs: Any) -> None: ...
    def save(self) -> Any: ...
    def write_cells(self, cells: Any, sheet_name: Optional[Any] = ..., startrow: int = ..., startcol: int = ..., freeze_panes: Optional[Any] = ...) -> None: ...