'''
7. Data Structures: Lists, Dictionaries, and Sets
• Concepts: Efficient use of lists, dictionaries, tuples, and sets to store and manipulate data.
• Task:
• Given a list of log lines, group them by severity (e.g., INFO, WARNING, ERROR)
using a dictionary.
• Validation: Verify that the dictionary keys and counts correctly reflect the
distribution of log entries. 
'''

import os,sys
filename=input("Enter file name:")
if not os.path.exists(filename):
    print("File not exist:")
    sys.exit()
count={}
with open(filename,'r') as fp:
    for line in fp:
        if 'ERROR' in line:
            count['ERROR']=count.get('ERROR',0)+1
        elif 'INFO' in line:
            count['INFO']=count.get('INFO',0)+1
        elif 'WARN' in line:
            count['WARN']=count.get('WARN',0)+1
for key,value in count.items():
    print(f"{key}:{value}")