import os
from dotenv import load_dotenv

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HF_TOKEN=os.getenv("HF_TOKEN")
MODEL_URL= (
    "https://api-inference.huggingface.co/models/"
    "mistralai/Mistral-7B-Instruct-v0.2"
)