#!/bin/bash
echo "📤 Pushing to GitHub..."
git add .
git commit -m "${1:-Update}"
git push origin main
