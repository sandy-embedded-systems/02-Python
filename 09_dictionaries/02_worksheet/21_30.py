# 21. Remove High-Value Keys
# Remove all keys whose value is greater than a given number. Ignore non-numeric values.
# Input: d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}, limit = 10
# Expected Output: {'a': 5, 'b': 10, 'd': 'big'}
d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}
limit = 10

# 22. Remove Keys with Substring
# Remove all keys from the dictionary that contain a certain substring (like a keyword filter).
# Input: d = {'sun': 1, 'sunny': 2, 'rain': 3}, substring = 'sun'
# Expected Output: {'rain': 3}
d={'sun':1,'sunny':2,'rain':3}
substring='sun'
result={}
for key in d:
    if substring not in key:
        result[key]=d[key]
print(result)


# 23. Dictionary with Most Pairs
# Given multiple dictionaries, find the one with the most key-value pairs (the biggest dictionary wins).
# Input: dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]
# Expected Output: {'x': 1, 'y': 2, 'z': 3}
dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]
idx=-1
i=0
temp=0
for item in dicts:
    if len(item)>temp:
        temp=len(item)
        idx=i
    i+=1
print(dicts[idx])

# 24. Append Dictionary Keys and Values
# Append the keys and values of one dictionary to another, keeping the order. Build a bigger dictionary!
# Input: d1 = {'one': 1, 'two': 2}, d2 = {'three': 3, 'four': 4}
# Expected Output: {'one': 1, 'two': 2, 'three': 3, 'four': 4}
d1 = {'one': 1, 'two': 2}
d2 = {'three': 3, 'four': 4}
d1.update(d2)
print(d1)

# 25. Extract Unique Dictionary Values
# Extract all unique values from the dictionary. How many distinct items are there?
# Input: d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
# Expected Output: [1, 2, 3]
lst=[]
d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
for key in d:
    if d[key] not in lst:
        lst.append(d[key])
print(lst)
    

# 26. Keys Associated with Values
# Find all keys that share the same value. Group keys by their values.
# Input: d = {'m': 1, 'n': 2, 'o': 1}
# Expected Output: {1: ['m', 'o'], 2: ['n']}
d={'m':1,'n':2,'o':1}
result={}
for key in d:
    value=d[key]
    if value not in result:
        result[value]=[]
    result[value].append(key)
print(result)


# 27. Filter Dictionary Values in Heterogeneous Dictionary
# Your dictionary has mixed value types. Filter only the integer values into a new dictionary.
# Input: d = {'x': 100, 'y': 'hello', 'z': 200}
# Expected Output: {'x': 100, 'z': 200}
d = {'x': 100, 'y': 'hello', 'z': 200}
result={}
for key in d:
    if isinstance(d[key],int):
        if key not in result:
            result[key]=d[key]
        else: result.update({key,d[key]})
print(result)

# 28. Print Anagrams Together Using List and Dictionary
# Group words that are anagrams together from a list (all the jumbled twins in one basket).
# Input: words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']
# Expected Output: [['listen', 'silent', 'enlist'], ['hello', 'ohlle']]
words=['listen','silent','enlist','hello','ohlle']
groups={}
for word in words:
    key="".join(sorted(word))
    if key not in groups:
        groups[key]=[]
    groups[key].append(word)

result=list(groups.values())
print(result)

# 29. Check if Binary Representations of Two Numbers are Anagrams
# Given two numbers, check if their binary representations are anagrams (same bits, just shuffled).
# Input: num1 = 5, num2 = 6
# Expected Output: False
num1=int(input("enter num1:"))
num2=int(input("Enter num2:"))
if num1.bit_count()==num2.bit_count():
    print(True)
else: print(False)


# 30. Largest Subset of Anagram Words
# Given a list of words, find the size of the largest subset where all are anagrams of each other.
# Input: words = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
# Expected Output: 3
words=['bat','tab','eat','tea','tan','nat']
groups={}
for word in words:
    key="".join(sorted(word))
    if key not in groups:
        groups[key]=0
    groups[key]+=1
print(max(groups.values()))