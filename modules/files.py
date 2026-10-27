import os
ROOT=os.path.expanduser("~/ZED-OS/vault")
def run():
    os.makedirs(ROOT, exist_ok=True)
    print(f"--- Files Vault: {ROOT} ---")
    while True:
        print("\nFiles:", os.listdir(ROOT) or "(empty)")
        x=input("files $ (view <name> / add <name> / del <name> / exit) > ").strip()
        if x in ["exit","quit",""]: break
        parts=x.split(maxsplit=1)
        cmd=parts[0]
        name=parts[1] if len(parts)>1 else ""
        if cmd=="add" and name:
            txt=input(f"Content for {name}: ")
            open(os.path.join(ROOT,name),"w").write(txt)
            print("Saved")
        elif cmd=="view" and name:
            p=os.path.join(ROOT,name)
            if os.path.exists(p): print(open(p).read())
            else: print("Not found")
        elif cmd=="del" and name:
            try: os.remove(os.path.join(ROOT,name)); print("Deleted")
            except: print("Not found")
