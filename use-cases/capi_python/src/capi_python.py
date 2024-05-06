#
# Copyright (C) 2024 Intel Corporation.
#
# SPDX-License-Identifier: Apache-2.0
#

from ctypes import *

ovms_so = "/ovms/lib/libovms_shared.so"
ovms_api = CDLL(ovms_so)

print(type(ovms_api))

# INTP = POINTER(c_uint32)
# major = c_uint32(2)
# addr = addressof(major)
# print ("address:", addr, type(addr))

# INTP2 = POINTER(c_uint32)
# minor = c_uint32(2)
# addr2 = addressof(minor)
# print ("address:", addr, type(addr2))

# print(ovms_api.OVMS_ApiVersion(addr, addr2))

class OVMS_ServerSettings(Structure):
    _fields_ = [("GrpcPort", c_uint32),
                ("RestPort", c_uint32)]

class OVMS_ModelsSettings(Structure):
    _fields_ = []

class OVMS_Server(Structure):
    _fields_ = [("OVMS_ServerSettings", OVMS_ServerSettings),
                ("OVMS_ModelsSettings", OVMS_ModelsSettings)]

serverSettings = POINTER(OVMS_ServerSettings)
# print(serverSettings.GrpcPort)
# print(serverSettings.RestPort)
serverSettingsFunc = serverSettings()
grpcPort = c_uint32(9178)
print(serverSettings)
ovms_api.OVMS_ServerSettingsNew(serverSettingsFunc)
ovms_api.OVMS_ServerSettingsSetGrpcPort(byref(serverSettingsFunc), grpcPort)
print(serverSettings)
print(serverSettings.contents)