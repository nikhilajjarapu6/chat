import os
from pathlib import Path
from dotenv import load_dotenv

# This finds the folder where config.py lives
BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env.local"

# Load the file explicitly
load_dotenv(dotenv_path=env_path)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")

# This is a helpful 'fail-fast' check
if not TELEGRAM_TOKEN:
    print(f"❌ ERROR: TELEGRAM_TOKEN not found in {env_path}")
else:
    print("✅ Environment variables loaded successfully")


MODEL_ID = "zephyr-7b-beta"

MODEL_URL = (
    f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
)
