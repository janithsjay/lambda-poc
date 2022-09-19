# syntax = docker/dockerfile:experimental

# ------------------------------------------------------------------------------
# BUILD STAGE
# ------------------------------------------------------------------------------

FROM python:3.9-alpine as build

ARG ARTIFACT_VERSION=0.1

WORKDIR /workspace

COPY . .

RUN pip install -r requirements.txt -t src
RUN apk add --no-cache zip
WORKDIR /workspace/src
RUN zip -r ./python.zip ./*

FROM scratch AS export-artifact
COPY --from=build /workspace/src/python.zip .
