import os, datetime, socket, getpass, platform

VERSION = "1.5"
AUTHOR = "invisibleman31coder"
PASSWORD = "zed123"

APPS = {
    "calculator": 'print("ZED Calculator v1.5");\ntry:\n    expr=input("Calc (e.g 1+1): ")\n    print(f"Result: {eval(expr)}")\nexcept Exception as e:\n    print(f"Error: {e}")',
    "clock": 'import datetime; print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))',
    "hacksim": 'import time, random; print("ZED HackSim v1.5\\n"); [print(f"[{i*20}%] Breaching node {random.randint(100,999)}...") or time.sleep(0.4) for i in range(5)]; print("\\nROOT ACCESS GRANTED!")',
    "files": 'import os; print("\\n".join(os.listdir(".")))',
    "notepad": 't=input("Note name: "); c=input("Text: "); open(t,"w").write(c); print(f"Saved {t}")',
    "matrix": 'import time, random; [print("".join([str(random.randint(0,1)) for _ in range(40)])) or time.sleep(0.05) for _ in range(20)]',
    "sysmon": 'import os, platform; print(f"OS: {platform.system()} | Files: {len(os.listdir(\".\"))} | Time: {__import__(\"datetime\").datetime.now()}")'
}

os.system("clear")
print(f"""
███████╗███████╗██████╗       ██████╗ ███████╗
╚══███╔╝██╔════╝██╔══██╗     ██╔═══██╗██╔════╝
  ███╔╝ █████╗  ██║  ██║     ██║   ██║███████╗
 ███╔╝  ██╔══╝  ██║  ██║     ██║   ██║╚════██║
███████╗███████╗██████╔╝     ╚██████╔╝███████║
╚══════╝╚══════╝╚═════╝       ╚═════╝ ╚══════╝
           v{VERSION} - FINAL OFFLINE
           Author: {AUTHOR}
           {len(os.listdir('.'))} files | Ready
""")

if getpass.getpass("Password: ") != PASSWORD:
    print("Access Denied."); exit()
print("Access Granted.\nType help\n")

while True:
    try:
        cmd = input(f"ZED-OS v{VERSION} | {AUTHOR}$ ").strip()
    except KeyboardInterrupt:
        print("\nUse exit"); continue
    if not cmd: continue
    low = cmd.lower()
    if low=="exit": print("Shutting down ZED-OS v1.5"); break
    elif low=="clear": os.system("clear")
    elif low=="version": print(f"ZED-OS v{VERSION} FINAL by {AUTHOR}")
    elif low=="sysinfo":
        try:
            ip=socket.gethostbyname("google.com")
            print(f"DNS: OK ({ip}) | Online")
        except:
            print("DNS: Offline mode (no data needed)")
        print(f"Files: {len(os.listdir('.'))} | {datetime.datetime.now()}")
    elif low=="apps":
        print("ZED Store v1.5:"); [print(f"  - {k}") for k in APPS]
    elif low.startswith("install "):
        a=low.split()[1]
        if a in APPS: open(f"{a}.py","w").write(APPS[a]); print(f"Installed {a}.py (offline)")
        else: print("App not found")
    elif low.startswith("ping "):
        h=low.split()[1]
        try:
            socket.setdefaulttimeout(3)
            socket.gethostbyname(h)
            print(f"{h} -> reachable (DNS OK)")
        except: print(f"{h} -> offline / blocked")
    elif low.startswith("browse "):
        url=cmd.split(" ",1)[1]
        print(f"Trying {url} (3s)...")
        try:
            import urllib.request
            data=urllib.request.urlopen(url, timeout=3).read(500).decode(errors='ignore')
            print(data[:500])
        except Exception as e:
            print(f"Offline: {e}\nTip: No data? Use offline apps.")
    elif low.startswith("write "):
        p=cmd.split(" ",2)
        if len(p)>=3: open(p[1],"w").write(p[2]); print(f"Wrote {p[1]}")
    elif low.startswith("read "):
        try: print(open(cmd[5:].strip()).read())
        except: print("File not found")
    elif low.startswith("run "): os.system(f"python {cmd[4:].strip()}")
    elif low=="ls": os.system("ls -lh")
    elif low=="help": print("version, sysinfo, apps, install <app>, run <file>, ping, browse, ls, write, read, clear, exit")
    else: print(f"Unknown: {cmd}")
