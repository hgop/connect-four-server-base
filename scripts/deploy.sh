#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo "Invalid number of arguments"
    echo "./scripts/deploy.sh <NAMESPACE> <SUBDOMAIN> <ENVIRONMENT> <IMAGE_TAG>"
    exit 1
fi

if [[ -z "${DATABASE_USERNAME}" ]]; then
    echo "Environment variable DATABASE_USERNAME not set"
    exit 1
fi

if [[ -z "${DATABASE_PASSWORD}" ]]; then
    echo "Environment variable DATABASE_PASSWORD not set"
    exit 1
fi

if [[ -z "${SECRET_KEY}" ]]; then
    echo "Environment variable SECRET_KEY not set"
    exit 1
fi

NAMESPACE="$1"
SUBDOMAIN="$2"
ENVIRONMENT="$3"
IMAGE_TAG="$4"

cat "k8s.yaml.template" \
    | sed "s/{{SUBDOMAIN}}/${SUBDOMAIN}/g" \
    | sed "s/{{ENVIRONMENT}}/${ENVIRONMENT}/g" \
    | sed "s/{{IMAGE_TAG}}/${IMAGE_TAG}/g" \
    | sed "s/{{DATABASE_USERNAME}}/${DATABASE_USERNAME}/g" \
    | sed "s/{{DATABASE_PASSWORD}}/${DATABASE_PASSWORD}/g" \
    | sed "s/{{SECRET_KEY}}/${SECRET_KEY}/g" \
    > k8s.yaml

kubectl --namespace "${NAMESPACE}" apply -f "k8s.yaml"
