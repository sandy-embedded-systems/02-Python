'''
Format Validator with Exception Handling
Create a script that reads the log file and identifies lines that do not match the expected log
format. For each misformatted line, log a warning with its line number while continuing to
process the rest of the file.
Challenge: Ensure that your solution uses try-except blocks to catch and handle exceptions
without crashing.
'''

import os
import sys
import re

logFile=input("Enter file name:")
if not os.path.exists(logFile):
    print("File not Found")
    sys.exit()
with open(logFile,'r') as file:
    line_num=1
    for line in file:
        try:
            m=re.match(r"\d{4}",line)
            m.group()
        except AttributeError:
            print(f"misformate : Exception at line:{line_num}")
        line_num+=1