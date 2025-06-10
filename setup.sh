#!/bin/bash
echo "🔧 Setting up the environment..."

python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f .env ]; then
  cp .env.example .env
  echo "✅ .env created. Add your OpenAI API key!"
fi

echo "✅ Setup complete. Run ./run.sh to start the assistant."
