# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stateservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stateservice.proto',
  package='lnrpc',
  syntax='proto3',
  serialized_options=b'Z%github.com/lightningnetwork/lnd/lnrpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12stateservice.proto\x12\x05lnrpc\"\x17\n\x15SubscribeStateRequest\";\n\x16SubscribeStateResponse\x12!\n\x05state\x18\x01 \x01(\x0e\x32\x12.lnrpc.WalletState*I\n\x0bWalletState\x12\x10\n\x0cNON_EXISTING\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\x0c\n\x08UNLOCKED\x10\x02\x12\x0e\n\nRPC_ACTIVE\x10\x03\x32X\n\x05State\x12O\n\x0eSubscribeState\x12\x1c.lnrpc.SubscribeStateRequest\x1a\x1d.lnrpc.SubscribeStateResponse0\x01\x42\'Z%github.com/lightningnetwork/lnd/lnrpcb\x06proto3'
)

_WALLETSTATE = _descriptor.EnumDescriptor(
  name='WalletState',
  full_name='lnrpc.WalletState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NON_EXISTING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCKED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNLOCKED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RPC_ACTIVE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=115,
  serialized_end=188,
)
_sym_db.RegisterEnumDescriptor(_WALLETSTATE)

WalletState = enum_type_wrapper.EnumTypeWrapper(_WALLETSTATE)
NON_EXISTING = 0
LOCKED = 1
UNLOCKED = 2
RPC_ACTIVE = 3



_SUBSCRIBESTATEREQUEST = _descriptor.Descriptor(
  name='SubscribeStateRequest',
  full_name='lnrpc.SubscribeStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=52,
)


_SUBSCRIBESTATERESPONSE = _descriptor.Descriptor(
  name='SubscribeStateResponse',
  full_name='lnrpc.SubscribeStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='lnrpc.SubscribeStateResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=113,
)

_SUBSCRIBESTATERESPONSE.fields_by_name['state'].enum_type = _WALLETSTATE
DESCRIPTOR.message_types_by_name['SubscribeStateRequest'] = _SUBSCRIBESTATEREQUEST
DESCRIPTOR.message_types_by_name['SubscribeStateResponse'] = _SUBSCRIBESTATERESPONSE
DESCRIPTOR.enum_types_by_name['WalletState'] = _WALLETSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeStateRequest = _reflection.GeneratedProtocolMessageType('SubscribeStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBESTATEREQUEST,
  '__module__' : 'stateservice_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SubscribeStateRequest)
  })
_sym_db.RegisterMessage(SubscribeStateRequest)

SubscribeStateResponse = _reflection.GeneratedProtocolMessageType('SubscribeStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBESTATERESPONSE,
  '__module__' : 'stateservice_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SubscribeStateResponse)
  })
_sym_db.RegisterMessage(SubscribeStateResponse)


DESCRIPTOR._options = None

_STATE = _descriptor.ServiceDescriptor(
  name='State',
  full_name='lnrpc.State',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=190,
  serialized_end=278,
  methods=[
  _descriptor.MethodDescriptor(
    name='SubscribeState',
    full_name='lnrpc.State.SubscribeState',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBESTATEREQUEST,
    output_type=_SUBSCRIBESTATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATE)

DESCRIPTOR.services_by_name['State'] = _STATE

# @@protoc_insertion_point(module_scope)
