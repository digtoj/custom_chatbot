#!/bin/bash
docker build . -t embedding-app-image:latest -f Dockerfile-embeddingapp

docker compose up

