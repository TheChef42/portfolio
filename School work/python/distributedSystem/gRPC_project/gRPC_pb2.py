# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gRPC.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngRPC.proto\"\x1b\n\x0bTextToCount\x12\x0c\n\x04text\x18\x01 \x01(\t\"z\n\tWordCount\x12\x36\n\x0eWordOccurrence\x18\x01 \x03(\x0b\x32\x1e.WordCount.WordOccurrenceEntry\x1a\x35\n\x13WordOccurrenceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"$\n\x06tuples\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03\"*\n\rTextToCombine\x12\x19\n\x08\x61llwords\x18\x01 \x03(\x0b\x32\x07.tuples\"|\n\nTotalCount\x12\x37\n\x0eWordOccurrence\x18\x01 \x03(\x0b\x32\x1f.TotalCount.WordOccurrenceEntry\x1a\x35\n\x13WordOccurrenceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x32h\n\x13\x46requencyCalculator\x12\'\n\tCalculate\x12\x0c.TextToCount\x1a\n.WordCount\"\x00\x12(\n\x07\x43ombine\x12\x0e.TextToCombine\x1a\x0b.TotalCount\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gRPC_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WORDCOUNT_WORDOCCURRENCEENTRY._options = None
  _WORDCOUNT_WORDOCCURRENCEENTRY._serialized_options = b'8\001'
  _TOTALCOUNT_WORDOCCURRENCEENTRY._options = None
  _TOTALCOUNT_WORDOCCURRENCEENTRY._serialized_options = b'8\001'
  _globals['_TEXTTOCOUNT']._serialized_start=14
  _globals['_TEXTTOCOUNT']._serialized_end=41
  _globals['_WORDCOUNT']._serialized_start=43
  _globals['_WORDCOUNT']._serialized_end=165
  _globals['_WORDCOUNT_WORDOCCURRENCEENTRY']._serialized_start=112
  _globals['_WORDCOUNT_WORDOCCURRENCEENTRY']._serialized_end=165
  _globals['_TUPLES']._serialized_start=167
  _globals['_TUPLES']._serialized_end=203
  _globals['_TEXTTOCOMBINE']._serialized_start=205
  _globals['_TEXTTOCOMBINE']._serialized_end=247
  _globals['_TOTALCOUNT']._serialized_start=249
  _globals['_TOTALCOUNT']._serialized_end=373
  _globals['_TOTALCOUNT_WORDOCCURRENCEENTRY']._serialized_start=112
  _globals['_TOTALCOUNT_WORDOCCURRENCEENTRY']._serialized_end=165
  _globals['_FREQUENCYCALCULATOR']._serialized_start=375
  _globals['_FREQUENCYCALCULATOR']._serialized_end=479
# @@protoc_insertion_point(module_scope)
