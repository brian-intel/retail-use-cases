# Copyright © 2024 Intel Corporation. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

.PHONY: build run down model-names

DOCKER_COMPOSE ?= docker-compose_capi_python.yml
PIPELINE_COUNT ?= 1
# supported MODEL_NAME: instance-segmentation-security-1040, bit_64, or yolov5s
MODEL_NAME ?= instance-segmentation-security-1040
RETAIL_USE_CASE_ROOT ?= ../..
RESULTS_DIR ?= ../../results

build:
	docker build -t capi_python:dev .

run:
	PIPELINE_COUNT=$(PIPELINE_COUNT) MODEL_NAME=$(MODEL_NAME) RETAIL_USE_CASE_ROOT="$(RETAIL_USE_CASE_ROOT)" RESULTS_DIR="$(RESULTS_DIR)" docker compose -f $(DOCKER_COMPOSE) up -d

down:
	PIPELINE_COUNT=$(PIPELINE_COUNT) MODEL_NAME=$(MODEL_NAME) RETAIL_USE_CASE_ROOT="$(RETAIL_USE_CASE_ROOT)" RESULTS_DIR="$(RESULTS_DIR)" docker compose -f $(DOCKER_COMPOSE) down

debug:
	docker run -v .:/tmp/capi_python -it capi_python:dev /bin/bash