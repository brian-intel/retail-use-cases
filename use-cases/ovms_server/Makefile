# Copyright © 2023 Intel Corporation. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

.PHONY: build run down

DOCKER_COMPOSE ?= docker-compose_ovms_server.yml

build:
	HTTPS_PROXY=${HTTPS_PROXY} HTTP_PROXY=${HTTP_PROXY} docker build -t ovms-server:dev .

run:
	docker compose -f $(DOCKER_COMPOSE) up -d

down:
	docker compose -f $(DOCKER_COMPOSE) down
