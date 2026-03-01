'''
8. List and Dictionary Comprehensions
• Concepts: Using comprehensions for concise and efficient data transformations.
• Task:
• Write a script that filters out and transforms a list of log entries using list
comprehensions (for instance, extracting only error messages).
• Validation: Confirm that the resultant list contains only the expected entries.
'''


import os,sys
filename=input("Enter file name:")
msg=input("enter msg to filter lines:")

if not os.path.exists(filename):
    print("File not exist:")
    sys.exit()
with open(filename,'r') as file:
    lines=file.readlines()
    filtered=[l for l in lines if msg in l]
    for l in filtered:
        print(l)
