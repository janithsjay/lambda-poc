# syntax = docker/dockerfile:experimental

# ------------------------------------------------------------------------------
# BUILD STAGE
# ------------------------------------------------------------------------------

FROM python:3.9-alpine as build

ARG applicationName
ARG ARTIFACT_VERSION=0.1

WORKDIR /workspace/
COPY . .

WORKDIR /workspace/$applicationName

RUN pip install -r requirements.txt -t src
RUN apk add --no-cache zip
RUN zip -r ./$applicationName.zip ./*

FROM scratch AS export-artifact
ARG applicationName
COPY --from=build /workspace/$applicationName/$applicationName.zip .
