import os, datetime, platform, getpass, socket, subprocess

VERSION = "1.4"
AUTHOR = "invisibleman31coder"
PASSWORD = "zed123"

APPS = {
    "calculator": 'print("ZED Calculator"); a=int(input("First: ")); b=int(input("Second: ")); print(f"Result: {a+b}")',
    "clock": 'import datetime; print(datetime.datetime.now())',
    "hacksim": 'import time, random; print("Hacking..."); [print(f"Accessing node {i}... {random.randint(0,100)}%") or time.sleep(0.3) for i in range(5)]; print("Access Granted!")'
}

os.system("clear")
print(f"""
███████╗███████╗██████╗       ██████╗ ███████╗
╚══███╔╝██╔════╝██╔══██╗     ██╔═══██╗██╔════╝
  ███╔╝ █████╗  ██║  ██║     ██║   ██║███████╗
 ███╔╝  ██╔══╝  ██║  ██║     ██║   ██║╚════██║
███████╗███████╗██████╔╝     ╚██████╔╝███████║
╚══════╝╚══════╝╚═════╝       ╚═════╝ ╚══════╝
           v{VERSION} - NETWORK
           Author: {AUTHOR}
""")

if getpass.getpass("Password: ") != PASSWORD:
    print("Access Denied.")
    exit()
print("Access Granted.\n")

while True:
    cmd = input(f"ZED-OS v{VERSION} | {AUTHOR}$ ").strip()
    if not cmd:
        continue
    low = cmd.lower()

    if low == "exit":
        print("Shutting down ZED-OS.")
        break
    elif low == "clear":
        os.system("clear")
    elif low == "version":
        print(f"ZED-OS v{VERSION}")
    elif low == "sysinfo":
        try:
            ip = socket.gethostbyname(socket.gethostname())
        except:
            ip = "Offline"
        print(f"Version: v{VERSION} | IP: {ip} | Files: {len(os.listdir('.'))}")
    elif low == "apps":
        print("Store:")
        for n in APPS: print(f"  - {n}")
    elif low.startswith("install "):
        app = low.split()[1]
        if app in APPS:
            open(f"{app}.py","w").write(APPS[app])
            print(f"Installed {app}.py")
        else:
            print("App not found")
    elif low.startswith("ping "):
        host = low.split()[1]
        print(f"Pinging {host}...")
        os.system(f"ping -c 3 {host}")
    elif low.startswith("browse "):
        url = cmd.split(" ",1)[1]
        print(f"Fetching {url}...")
        os.system(f"curl -I {url} 2>&1 | head -20")
    elif low.startswith("write "):
        p = cmd.split(" ",2)
        if len(p)>=3:
            open(p[1],"w").write(p[2])
            print(f"Wrote {p[1]}")
    elif low.startswith("read "):
        try: print(open(cmd[5:].strip()).read())
        except: print("Not found")
    elif low.startswith("run "):
        os.system(f"python {cmd[4:].strip()}")
    elif low == "ls":
        os.system("ls -lh")
    elif low == "help":
        print("Commands: version, sysinfo, apps, install, ping, browse, ls, write, read, run, clear, exit")
    else:
        print(f"Unknown: {cmd}")
