import os
import datetime
import platform

VERSION = "1.1"
AUTHOR = "invisibleman31coder"

os.system("clear")
print(f"""
███████╗███████╗██████╗       ██████╗ ███████╗
╚══███╔╝██╔════╝██╔══██╗     ██╔═══██╗██╔════╝
  ███╔╝ █████╗  ██║  ██║     ██║   ██║███████╗
 ███╔╝  ██╔══╝  ██║  ██║     ██║   ██║╚════██║
███████╗███████╗██████╔╝     ╚██████╔╝███████║
╚══════╝╚══════╝╚═════╝       ╚═════╝ ╚══════╝
           v{VERSION}
           Author: {AUTHOR}
""")

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
    elif low == "whoami":
        print(AUTHOR)
    elif low == "time":
        print(datetime.datetime.now())
    elif low == "sysinfo":
        print(f"""
ZED-OS System Info:
  Version: v{VERSION}
  Author: {AUTHOR}
  Platform: {platform.system()} {platform.release()}
  Python: {platform.python_version()}
  Time: {datetime.datetime.now()}
  Directory: {os.getcwd()}
  Files: {len(os.listdir('.'))} files in core
""")
    elif low.startswith("calc "):
        try:
            print(f"= {eval(cmd[5:])}")
        except:
            print("Calculation error")
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
    elif low.startswith("rm "):
        try:
            os.remove(cmd[3:].strip())
            print("Deleted")
        except:
            print("Delete failed")
    elif low.startswith("run "):
        os.system(f"python {cmd[4:].strip()}")
    elif low == "ls":
        os.system("ls -lh")
    elif low == "help":
        print("""
Commands:
  version, whoami, time, sysinfo, clear, exit
  calc <expression>
  ls, write, read, rm, run
""")
    else:
        print(f"Unknown command: {cmd}")
