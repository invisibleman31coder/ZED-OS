import os
import datetime
import platform
import getpass

VERSION = "1.3"
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
           v{VERSION} - APP STORE
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
        print(f"Version: v{VERSION} | Files: {len(os.listdir('.'))} | Time: {datetime.datetime.now()}")
    elif low == "apps":
        print("Available apps in ZED Store:")
        for name in APPS.keys():
            print(f"  - {name}")
        print("\nUse: install <appname>")
    elif low.startswith("install "):
        app = low.split(" ")[1]
        if app in APPS:
            with open(f"{app}.py", "w") as f:
                f.write(APPS[app])
            print(f"Installed {app}.py - run with: run {app}.py")
        else:
            print("App not found. Use 'apps' to list.")
    elif low.startswith("write "):
        parts = cmd.split(" ", 2)
        if len(parts) >= 3:
            open(parts[1], "w").write(parts[2])
            print(f"Wrote to {parts[1]}")
    elif low.startswith("read "):
        try:
            print(open(cmd[5:].strip()).read())
        except:
            print("File not found")
    elif low.startswith("run "):
        os.system(f"python {cmd[4:].strip()}")
    elif low == "ls":
        os.system("ls -lh")
    elif low == "help":
        print("Commands: version, sysinfo, apps, install, ls, write, read, run, clear, exit")
    else:
        print(f"Unknown: {cmd}")
