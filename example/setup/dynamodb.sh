#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

deletetables=false

while getopts :d flag
do
    case "${flag}" in
        d) deletetables=true;;
    esac
done

if "$deletetables"
then
    echo "Deleting tables..."
    aws dynamodb delete-table \
        --endpoint-url http://localhost:8000 \
        --table-name recurring-events
    
    aws dynamodb delete-table \
        --endpoint-url http://localhost:8000 \
        --table-name event-instance

    echo "Delete complete. Goodbye!"
    exit
fi

echo "Creating 'recurring-event' table..."
aws dynamodb create-table \
    --table-name recurring-events \
    --attribute-definitions \
        AttributeName=guid,AttributeType=S \
    --key-schema \
        AttributeName=guid,KeyType=HASH \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url http://localhost:8000

for FILE in ${BASEDIR}/dynamodb-items/*.json; do
    echo "Loading item from file '${FILE}'..."
    aws dynamodb put-item \
        --endpoint-url http://localhost:8000 \
        --table-name recurring-events \
        --item "file://${FILE}"
done

echo "Creating 'event-instance' table..."
aws dynamodb create-table \
    --table-name event-instance \
    --attribute-definitions \
        AttributeName=guid,AttributeType=S \
        AttributeName=notificationDate,AttributeType=S \
    --key-schema \
        AttributeName=guid,KeyType=HASH \
        AttributeName=notificationDate,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url http://localhost:8000
