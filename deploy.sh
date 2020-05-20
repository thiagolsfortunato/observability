#!/usr/bin/env bash

for dir in $(ls | grep service) ; do
  cd $dir
  DIR_NAME=$(basename "$PWD")
  cat "${DIR_NAME}.yaml" | sed "s/{{PROJECT_ID}}/${PROJECT_ID}/g" | kubectl apply -f -
  cd ..
done
