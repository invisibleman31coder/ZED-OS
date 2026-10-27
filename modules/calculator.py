def run():
    print("--- Calculator (offline) ---")
    print("Type expression or 'exit'")
    while True:
        x=input("calc $ ").strip()
        if x in ["exit","quit",""]: break
        try: print(f"= {eval(x, {'__builtins__':{}})}")
        except Exception as e: print(f"Error: {e}")
