# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chart.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'chart.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63hart.proto\x12\x0c\x65xinity.test\"S\n\x10SubscribeRequest\x12*\n\ttimeframe\x18\x01 \x01(\x0e\x32\x17.exinity.test.Timeframe\x12\x13\n\x0bsymbol_list\x18\x02 \x03(\t\"]\n\x0b\x43\x61ndlestick\x12\x16\n\x0etimestamp_msec\x18\x01 \x01(\x04\x12\x0c\n\x04open\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0b\n\x03low\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\"K\n\x11SubscribeResponse\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12&\n\x03\x62\x61r\x18\x02 \x01(\x0b\x32\x19.exinity.test.Candlestick*:\n\tTimeframe\x12\x15\n\x11TIMEFRAME_UNKNOWN\x10\x00\x12\x16\n\x12TIMEFRAME_MINUTE_1\x10\x01\x32^\n\x0c\x43hartService\x12N\n\tSubscribe\x12\x1e.exinity.test.SubscribeRequest\x1a\x1f.exinity.test.SubscribeResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chart_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TIMEFRAME']._serialized_start=286
  _globals['_TIMEFRAME']._serialized_end=344
  _globals['_SUBSCRIBEREQUEST']._serialized_start=29
  _globals['_SUBSCRIBEREQUEST']._serialized_end=112
  _globals['_CANDLESTICK']._serialized_start=114
  _globals['_CANDLESTICK']._serialized_end=207
  _globals['_SUBSCRIBERESPONSE']._serialized_start=209
  _globals['_SUBSCRIBERESPONSE']._serialized_end=284
  _globals['_CHARTSERVICE']._serialized_start=346
  _globals['_CHARTSERVICE']._serialized_end=440
# @@protoc_insertion_point(module_scope)
