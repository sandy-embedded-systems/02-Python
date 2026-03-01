'''
1. Basic Syntax and Data Types
• Concepts: Variables, basic data types (integers, floats, strings), and control structures (ifelse, loops).
• Task:
• Write a script that reads a text file and counts the occurrence of each word.
• Validation: Verify that the output dictionary correctly represents word counts for
given test files. 
'''

import os,re
filename=input("Enter fine name:")
words_freq={}
if os.path.exists(filename):
    with open(filename,"r") as file:
        text=file.read()
        Iter=re.finditer(r"\b\w+\b",text)
        for match in Iter:
            word=match.group()
            if word not in words_freq:
                words_freq[word]=1
            else: words_freq[word]+=1
    with open("new.txt",'w') as file:
        for key in words_freq:
            file.write(key+':'+ str(words_freq[key])+'\n')
        