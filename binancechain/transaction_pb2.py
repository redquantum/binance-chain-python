# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='transaction',
  syntax='proto3',
  serialized_pb=_b('\n\x11transaction.proto\x12\x0btransaction\"U\n\x05StdTx\x12\x0c\n\x04msgs\x18\x01 \x03(\x0c\x12\x12\n\nsignatures\x18\x02 \x03(\x0c\x12\x0c\n\x04memo\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\"\\\n\x0cStdSignature\x12\x0f\n\x07pub_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x03 \x01(\x03\x12\x10\n\x08sequence\x18\x04 \x01(\x03\"\x05\n\x03Msg\"\x8d\x01\n\x08NewOrder\x12\x0e\n\x06sender\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x11\n\tordertype\x18\x04 \x01(\x03\x12\x0c\n\x04side\x18\x05 \x01(\x03\x12\r\n\x05price\x18\x06 \x01(\x03\x12\x10\n\x08quantity\x18\x07 \x01(\x03\x12\x13\n\x0btimeinforce\x18\x08 \x01(\x03\"<\n\x0b\x43\x61ncelOrder\x12\x0e\n\x06sender\x18\x01 \x01(\x0c\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\r\n\x05refid\x18\x03 \x01(\t\"P\n\x04Send\x12\"\n\x06inputs\x18\x01 \x03(\x0b\x32\x12.transaction.Input\x12$\n\x07outputs\x18\x02 \x03(\x0b\x32\x13.transaction.Output\"&\n\x05Token\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\";\n\x05Input\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12!\n\x05\x63oins\x18\x02 \x03(\x0b\x32\x12.transaction.Token\"<\n\x06Output\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12!\n\x05\x63oins\x18\x02 \x03(\x0b\x32\x12.transaction.Token\"6\n\x06\x46reeze\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x0c\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"8\n\x08Unfreeze\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x0c\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"S\n\x04Vote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x03\x12\r\n\x05voter\x18\x02 \x01(\x0c\x12\'\n\x06option\x18\x03 \x01(\x0e\x32\x17.transaction.VoteOption*G\n\nVoteOption\x12\x0b\n\x07Unknown\x10\x00\x12\x07\n\x03Yes\x10\x01\x12\x0b\n\x07\x41\x62stain\x10\x02\x12\x06\n\x02No\x10\x03\x12\x0e\n\nNoWithVeto\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_VOTEOPTION = _descriptor.EnumDescriptor(
  name='VoteOption',
  full_name='transaction.VoteOption',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Yes', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Abstain', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='No', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NoWithVeto', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=872,
  serialized_end=943,
)
_sym_db.RegisterEnumDescriptor(_VOTEOPTION)

VoteOption = enum_type_wrapper.EnumTypeWrapper(_VOTEOPTION)
Unknown = 0
Yes = 1
Abstain = 2
No = 3
NoWithVeto = 4



_STDTX = _descriptor.Descriptor(
  name='StdTx',
  full_name='transaction.StdTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgs', full_name='transaction.StdTx.msgs', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='transaction.StdTx.signatures', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memo', full_name='transaction.StdTx.memo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='transaction.StdTx.source', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='transaction.StdTx.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=119,
)


_STDSIGNATURE = _descriptor.Descriptor(
  name='StdSignature',
  full_name='transaction.StdSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='transaction.StdSignature.pub_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='transaction.StdSignature.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_number', full_name='transaction.StdSignature.account_number', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='transaction.StdSignature.sequence', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=213,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='transaction.Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=220,
)


_NEWORDER = _descriptor.Descriptor(
  name='NewOrder',
  full_name='transaction.NewOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='transaction.NewOrder.sender', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='transaction.NewOrder.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='transaction.NewOrder.symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ordertype', full_name='transaction.NewOrder.ordertype', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='side', full_name='transaction.NewOrder.side', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='transaction.NewOrder.price', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='transaction.NewOrder.quantity', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeinforce', full_name='transaction.NewOrder.timeinforce', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=364,
)


_CANCELORDER = _descriptor.Descriptor(
  name='CancelOrder',
  full_name='transaction.CancelOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='transaction.CancelOrder.sender', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='transaction.CancelOrder.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refid', full_name='transaction.CancelOrder.refid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=426,
)


_SEND = _descriptor.Descriptor(
  name='Send',
  full_name='transaction.Send',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='transaction.Send.inputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='transaction.Send.outputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=508,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='transaction.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='denom', full_name='transaction.Token.denom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transaction.Token.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=510,
  serialized_end=548,
)


_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='transaction.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='transaction.Input.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coins', full_name='transaction.Input.coins', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=609,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='transaction.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='transaction.Output.address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coins', full_name='transaction.Output.coins', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=671,
)


_FREEZE = _descriptor.Descriptor(
  name='Freeze',
  full_name='transaction.Freeze',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='transaction.Freeze.from', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='transaction.Freeze.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transaction.Freeze.amount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=673,
  serialized_end=727,
)


_UNFREEZE = _descriptor.Descriptor(
  name='Unfreeze',
  full_name='transaction.Unfreeze',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='transaction.Unfreeze.from', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='transaction.Unfreeze.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transaction.Unfreeze.amount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=785,
)


_VOTE = _descriptor.Descriptor(
  name='Vote',
  full_name='transaction.Vote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='transaction.Vote.proposal_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voter', full_name='transaction.Vote.voter', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='option', full_name='transaction.Vote.option', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=787,
  serialized_end=870,
)

_SEND.fields_by_name['inputs'].message_type = _INPUT
_SEND.fields_by_name['outputs'].message_type = _OUTPUT
_INPUT.fields_by_name['coins'].message_type = _TOKEN
_OUTPUT.fields_by_name['coins'].message_type = _TOKEN
_VOTE.fields_by_name['option'].enum_type = _VOTEOPTION
DESCRIPTOR.message_types_by_name['StdTx'] = _STDTX
DESCRIPTOR.message_types_by_name['StdSignature'] = _STDSIGNATURE
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['NewOrder'] = _NEWORDER
DESCRIPTOR.message_types_by_name['CancelOrder'] = _CANCELORDER
DESCRIPTOR.message_types_by_name['Send'] = _SEND
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['Freeze'] = _FREEZE
DESCRIPTOR.message_types_by_name['Unfreeze'] = _UNFREEZE
DESCRIPTOR.message_types_by_name['Vote'] = _VOTE
DESCRIPTOR.enum_types_by_name['VoteOption'] = _VOTEOPTION

StdTx = _reflection.GeneratedProtocolMessageType('StdTx', (_message.Message,), dict(
  DESCRIPTOR = _STDTX,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.StdTx)
  ))
_sym_db.RegisterMessage(StdTx)

StdSignature = _reflection.GeneratedProtocolMessageType('StdSignature', (_message.Message,), dict(
  DESCRIPTOR = _STDSIGNATURE,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.StdSignature)
  ))
_sym_db.RegisterMessage(StdSignature)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), dict(
  DESCRIPTOR = _MSG,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Msg)
  ))
_sym_db.RegisterMessage(Msg)

NewOrder = _reflection.GeneratedProtocolMessageType('NewOrder', (_message.Message,), dict(
  DESCRIPTOR = _NEWORDER,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.NewOrder)
  ))
_sym_db.RegisterMessage(NewOrder)

CancelOrder = _reflection.GeneratedProtocolMessageType('CancelOrder', (_message.Message,), dict(
  DESCRIPTOR = _CANCELORDER,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.CancelOrder)
  ))
_sym_db.RegisterMessage(CancelOrder)

Send = _reflection.GeneratedProtocolMessageType('Send', (_message.Message,), dict(
  DESCRIPTOR = _SEND,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Send)
  ))
_sym_db.RegisterMessage(Send)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), dict(
  DESCRIPTOR = _TOKEN,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Token)
  ))
_sym_db.RegisterMessage(Token)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), dict(
  DESCRIPTOR = _INPUT,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Input)
  ))
_sym_db.RegisterMessage(Input)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUT,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Output)
  ))
_sym_db.RegisterMessage(Output)

Freeze = _reflection.GeneratedProtocolMessageType('Freeze', (_message.Message,), dict(
  DESCRIPTOR = _FREEZE,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Freeze)
  ))
_sym_db.RegisterMessage(Freeze)

Unfreeze = _reflection.GeneratedProtocolMessageType('Unfreeze', (_message.Message,), dict(
  DESCRIPTOR = _UNFREEZE,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Unfreeze)
  ))
_sym_db.RegisterMessage(Unfreeze)

Vote = _reflection.GeneratedProtocolMessageType('Vote', (_message.Message,), dict(
  DESCRIPTOR = _VOTE,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.Vote)
  ))
_sym_db.RegisterMessage(Vote)


# @@protoc_insertion_point(module_scope)