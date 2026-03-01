'''
Regular Expression Challenge (IP Address Extractor)
Write a Python function that uses a regular expression to extract all unique IPv4 addresses
from the log file. Some log messages include IP addresses (e.g., “Ping to server
192.168.1.100 succeeded”). Return a list of unique IP addresses found.
Challenge: Ensure your regex correctly matches typical IPv4 formats and does not capture
invalid patterns.
'''

import os,sys,re
log_file=input("Enter file name:")
if not os.path.exists(log_file):
    print("file not found")
    sys.exit()
unique_ips=[]
with open(log_file,'r') as file:
    for line in file:
        m=re.search(r"\b\d+\.\d+\.\d+\.\d\b",line)
        if m:
            if m.group() not in unique_ips:
                unique_ips.append(m.group())
print("All uniqu IPv4 Addresses Found:")
print(*unique_ips,sep='\n')