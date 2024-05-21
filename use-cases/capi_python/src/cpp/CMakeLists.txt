cmake_minimum_required(VERSION 3.1.0)
project(ovmspybind)
set (CMAKE_CXX_STANDARD 20)

add_subdirectory(pybind11)

pybind11_add_module(ovmspybind "./ovms-pybind.cpp")
include_directories(${CMAKE_SOURCE_DIR}/model_server/src)