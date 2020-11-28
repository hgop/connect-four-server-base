#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Invalid number of arguments"
    echo "./scripts/deploy.sh <NAMESPACE> <ENVIRONMENT>"
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

NAMESPACE="$1"
ENVIRONMENT="$2"

cat "database.yaml.template" \
    | sed "s/{{ENVIRONMENT}}/${ENVIRONMENT}/g" \
    | sed "s/{{DATABASE_USERNAME}}/${DATABASE_USERNAME}/g" \
    | sed "s/{{DATABASE_PASSWORD}}/${DATABASE_PASSWORD}/g" \
    > database.yaml

kubectl --namespace "${NAMESPACE}" apply -f "database.yaml"
