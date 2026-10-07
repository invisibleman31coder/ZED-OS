from memory import add_conversation, get_recent_context
import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY","").strip()
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL","meta-llama/llama-3.1-8b-instruct:free")

def generate_response(prompt: str) -> str:
    prompt = prompt.strip()
    if not prompt:
        return "I did not hear anything."
    recent_context = get_recent_context()

    # OFFLINE mode (no key needed)
    if not OPENROUTER_API_KEY:
        low = prompt.lower()
        if "who am i" in low:
            ans = "You are Sandile Maphumulo, 24, from uMkomass Durban, Unisa, creator of ZED GHOST."
        elif "hello" in low or "hi" in low:
            ans = "Hello creator Sandile. ZED-OS phone ready, offline mode clean."
        else:
            ans = f"ZED hears: {prompt} (offline mode)"
        add_conversation(prompt, ans)
        return ans

    # ONLINE super intelligence
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://localhost",
            "X-Title": "ZED-OS"
        }
        payload = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "system", "content": "You are ZED-OS, calm, intelligent, human-like, remember context."},
                {"role": "user", "content": f"Context:\n{recent_context}\n\nUser: {prompt}"}
            ]
        }
        r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=20)
        r.raise_for_status()
        ans = r.json()['choices'][0]['message']['content']
        add_conversation(prompt, ans)
        return ans
    except Exception as e:
        return f"Offline fallback: {e}"

if __name__ == "__main__":
    print("ZED-OS PHONE READY - type to talk (no mic needed)")
    while True:
        q = input("\nYou: ")
        a = generate_response(q)
        print(f"ZED: {a}")