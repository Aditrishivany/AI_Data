ip_address = []
with open("sample.log", "r") as log:
    lines = log.readlines()
for line in lines:
    if "reverse mapping" in line:
        words = line.split()                
        ip_with_brackets = words[0]         
        ip_addr = ip_with_brackets[1:-1]    
        ip_address.append(ip_addr)
import csv
with open("ip.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IP Address"])   
    for addr in ip_address:
        writer.writerow([addr])
with open("ip.txt", "w") as txt:
    for addr in ip_address:
        txt.write(addr + "\n")
print("IP addresses extracted to CSV and TXT successfully.")
