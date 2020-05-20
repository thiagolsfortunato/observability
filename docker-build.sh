#!/usr/bin/env bash

SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

for dir in $(ls | grep service) ; do
  cd $dir
  DIR_NAME=$(basename "$PWD")
  IMAGE_NAME="gcr.io/observability-277802/${DIR_NAME}:v1"
  DOCKER_BUILDKIT=1 docker build -t "${IMAGE_NAME}" .
  docker push "${IMAGE_NAME}"
  cd ..
done
