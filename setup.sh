#!/bin/bash

echo "🔧 Setting up Daddy Assistant environment..."

# Create virtual environment
python3 -m venv env
echo "✅ Virtual environment created."

# Activate the virtual environment
source env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
echo "✅ Required Python packages installed."

# Create .env if it doesn't exist
if [ ! -f .env ]; then
  cp .env.example .env
  echo "📄 .env file created from .env.example. Don't forget to add your OpenAI API key!"
else
  echo "📄 .env file already exists."
fi

echo "🎉 Setup complete. Run the assistant with: python main.py"
