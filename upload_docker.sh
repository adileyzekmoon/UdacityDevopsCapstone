#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=adileyzekmoon/udacitycapstone

# Step 2:  
# Authenticate & tag
docker login --username adileyzekmoon &&\
    docker image tag udacitycapstone $dockerpath
echo "Docker ID and Image: $dockerpath"

# Step 3:
# Push image to a docker repository
docker image push $dockerpath
