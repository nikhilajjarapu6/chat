from dotenv import load_dotenv
import os

load_dotenv('.env.local')


print("Debug: .env.local loaded successfully")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
print(f"Debug: TELEGRAM_TOKEN = {TELEGRAM_TOKEN}")
print(f"Current Directory: {os.getcwd()}")

import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="HuggingFaceH4/zephyr-7b-beta:featherless-ai",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of india?"
        }
    ],
)

print(completion.choices[0].message)