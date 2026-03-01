'''
2. File I/O Operations
• Concepts: Reading from and writing to files, handling file paths, and using context
managers.
• Task:
• Create a script that reads a log file, filters specific lines (e.g., containing "ERROR"),
and writes the filtered content to a new file.
• Validation: Check that the output file contains only the lines that meet the filter
criteria. '''

import os,sys
filename=input("Enter file name:")
word='ERROR'
target=open('filter.log','w')
if os.path.exists(filename):
    with open(filename,"r") as fp:
        for line in fp:
            if line.count(word):
                target.write(line)
else:
    print("No such file")
    sys.exit()
    target.close()
target.close()
