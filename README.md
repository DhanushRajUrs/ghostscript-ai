# GhostScript AI 👻

A spooky, beginner-friendly coding companion powered by local AI.
Ask about terminal commands or coding concepts and receive an eerie
opening, a useful explanation, and a practical example.

## Built with
- Python
- Streamlit
- Ollama
- Gemma 3:1B

## Run locally

Install Python and Ollama. Download the model:

    ollama pull gemma3:1b

Create and activate a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install streamlit requests

Start the app:

    streamlit run app.py

Open the local URL displayed in the terminal.

## Why open innovation matters

GhostScript AI uses an open-weight model through local inference.
After installation and model download, it can generate responses
without sending prompts to a hosted AI API. This gives users greater
control over their inputs and lets developers experiment with local AI.

## Project status
Working local prototype for Hacktoberfest Week 4: Ghost in the Machine.
