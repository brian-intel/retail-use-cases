# Copyright © 2024 Intel Corporation. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

.PHONY: build run down model-names

DOCKER_COMPOSE ?= docker-compose_grpc_python.yml

build:
	docker build -t grpc_python:dev .

model-names:
	@echo
	@echo "For grpc_python, supported MODEL_NAME value: instance-segmentation-security-1040, bit_64, or yolov5s"
	@echo "the default value for MODEL_NAME is instance-segmentation-security-1040 if not provided."
	@echo
	@echo "example: MODEL_NAME=yolov5s make run-grpc_python"
	@echo

run:
	docker compose -f $(DOCKER_COMPOSE) up -d

down:
	docker compose -f $(DOCKER_COMPOSE) down
