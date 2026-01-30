import os
servers = ["8.8.8.8", "1.1.1.1", "google.com"] 
results = []
for server in servers:
    cmd = f"ping -n 1 {server}" if os.name == "nt" else f"ping -c 1 {server}"
    response = os.system(cmd)
    status = "Reachable" if response == 0 else "Not Reachable"
    results.append(f"{server}: {status}")
    print(server, "-", status)
with open("outputs.txt", "a") as out:
    out.write("=== Ping Server Report ===\n")
    for r in results:
        out.write(r + "\n")
    out.write("\n")
