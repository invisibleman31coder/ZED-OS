import os,datetime,socket
print("=== ZED-OS v0.8 WRITER ===")
print("Builder: invisibleman31coder")
while True:
 a=input("ZED-OS | invisibleman31coder:~$ ").strip()
 if not a: continue
 l=a.lower()
 if l=="exit": break
 elif l=="clear": os.system("clear")
 elif l=="whoami": print("invisibleman31coder")
 elif l=="time": print(datetime.datetime.now())
 elif l.startswith("calc "):
  try: print(f"= {eval(a[5:])}")
  except: print("error")
 elif l.startswith("ask "): print(f"[ZED-AI] {a[4:]}")
 elif l.startswith("note "): open("memory.txt","a").write(a[5:]+"\n"); print("Saved!")
 elif l=="memory":
  try: print(open("memory.txt").read())
  except: print("Empty")
 elif l=="ls": os.system("ls -lh")
 elif l=="tree": os.system("find . -type f | head -20")
 elif l.startswith("mkfile "):
  f=a[7:]; open(f,"w").write(""); print(f"Created {f} ✅")
 elif l.startswith("write "):
  # write filename text
  parts=a.split(" ",2)
  if len(parts)<3: print("Usage: write filename your text")
  else: open(parts[1],"w").write(parts[2]); print(f"Wrote to {parts[1]} ✅")
 elif l.startswith("read "):
  try: print(open(a[5:]).read())
  except: print("File not found")
 elif l.startswith("rm "):
  try: os.remove(a[3:]); print("Deleted ✅")
  except: print("Error")
 elif l=="ip": print("ONLINE ✅")
 elif l.startswith("ping "):
  try: print(f"Reply from {socket.gethostbyname(a[5:])} ✅")
  except: print("Fail")
 elif l=="help": print("whoami, ask, calc, note, memory, ls, tree, mkfile, write, read, rm, ip, ping, clear, exit")
 else: print(f"Unknown: {a}")
