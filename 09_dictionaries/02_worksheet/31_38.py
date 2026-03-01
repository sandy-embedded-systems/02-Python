# 31. Count Groups by Digit Sum
# Group numbers by the sum of their digits and report the size of the largest group.
# Input: nums = [11, 20, 12, 21, 3]
# Expected Output: 2
nums=[11,20,12,21,3]
groups={}
for num in nums:
    s=0
    for ch in str(num):
        s+=int(ch)
    if s not in groups:
        groups[s]=0
    groups[s]+=1
print(max(groups.values()))


# 32. Sort Dictionary Keys and Values List
# Sort a dictionary by keys, and also sort the values list of each key.
# Input: d = {'c': [3,1], 'a': [2,4], 'b': [5,1]}
# Expected Output: [('a', [2,4]), ('b', [1,5]), ('c', [1,3])]
d={'c':[3,1],'a':[2,4],'b':[5,1]}
result=[]
for k in sorted(d):
    d[k].sort()
    result.append((k,d[k]))
print(result)

# 33. Sort by Values Summation
# Sort a dictionary by the sum of its list values, from smallest to largest.
# Input: d = {'x': [5,5], 'y': [1,2,3], 'z': [10]}
# Expected Output: [('y', [1,2,3]), ('x', [5,5]), ('z', [10])]
d={'x':[5,5],'y':[1,2,3],'z':[10]}
result=sorted(d.items(),key=lambda x:sum(x[1]))
print(result)

# 34. Sort Dictionaries List by Key’s Value List Index
# Given a list of dictionaries, sort them by the value at a specific index in each key’s value list.
# Input: dicts = [{'a': [5,1]}, {'a': [3,4]}, {'a': [7,0]}], index = 1
# Expected Output: [{'a': [7,0]}, {'a': [5,1]}, {'a': [3,4]}]
dicts=[{'a':[5,1]},{'a':[3,4]},{'a':[7,0]}]
index=1
result=sorted(dicts,key=lambda x:x['a'][index])
print(result)

# 35. Sort Nested Keys by Value
# Sort the keys inside each nested dictionary by their value.
# Input: d = {'group1': {'b': 2, 'a': 1}, 'group2': {'c': 3, 'd': 0}}
# Expected Output: {'group1': [('a', 1), ('b', 2)], 'group2': [('d', 0), ('c', 3)]}
d={'group1':{'b':2,'a':1},'group2':{'c':3,'d':0}}
result={}
for group in d:
    sorted_items=sorted(d[group].items(),key=lambda x:x[1])
    result[group]=sorted_items
print(result)

# 36. Scoring Matrix Using Dictionary
# Build a scoring matrix for students and subjects using a dictionary.
# Input: students = ['A', 'B'], subjects = ['math', 'sci'], scores = [[90, 80], [85, 95]]
# Expected Output: {'A': {'math': 90, 'sci': 80}, 'B': {'math': 85, 'sci': 95}}
students = ['A', 'B']
subjects = ['math', 'sci']
scores = [[90, 80], [85, 95]]


# 37. Factors Frequency Dictionary
# Count the frequency of each factor for all numbers in a list using a dictionary.
# Input: nums = [10, 15]
# Expected Output: {1: 2, 2: 1, 5: 2, 10: 1, 3: 1, 15: 1}
nums=[10,15]
max=max(nums)
d={}
for n in nums:
    for i in range(1,max+1):
        if n%i==0:
            if i in d.keys():
                d[i]+=1
            else: d[i]=1
print(d)

# 38. Count Distinct Substrings (Rabin-Karp)
# Count all distinct substrings of a string using Rabin-Karp algorithm and a dictionary.
# Input: s = "abc"
# Expected Output: 6
def count_distinct_substrings(s):
    n=len(s)
    base=256
    mod=10**9+7
    result={}
    count=0

    for i in range(n):
        h=0
        for j in range(i,n):
            h=(h*base+ord(s[j]))%mod
            if h not in result:
                result[h]=1
                count+=1

    return count

s="abc"
print(count_distinct_substrings(s))
