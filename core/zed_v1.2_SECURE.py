import os
import datetime
import platform
import getpass

VERSION = "1.2"
AUTHOR = "invisibleman31coder"
PASSWORD = "zed123"

os.system("clear")
print(f"""
███████╗███████╗██████╗       ██████╗ ███████╗
╚══███╔╝██╔════╝██╔══██╗     ██╔═══██╗██╔════╝
  ███╔╝ █████╗  ██║  ██║     ██║   ██║███████╗
 ███╔╝  ██╔══╝  ██║  ██║     ██║   ██║╚════██║
███████╗███████╗██████╔╝     ╚██████╔╝███████║
╚══════╝╚══════╝╚═════╝       ╚═════╝ ╚══════╝
           v{VERSION} - SECURE
           Author: {AUTHOR}
""")

attempt = getpass.getpass("Enter password to access ZED-OS: ")
if attempt != PASSWORD:
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
        print(f"""
Version: v{VERSION}
Author: {AUTHOR}
Platform: {platform.system()} {platform.release()}
Python: {platform.python_version()}
Time: {datetime.datetime.now()}
""")
    elif low.startswith("write "):
        parts = cmd.split(" ", 2)
        if len(parts) < 3:
            print("Usage: write <filename> <text>")
        else:
            with open(parts[1], "w") as f:
                f.write(parts[2])
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
        print("Commands: version, sysinfo, ls, write, read, run, clear, exit")
    else:
        print(f"Unknown command: {cmd}")
