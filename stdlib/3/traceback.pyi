# Stubs for traceback

from typing import List
from types import TracebackType
import typing

# TODO signatures
def format_exception_only(etype, value): ...
def format_exception(type: type, value: List[str], tb: TracebackType, limit: int, chain: bool) -> str: ...
def format_tb(traceback): ...
def print_exc(limit=..., file=..., chain=...): ...
def format_exc(limit: int = ..., chain: bool = ...) -> str: ...
def extract_stack(f=..., limit=...): ...
def extract_tb(traceback, limit=...): ...
def format_list(list): ...

# TODO add more
