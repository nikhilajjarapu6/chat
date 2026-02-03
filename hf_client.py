import requests
from config import HF_TOKEN,TELEGRAM_TOKEN,MODEL_URL

HEADERS={
    "authorization":f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def ask_llm(prompt:str)->str:
    payload={
        "imputs":prompt,
        "parameters":{
            "max_new_tokens": 200,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    response=requests.post(
        url=MODEL_URL,
        json=payload,
        headers=HEADERS,
        timeout=30
    )
    print(response)