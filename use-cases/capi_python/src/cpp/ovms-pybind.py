import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './')

import ovmspybind

serverSet = ovmspybind.ServerSettingsNew()
print(serverSet.grpcPort)
serverSet.grpcPort = 8080
print(serverSet.grpcPort)

modelSet = ovmspybind.ModelsSettingsImpl
print(modelSet.configPath)
modelSet.configPath = "../../res/yolov8/config-yolov8.json"
print(modelSet.configPath)

status = ovmspybind.StatusCode.OK
print(status)
print(status.value)