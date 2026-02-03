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

    try:

        response=requests.post(
            url=MODEL_URL,
            json=payload,
            headers=HEADERS,
            timeout=30
        )
        print(response)
        response.raise_for_status()
        data = response.json()
        print(data)
        if isinstance(data, list) and "generated_text" in data[0]:
                return data[0]["generated_text"]

        return "🤖 I couldn't generate a response."
    except requests.exceptions.RequestException as e:
        print("HF Error:", e)
        return "⚠️ AI service is busy. Try again later."