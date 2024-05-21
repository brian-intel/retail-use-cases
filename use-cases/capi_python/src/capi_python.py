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
class OVMS_Status(Structure):
    _fields_ = []

class OVMS_ServerSettings(Structure):
    _fields_ = [("grpcPort", c_uint32)]

class OVMS_ModelsSettings(Structure):
    _fields_ = [("configPath", c_char_p)]

class OVMS_Server(Structure):
    _fields_ = []

serverSettings = OVMS_ServerSettings(9180)
print(serverSettings.grpcPort)

status = ovms_api.OVMS_ServerSettingsNew(byref(pointer(serverSettings)))
print("new server settings")
print(serverSettings.grpcPort)

# status2 = ovms_api.OVMS_ServerSettingsSetGrpcPort(pointer(serverSettings), 8080)
# print("change grpc port")
# print(serverSettings.grpcPort)
# print(serverSettings.restPort)
# print(status)
# print(status2)

path = c_char_p(b"/tmp/capi_python/res/yolov8/config-yolov8.json")
modelSettings = OVMS_ModelsSettings(path)
print(modelSettings.configPath)

status3 = ovms_api.OVMS_ModelsSettingsNew(byref(pointer(modelSettings)))
print("new model settings")
print(modelSettings.configPath)

server = OVMS_Server()
print(server)
print("start server")
status4 = ovms_api.OVMS_ServerNew(byref(pointer(server)))
print(status4)
ovms_api.OVMS_ServerDelete(byref(server))
# serverStatus = ovms_api.OVMS_ServerStartFromConfigurationFile(byref(server), byref(serverSettings), byref(modelSettings))
# print(serverStatus)
# isLive = False
# ovms_api.OVMS_ServerLive(byref(server), isLive)
# print(isLive)

# class OVMS_ServableMetadata(Structure):
#     _fields_ = [("name", c_char_p),
#                 ("version", c_int64)]

# metadata = OVMS_ServableMetadata(b"",0)
# ovms_api.OVMS_GetServableMetadata(byref(server), b"bit_64", 1, byref(pointer(metadata)))