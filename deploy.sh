#!/bin/bash

git pull
docker compose --env-file docker.env up --build -d
