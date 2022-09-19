#!/bin/sh
docker build . --no-cache --output type=local,dest=./dist
