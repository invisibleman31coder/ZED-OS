import os,datetime,socket
print("=== ZED-OS v0.6.1 CLEAN ===")
print("Builder: invisibleman31coder")
while True:
 a=input("ZED-OS | invisibleman31coder:~$ ").strip()
 if not a: continue
 l=a.lower()
 if l=="exit": print("Shutting down..."); break
 elif l=="clear": os.system("clear")
 elif l=="whoami": print("invisibleman31coder")
 elif l=="ip": print("ONLINE ✅")
 elif l=="time": print(datetime.datetime.now())
 elif l=="date": print(datetime.date.today())
 elif l.startswith("calc "):
  try: print(f"= {eval(a[5:])}")
  except: print("error")
 elif l.startswith("ask "): print(f"[ZED-AI] {a[4:]} -> I am ZED-OS v0.6 built by invisibleman31coder!")
 elif l.startswith("note "): open("memory.txt","a").write(a[5:]+"\n"); print("Saved!")
 elif l=="memory":
  try: print(open("memory.txt").read())
  except: print("No memory yet")
 elif l.startswith("ping "):
  h=a.split(" ",1)[1]
  try:
   ip=socket.gethostbyname(h); print(f"Reply from {ip}: 67ms ✅")
  except Exception as e: print(e)
 elif l.startswith("fetch "): print("No data mode - fetch needs internet")
 elif l=="help": print("whoami, ask, calc, time, date, note, memory, ip, ping, clear, exit")
 elif l=="ls": os.system("ls")
 else: print(f"Unknown: {a}")
