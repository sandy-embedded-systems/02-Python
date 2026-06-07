'''
 1.Log Level Counter
Write a script that reads the provided log file and counts the number of occurrences of each
log level (INFO, DEBUG, WARNING, ERROR) using file I/O and dictionaries. Avoid using
regular expressions for this task.
Challenge: Ensure your code gracefully handles lines that do not follow the expected
format.
'''

import os,sys
log_file=input("Enter the log file name:")
occured={}
if not os.path.exists(log_file):
    print("File not Found")
    sys.exit()
with open(log_file,'r') as log:
    for line in log:
        if 'ERROR' in line:
            occured['ERROR']=occured.get('ERROR',0)+1
        elif 'INFO' in line:
            occured['INFO']=occured.get('INFO',0)+1
        elif 'WARNING' in line:
            occured['WARNING']=occured.get('WARNING',0)+1
        elif 'DEBUG' in line:
            occured['DEBUG']=occured.get('DEBUG',0)+1
for key,value in occured.items():
    print(f"{key}:{value}")
    
    
'''2.Error Log Extractor
Using basic string manipulation (without regex), write a script that filters and prints all log
entries containing the word “ERROR”.
Challenge: Verify that only well-formed error lines are extracted while ignoring
misformatted lines
'''
log_file=input("Enter the log file name:")
if not os.path.exists(log_file):
    print("File not Found")
    sys.exit()
with open(log_file)  as file:
    for line in file:
        if 'ERROR' in line:
            print(line)

