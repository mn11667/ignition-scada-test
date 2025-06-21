#!/bin/bash

echo "🔁 Watching for changes in ./sensor-api..."
while true; do
  fswatch -r ./sensor-api | while read change; do
    echo "🔧 Change detected in $change"
    echo "📦 Rebuilding Docker container: sensor-api"
    docker-compose build sensor-api

    echo "🚀 Restarting container..."
    docker-compose up -d sensor-api

    echo "✅ sensor-api container updated!"
    sleep 1  # avoid duplicate events
  done
done
