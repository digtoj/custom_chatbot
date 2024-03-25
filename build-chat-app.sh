#!/bin/bash
docker build . -t chatbot-app-image:latest -f Dockerfile-chatapp

docker compose up