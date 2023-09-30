from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextToCount(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class WordCount(_message.Message):
    __slots__ = ["WordOccurrence"]
    class WordOccurrenceEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    WORDOCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    WordOccurrence: _containers.ScalarMap[str, int]
    def __init__(self, WordOccurrence: _Optional[_Mapping[str, int]] = ...) -> None: ...

class tuples(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: int
    def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...

class TextToCombine(_message.Message):
    __slots__ = ["allwords"]
    ALLWORDS_FIELD_NUMBER: _ClassVar[int]
    allwords: _containers.RepeatedCompositeFieldContainer[tuples]
    def __init__(self, allwords: _Optional[_Iterable[_Union[tuples, _Mapping]]] = ...) -> None: ...

class TotalCount(_message.Message):
    __slots__ = ["WordOccurrence"]
    class WordOccurrenceEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    WORDOCCURRENCE_FIELD_NUMBER: _ClassVar[int]
    WordOccurrence: _containers.ScalarMap[str, int]
    def __init__(self, WordOccurrence: _Optional[_Mapping[str, int]] = ...) -> None: ...
