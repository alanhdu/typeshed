# Stubs for pprint

# Based on http://docs.python.org/2/library/pprint.html
# Based on http://docs.python.org/3/library/pprint.html

import sys
from typing import Any, Dict, Tuple, IO, Optional

if sys.version_info >= (3, 8):
    def pformat(
        o: object, indent: int = ..., width: int = ..., depth: Optional[int] = ..., *, compact: bool = ..., sort_dicts: bool = ...
    ) -> str: ...

elif sys.version_info >= (3, 4):
    def pformat(o: object, indent: int = ..., width: int = ...,
                depth: Optional[int] = ..., *, compact: bool = ...) -> str: ...
else:
    def pformat(o: object, indent: int = ..., width: int = ...,
                depth: Optional[int] = ...) -> str: ...

if sys.version_info >= (3, 8):
    def pp(
        o: object,
        stream: Optional[IO[str]] = ...,
        indent: int = ...,
        width: int = ...,
        depth: Optional[int] = ...,
        *,
        compact: bool = ...,
        sort_dicts: bool = ...,
    ) -> None: ...

if sys.version_info >= (3, 8):
    def pprint(
        o: object,
        stream: Optional[IO[str]] = ...,
        indent: int = ...,
        width: int = ...,
        depth: Optional[int] = ...,
        *,
        compact: bool = ...,
        sort_dicts: bool = ...,
    ) -> None: ...

elif sys.version_info >= (3, 4):
    def pprint(o: object, stream: Optional[IO[str]] = ..., indent: int = ..., width: int = ...,
               depth: Optional[int] = ..., *, compact: bool = ...) -> None: ...
else:
    def pprint(o: object, stream: Optional[IO[str]] = ..., indent: int = ..., width: int = ...,
               depth: Optional[int] = ...) -> None: ...

def isreadable(o: object) -> bool: ...
def isrecursive(o: object) -> bool: ...
def saferepr(o: object) -> str: ...

class PrettyPrinter:
    if sys.version_info >= (3, 8):
        def __init__(
            self,
            indent: int = ...,
            width: int = ...,
            depth: Optional[int] = ...,
            stream: Optional[IO[str]] = ...,
            *,
            compact: bool = ...,
            sort_dicts: bool = ...,
        ) -> None: ...
    elif sys.version_info >= (3, 4):
        def __init__(self, indent: int = ..., width: int = ..., depth: Optional[int] = ...,
                     stream: Optional[IO[str]] = ..., *, compact: bool = ...) -> None: ...
    else:
        def __init__(self, indent: int = ..., width: int = ..., depth: Optional[int] = ...,
                     stream: Optional[IO[str]] = ...) -> None: ...

    def pformat(self, o: object) -> str: ...
    def pprint(self, o: object) -> None: ...
    def isreadable(self, o: object) -> bool: ...
    def isrecursive(self, o: object) -> bool: ...
    def format(self, o: object, context: Dict[int, Any], maxlevels: int,
               level: int) -> Tuple[str, bool, bool]: ...
