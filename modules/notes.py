import os, datetime
FILE=os.path.expanduser("~/ZED-OS/vault/notes.txt")
def run():
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    print(f"--- Notes Vault: {FILE} ---")
    print("Commands: list | clear | exit")
    print("Just type a line to save it.")
    while True:
        x=input("notes $ ").strip()
        if not x: continue
        if x in ["exit","quit"]: break
        if x=="list":
            if os.path.exists(FILE): print(open(FILE).read() or "(empty)")
            else: print("(empty)")
            continue
        if x=="clear":
            open(FILE,"w").write(""); print("Cleared"); continue
        with open(FILE,"a") as f:
            f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}] {x}\n")
        print("Saved.")
