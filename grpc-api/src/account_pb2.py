# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\raccount.proto\x12\x07\x61\x63\x63ount\"I\n\x11\x43reateUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\"5\n\x11\x43reateUserReponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\" \n\x0eGetUserRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\"G\n\x0fGetUserResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\"I\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\"6\n\x12UpdateUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"6\n\x12\x44\x65leteUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xaa\x02\n\x0e\x41\x63\x63ountService\x12\x46\n\nCreateUser\x12\x1a.account.CreateUserRequest\x1a\x1a.account.CreateUserReponse\"\x00\x12>\n\x07GetUser\x12\x17.account.GetUserRequest\x1a\x18.account.GetUserResponse\"\x00\x12G\n\nUpdateUser\x12\x1a.account.UpdateUserRequest\x1a\x1b.account.UpdateUserResponse\"\x00\x12G\n\nDeleteUser\x12\x1a.account.DeleteUserRequest\x1a\x1b.account.DeleteUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'account_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CREATEUSERREQUEST']._serialized_start=26
  _globals['_CREATEUSERREQUEST']._serialized_end=99
  _globals['_CREATEUSERREPONSE']._serialized_start=101
  _globals['_CREATEUSERREPONSE']._serialized_end=154
  _globals['_GETUSERREQUEST']._serialized_start=156
  _globals['_GETUSERREQUEST']._serialized_end=188
  _globals['_GETUSERRESPONSE']._serialized_start=190
  _globals['_GETUSERRESPONSE']._serialized_end=261
  _globals['_UPDATEUSERREQUEST']._serialized_start=263
  _globals['_UPDATEUSERREQUEST']._serialized_end=336
  _globals['_UPDATEUSERRESPONSE']._serialized_start=338
  _globals['_UPDATEUSERRESPONSE']._serialized_end=392
  _globals['_DELETEUSERREQUEST']._serialized_start=394
  _globals['_DELETEUSERREQUEST']._serialized_end=425
  _globals['_DELETEUSERRESPONSE']._serialized_start=427
  _globals['_DELETEUSERRESPONSE']._serialized_end=481
  _globals['_ACCOUNTSERVICE']._serialized_start=484
  _globals['_ACCOUNTSERVICE']._serialized_end=782
# @@protoc_insertion_point(module_scope)