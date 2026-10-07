import os
import json
from datetime import datetime

MEMORY_FILE = "/storage/emulated/0/ZED-OS/data/memory.json"

def ensure_memory_file():
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "user_name": "User",
                "preferences": [],
                "conversation_history": []
            }, f, ensure_ascii=False, indent=2)

def load_memory():
    ensure_memory_file()
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {
                "user_name": "User",
                "preferences": [],
                "conversation_history": []
            }

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_conversation(user_text, assistant_text):
    data = load_memory()
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user_text,
        "assistant": assistant_text
    }
    data["conversation_history"].append(entry)

    # keep only last 20 conversations
    if len(data["conversation_history"]) > 20:
        data["conversation_history"] = data["conversation_history"][-20:]

    save_memory(data)

def get_recent_context():
    data = load_memory()
    history = data.get("conversation_history", [])
    recent = []
    for item in history[-8:]:
        recent.append(f"User: {item['user']}")
        recent.append(f"Assistant: {item['assistant']}")
    return "\n".join(recent)