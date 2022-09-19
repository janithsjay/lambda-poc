#!/bin/sh
docker build . --build-arg applicationName=shared --no-cache --output type=local,dest=./dist
