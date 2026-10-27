import os, getpass
try:
    import brain_real as brain
    MODE="DUAL: GROQ online + SMART OFFLINE"
except:
    import brain as brain
    MODE="SMART OFFLINE ONLY"
G="\033[92m";W="\033[0m"
LOGO=f"{G}███████╗███████╗██████╗       ██████╗ ███████╗\n╚══███╔╝██╔════╝██╔══██╗     ██╔═══██╗██╔════╝\n  ███╔╝ █████╗  ██║  ██║     ██║   ██║███████╗\n ███╔╝  ██╔══╝  ██║  ██║     ██║   ██║╚════██║\n███████╗███████╗██████╔╝     ╚██████╔╝███████║\n╚══════╝╚══════╝╚═════╝       ╚═════╝ ╚══════╝{W}"
os.system("clear")
print(LOGO)
print(f"Creator: invisibleman31coder | Brain: {MODE}")
print("Saider AI - OFFLINE SELF-BUILDING ONLINE\n----------------------------------------------------")
getpass.getpass("[LOGIN] Enter Passcode > ")
print("Access granted.\nCommands: files | notes | calculator | hacksim | status | clear | exit\nBuild: 'build anything' - works with NO DATA\n")
def run_module(name):
    try:
        mod=__import__(f"modules.{name}",fromlist=["run"])
        mod.run()
    except Exception as e:
        print(f"Error: {e}")
while True:
    q=input("invisibleman31coder $ ").strip()
    if not q: continue
    l=q.lower()
    if l in ["exit","quit"]: break
    if l=="clear": os.system("clear"); print(LOGO); continue
    if l in ["files","notes","calculator","hacksim"]: run_module(l); continue
    ans=brain.think(q)
    print(f"Saider $ {ans}\n")
