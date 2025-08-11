#!/bin/bash
NAME=sk035
IMAGE_NAME="posts-get"
VERSION="1.2"
CPU_PLATFORM=amd64
#CPU_PLATFORM=arm64

# Docker 이미지 빌드
docker build \
  --tag ${NAME}-${IMAGE_NAME}.${CPU_PLATFORM}:${VERSION} \
  --file Dockerfile \
  --platform linux/${CPU_PLATFORM} \
  ${IS_CACHE} .
