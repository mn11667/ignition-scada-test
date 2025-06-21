#!/bin/bash

echo "🔁 Staging changes..."
git add .

echo "✅ Committing with timestamp..."
git commit -m "Auto update - $(date '+%Y-%m-%d %H:%M:%S')"

echo "📤 Pushing to GitHub..."
git push

echo "🐳 Building Docker image..."
docker build -t scada-mqtt .

echo "🚀 Docker image built successfully!"

# Optional: Uncomment this line to run the container every time
# docker run -d -p 5000:5000 --name scada-auto scada-mqtt

echo "🎉 All done!"

