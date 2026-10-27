import random, time, os
def run():
    G="\033[92m"; R="\033[91m"; W="\033[0m"
    print(f"{G}--- HackSim v2.3 [SIMULATION ONLY] ---{W}")
    print("Targets: vault.local | 192.168.1.7 | saider-node | ghost-server")
    print("Commands: scan <target> | brute | trace | exploit | exit")
    print(f"{R}Warning: No real network touched. Lab only.{W}\n")
    while True:
        x=input("hacksim $ ").strip()
        if not x: continue
        l=x.lower()
        if l in ["exit","quit",""]: break
        if l.startswith("scan"):
            target = x.split()[-1] if len(x.split())>1 else "vault.local"
            print(f"[+] Scanning {target}...")
            time.sleep(0.8)
            print(f"  -> 22/tcp open ssh")
            print(f"  -> 80/tcp open http")
            print(f"  -> 443/tcp filtered https")
            print(f"  -> OS: ZED-OS Linux")
        elif "brute" in l:
            print("[+] Brute force simulation...")
            for i in range(1,6):
                time.sleep(0.3)
                print(f"  trying pass {random.randint(1000,9999)}... fail")
            print("[!] Access denied. Saider blocked you. Try again coder.")
        elif "trace" in l:
            print("Tracing route...")
            time.sleep(0.5)
            print("10.0.0.1 -> 192.168.1.1 -> saider-node [SECURE]")
        elif "exploit" in l:
            print("[!] Exploit simulated: Vault opened! File: flag.txt (simulation)")
        else:
            print("Unknown. Commands: scan, brute, trace, exploit, exit")

