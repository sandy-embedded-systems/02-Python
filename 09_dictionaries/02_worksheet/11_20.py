# 11. Empty Desk Detective
# You check a colleague's desk (dictionary) for items. If it's empty, print a 
# clear message so you don't miss anything!
# Input: desk = {}
# Expected Output: Dictionary is empty!
d={}
if len(d)==0:
    print("Dictionary is empty!")
else: print(len(d))

# 12. Max and Min Detective
# Among all your valuables (dictionary values), who owns the largest and smallest? Report 
# both the max and min key names.
# Input: valuables = {'ring': 5, 'necklace': 9, 'watch': 2}
# Expected Output: Max: 'necklace', Min: 'watch'
valuables = {'ring': 5, 'necklace': 9, 'watch': 2}
max_item=max(valuables, key=valuables.get)
min_item=min(valuables, key=valuables.get)
print("Max:",max_item)
print("Min:",min_item)

# 13. Substring Key Find
# Given a search term, find out which keys in your dictionary contain it. Useful for 
# partial name search!
# Input: d = {'hello': 1, 'world': 2, 'hell': 3}, substring = 'hell'
# Expected Output: Keys containing 'hell': ['hello', 'hell']
d= {'hello': 1, 'world': 2, 'hell': 3}
lst=[]
sub=input("Enter substring:")
for key in d:
    if key.find(sub)!=-1:
        lst.append(key)
print(lst)


# 14. Value to Key Reverse Find
# You know a value, but not which key owns it. Trace back and report the key for a given value!
# Input: d = {'x': 100, 'y': 200}, value = 200
# Expected Output: Key for value 200: 'y'
d = {'x': 100, 'y': 200}
value=200
for key in d:
    if d[key]==value:
        print("Key for value 200:",key)


# 15. Sort by Key
# Organize a scrambled dictionary by key order so that the output is sorted by key.
# Input: d = {'b': 2, 'a': 1, 'c': 3}
# Expected Output: [('a', 1), ('b', 2), ('c', 3)]
d={'b':2,'a':1,'c':3}
result=[]
for k in sorted(d):
    result.append((k,d[k]))
print(result)


# 16. Log Session Nested Dictionary from List
# Given a list, build a nested dictionary where each item is a deeper level (like a Russian doll).
# Input: lst = ['a', 'b', 'c', 'd']
# Expected Output: {'a': {'b': {'c': {'d': {}}}}}
lst=['a','b','c','d']
result={}
current=result
for item in lst:
    current[item]={}
    current=current[item]
print(result)


# 17. Flip Nested Dictionary
# Given a nested dictionary, swap the outer and inner keys. Who becomes the new outer boss?
# Input: d = {'x': {'p': 1}, 'y': {'q': 2}}
# Expected Output: {'p': {'x': 1}, 'q': {'y': 2}}
d={'x':{'p':1},'y':{'q':2}}
result={}
for outer in d:
    for inner in d[outer]:
        if inner not in result:
            result[inner]={}
        result[inner][outer]=d[outer][inner]
print(result)


# 18. Invert the Nest
# Given a nested dictionary of students and their subjects, flip it so that subjects are outer keys and students are inside.
# Input: d = {'math': {'john': 90, 'jane': 80}, 'science': {'john': 85, 'jane': 95}}
# Expected Output: {'john': {'math': 90, 'science': 85}, 'jane': {'math': 80, 'science': 95}}
d={'math':{'john':90,'jane':80},'science':{'john':85,'jane':95}}
result={}
for subject in d:
    for student in d[subject]:
        if student not in result:
            result[student]={}
        result[student][subject]=d[subject][student]
print(result)


# 19. Reverse the Order
# Reverse the order of keys in a dictionary, so the last becomes first and vice versa.
# Input: d = {'first': 1, 'second': 2, 'third': 3}
# Expected Output: {'third': 3, 'second': 2, 'first': 1}
d={'first':1,'second':2,'third':3}
result={}
keys=list(d.keys())
for k in reversed(keys):
    result[k]=d[k]
print(result)

# 20. Key Present in List and Dictionary
# Given a list and a dictionary, extract values for all keys that appear in both.
# Input: d = {'a': 100, 'b': 200, 'c': 300}, lst = ['b', 'c', 'd']
# Expected Output: {'b': 200, 'c': 300}
d = {'a': 100, 'b': 200, 'c': 300}
lst = ['b', 'c', 'd']
result={}
for item in lst:
    if item in d.keys():
        if item not in result:
            result[item]=d[item]
print(result)
