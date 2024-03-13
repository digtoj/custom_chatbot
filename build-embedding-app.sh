#!/bin/bash
docker build . -t embedding-backend:latest -f Dockerfile-backend

docker build . -t embedding-app-image:latest -f Dockerfile-embeddingapp
