# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: autopilotrpc/autopilot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='autopilotrpc/autopilot.proto',
  package='autopilotrpc',
  syntax='proto3',
  serialized_options=b'Z2github.com/lightningnetwork/lnd/lnrpc/autopilotrpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x61utopilotrpc/autopilot.proto\x12\x0c\x61utopilotrpc\"\x0f\n\rStatusRequest\" \n\x0eStatusResponse\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\"%\n\x13ModifyStatusRequest\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"\x16\n\x14ModifyStatusResponse\"A\n\x12QueryScoresRequest\x12\x0f\n\x07pubkeys\x18\x01 \x03(\t\x12\x1a\n\x12ignore_local_state\x18\x02 \x01(\x08\"\xfe\x01\n\x13QueryScoresResponse\x12\x42\n\x07results\x18\x01 \x03(\x0b\x32\x31.autopilotrpc.QueryScoresResponse.HeuristicResult\x1a\xa2\x01\n\x0fHeuristicResult\x12\x11\n\theuristic\x18\x01 \x01(\t\x12M\n\x06scores\x18\x02 \x03(\x0b\x32=.autopilotrpc.QueryScoresResponse.HeuristicResult.ScoresEntry\x1a-\n\x0bScoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x90\x01\n\x10SetScoresRequest\x12\x11\n\theuristic\x18\x01 \x01(\t\x12:\n\x06scores\x18\x02 \x03(\x0b\x32*.autopilotrpc.SetScoresRequest.ScoresEntry\x1a-\n\x0bScoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x13\n\x11SetScoresResponse2\xc9\x02\n\tAutopilot\x12\x43\n\x06Status\x12\x1b.autopilotrpc.StatusRequest\x1a\x1c.autopilotrpc.StatusResponse\x12U\n\x0cModifyStatus\x12!.autopilotrpc.ModifyStatusRequest\x1a\".autopilotrpc.ModifyStatusResponse\x12R\n\x0bQueryScores\x12 .autopilotrpc.QueryScoresRequest\x1a!.autopilotrpc.QueryScoresResponse\x12L\n\tSetScores\x12\x1e.autopilotrpc.SetScoresRequest\x1a\x1f.autopilotrpc.SetScoresResponseB4Z2github.com/lightningnetwork/lnd/lnrpc/autopilotrpcb\x06proto3'
)




_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='autopilotrpc.StatusRequest',
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
  serialized_start=46,
  serialized_end=61,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='autopilotrpc.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='active', full_name='autopilotrpc.StatusResponse.active', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=63,
  serialized_end=95,
)


_MODIFYSTATUSREQUEST = _descriptor.Descriptor(
  name='ModifyStatusRequest',
  full_name='autopilotrpc.ModifyStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='autopilotrpc.ModifyStatusRequest.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=97,
  serialized_end=134,
)


_MODIFYSTATUSRESPONSE = _descriptor.Descriptor(
  name='ModifyStatusResponse',
  full_name='autopilotrpc.ModifyStatusResponse',
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
  serialized_start=136,
  serialized_end=158,
)


_QUERYSCORESREQUEST = _descriptor.Descriptor(
  name='QueryScoresRequest',
  full_name='autopilotrpc.QueryScoresRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pubkeys', full_name='autopilotrpc.QueryScoresRequest.pubkeys', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ignore_local_state', full_name='autopilotrpc.QueryScoresRequest.ignore_local_state', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=160,
  serialized_end=225,
)


_QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY = _descriptor.Descriptor(
  name='ScoresEntry',
  full_name='autopilotrpc.QueryScoresResponse.HeuristicResult.ScoresEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='autopilotrpc.QueryScoresResponse.HeuristicResult.ScoresEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='autopilotrpc.QueryScoresResponse.HeuristicResult.ScoresEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=482,
)

_QUERYSCORESRESPONSE_HEURISTICRESULT = _descriptor.Descriptor(
  name='HeuristicResult',
  full_name='autopilotrpc.QueryScoresResponse.HeuristicResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heuristic', full_name='autopilotrpc.QueryScoresResponse.HeuristicResult.heuristic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scores', full_name='autopilotrpc.QueryScoresResponse.HeuristicResult.scores', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=482,
)

_QUERYSCORESRESPONSE = _descriptor.Descriptor(
  name='QueryScoresResponse',
  full_name='autopilotrpc.QueryScoresResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='autopilotrpc.QueryScoresResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_QUERYSCORESRESPONSE_HEURISTICRESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=482,
)


_SETSCORESREQUEST_SCORESENTRY = _descriptor.Descriptor(
  name='ScoresEntry',
  full_name='autopilotrpc.SetScoresRequest.ScoresEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='autopilotrpc.SetScoresRequest.ScoresEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='autopilotrpc.SetScoresRequest.ScoresEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=482,
)

_SETSCORESREQUEST = _descriptor.Descriptor(
  name='SetScoresRequest',
  full_name='autopilotrpc.SetScoresRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heuristic', full_name='autopilotrpc.SetScoresRequest.heuristic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scores', full_name='autopilotrpc.SetScoresRequest.scores', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SETSCORESREQUEST_SCORESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=485,
  serialized_end=629,
)


_SETSCORESRESPONSE = _descriptor.Descriptor(
  name='SetScoresResponse',
  full_name='autopilotrpc.SetScoresResponse',
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
  serialized_start=631,
  serialized_end=650,
)

_QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY.containing_type = _QUERYSCORESRESPONSE_HEURISTICRESULT
_QUERYSCORESRESPONSE_HEURISTICRESULT.fields_by_name['scores'].message_type = _QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY
_QUERYSCORESRESPONSE_HEURISTICRESULT.containing_type = _QUERYSCORESRESPONSE
_QUERYSCORESRESPONSE.fields_by_name['results'].message_type = _QUERYSCORESRESPONSE_HEURISTICRESULT
_SETSCORESREQUEST_SCORESENTRY.containing_type = _SETSCORESREQUEST
_SETSCORESREQUEST.fields_by_name['scores'].message_type = _SETSCORESREQUEST_SCORESENTRY
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['ModifyStatusRequest'] = _MODIFYSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ModifyStatusResponse'] = _MODIFYSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['QueryScoresRequest'] = _QUERYSCORESREQUEST
DESCRIPTOR.message_types_by_name['QueryScoresResponse'] = _QUERYSCORESRESPONSE
DESCRIPTOR.message_types_by_name['SetScoresRequest'] = _SETSCORESREQUEST
DESCRIPTOR.message_types_by_name['SetScoresResponse'] = _SETSCORESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'autopilotrpc.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'autopilotrpc.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)

ModifyStatusRequest = _reflection.GeneratedProtocolMessageType('ModifyStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYSTATUSREQUEST,
  '__module__' : 'autopilotrpc.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.ModifyStatusRequest)
  })
_sym_db.RegisterMessage(ModifyStatusRequest)

ModifyStatusResponse = _reflection.GeneratedProtocolMessageType('ModifyStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODIFYSTATUSRESPONSE,
  '__module__' : 'autopilotrpc.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.ModifyStatusResponse)
  })
_sym_db.RegisterMessage(ModifyStatusResponse)

QueryScoresRequest = _reflection.GeneratedProtocolMessageType('QueryScoresRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSCORESREQUEST,
  '__module__' : 'autopilotrpc.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.QueryScoresRequest)
  })
_sym_db.RegisterMessage(QueryScoresRequest)

QueryScoresResponse = _reflection.GeneratedProtocolMessageType('QueryScoresResponse', (_message.Message,), {

  'HeuristicResult' : _reflection.GeneratedProtocolMessageType('HeuristicResult', (_message.Message,), {

    'ScoresEntry' : _reflection.GeneratedProtocolMessageType('ScoresEntry', (_message.Message,), {
      'DESCRIPTOR' : _QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY,
      '__module__' : 'autopilotrpc.autopilot_pb2'
      # @@protoc_insertion_point(class_scope:autopilotrpc.QueryScoresResponse.HeuristicResult.ScoresEntry)
      })
    ,
    'DESCRIPTOR' : _QUERYSCORESRESPONSE_HEURISTICRESULT,
    '__module__' : 'autopilotrpc.autopilot_pb2'
    # @@protoc_insertion_point(class_scope:autopilotrpc.QueryScoresResponse.HeuristicResult)
    })
  ,
  'DESCRIPTOR' : _QUERYSCORESRESPONSE,
  '__module__' : 'autopilotrpc.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.QueryScoresResponse)
  })
_sym_db.RegisterMessage(QueryScoresResponse)
_sym_db.RegisterMessage(QueryScoresResponse.HeuristicResult)
_sym_db.RegisterMessage(QueryScoresResponse.HeuristicResult.ScoresEntry)

SetScoresRequest = _reflection.GeneratedProtocolMessageType('SetScoresRequest', (_message.Message,), {

  'ScoresEntry' : _reflection.GeneratedProtocolMessageType('ScoresEntry', (_message.Message,), {
    'DESCRIPTOR' : _SETSCORESREQUEST_SCORESENTRY,
    '__module__' : 'autopilotrpc.autopilot_pb2'
    # @@protoc_insertion_point(class_scope:autopilotrpc.SetScoresRequest.ScoresEntry)
    })
  ,
  'DESCRIPTOR' : _SETSCORESREQUEST,
  '__module__' : 'autopilotrpc.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.SetScoresRequest)
  })
_sym_db.RegisterMessage(SetScoresRequest)
_sym_db.RegisterMessage(SetScoresRequest.ScoresEntry)

SetScoresResponse = _reflection.GeneratedProtocolMessageType('SetScoresResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETSCORESRESPONSE,
  '__module__' : 'autopilotrpc.autopilot_pb2'
  # @@protoc_insertion_point(class_scope:autopilotrpc.SetScoresResponse)
  })
_sym_db.RegisterMessage(SetScoresResponse)


DESCRIPTOR._options = None
_QUERYSCORESRESPONSE_HEURISTICRESULT_SCORESENTRY._options = None
_SETSCORESREQUEST_SCORESENTRY._options = None

_AUTOPILOT = _descriptor.ServiceDescriptor(
  name='Autopilot',
  full_name='autopilotrpc.Autopilot',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=653,
  serialized_end=982,
  methods=[
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='autopilotrpc.Autopilot.Status',
    index=0,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyStatus',
    full_name='autopilotrpc.Autopilot.ModifyStatus',
    index=1,
    containing_service=None,
    input_type=_MODIFYSTATUSREQUEST,
    output_type=_MODIFYSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryScores',
    full_name='autopilotrpc.Autopilot.QueryScores',
    index=2,
    containing_service=None,
    input_type=_QUERYSCORESREQUEST,
    output_type=_QUERYSCORESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetScores',
    full_name='autopilotrpc.Autopilot.SetScores',
    index=3,
    containing_service=None,
    input_type=_SETSCORESREQUEST,
    output_type=_SETSCORESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTOPILOT)

DESCRIPTOR.services_by_name['Autopilot'] = _AUTOPILOT

# @@protoc_insertion_point(module_scope)
