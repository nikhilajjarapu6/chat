from huggingface_hub import InferenceClient
from config import HF_TOKEN, MODEL_ID

# Create client once (like a singleton bean)
client = InferenceClient(
    token=HF_TOKEN
)

def ask_llm(prompt: str) -> str:
    """General chat"""
    return _chat(prompt, max_tokens=400, temperature=0.7)

def ask_short(prompt: str) -> str:
    """Short answers for Telegram"""
    return _chat(
        f"Answer briefly in 2–3 sentences.\n{prompt}",
        max_tokens=80,
        temperature=0.5
    )


def ask_code(prompt: str) -> str:
    """Code-focused explanation"""
    return _chat(
        f"Explain with a short code example.\n{prompt}",
        max_tokens=300,
        temperature=0.3
    )


def ask_json(prompt: str) -> str:
    """Strict JSON output"""
    return _chat(
        f"Respond ONLY in valid JSON. No explanation.\n{prompt}",
        max_tokens=200,
        temperature=0.2
    )


def summarize(text: str) -> str:
    """Summarize text"""
    return _chat(
        f"Summarize the following text:\n{text}",
        max_tokens=150,
        temperature=0.4
    )

def _chat(prompt: str, max_tokens: int, temperature: float) -> str:
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct:novita",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Provide a complete answer. "
                        "If the explanation is long, keep it end cleanly.\n\n"
                        f"{prompt}"
                    )
                }
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print("HF Error:", repr(e))
        return "⚠️ AI service is busy. Try again later."
