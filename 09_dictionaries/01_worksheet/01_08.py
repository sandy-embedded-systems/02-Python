# 1. Dictionaries
# Dictionaries let you store and organize data using key-value pairs. They are fundamental for mapping, counting, and fast lookups.
# Log Session a dictionary to store the roll numbers (as keys) and names (as values) for 3 students.
# Sample Output: {101: 'Ravi', 102: 'Priya', 103: 'Amit'}
# Suppose you write a dictionary with the same key twice. What value is stored?
# Sample Input: d = {'x': 1, 'y': 2, 'x': 5}
# Sample Output: {'x': 5, 'y': 2}
# How can you check if the key 'fruit' exists in a dictionary called d?
# Sample Input: d = {'fruit': 'apple', 'veg': 'carrot'}
# Sample Output: True (when checked for 'fruit')
# Count the frequency of each letter in the string "apple", store results in a dictionary, and print it.
# Sample Input: "apple"
# Sample Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}

students={101: 'Ravi', 102: 'Priya', 103: 'Amit'}
print(students)
d = {'x': 1, 'y': 2, 'x': 5}
d['x']=5
print(d) #the value at given existing key will be modified
d = {'fruit': 'apple', 'veg': 'carrot'}
if 'fruit' in d.keys():
    print(True)
else: print(False)
s = "apple"
result={}
for ch in s:
    result[ch]=result.get(ch, 0)+1
print(result)


# 2. Access Dictionaries
# Knowing how to access values by key lets you use and process dictionary data effectively.
# Given marks = {'math': 75, 'science': 80}, access and print the marks for 'science'.
# What happens if you try to access a key that doesn’t exist in a dictionary? Try to print the value for
# key 'english' in marks = {'math': 75}.
# Expected Output: A KeyError.
# How can you safely access a value for key 'history' in a dictionary scores without causing an error?
# Sample Input: scores = {'math': 80, 'science': 90}
# Expected Output: If not present, print a custom message like 'Not found'.
# Print all subjects and marks from this dictionary: student = {'math': 90, 'english': 88, 'science': 92}.
# Sample Output:
# math 90
# english 88
# science 92
marks = {'math': 75, 'science': 80}
print("Science marks:",marks['science'])
print("KeyERROR:",marks['english']) # intentionally Error is raised
scores = {'math': 80, 'science': 90}
if 'history' in scores.keys():
    print(scores['history'])
else:
    print("Key not found")
student = {'math': 90, 'english': 88, 'science': 92}
for key in student:
    print(key,":",student[key])
    

# 3. Change Dictionaries
# Updating dictionary values is needed when data changes during runtime.
# Update the age of 'Anil' from 21 to 22 in this dictionary: ages = {'Anil': 21, 'Sunita': 20}.
# Change multiple values at once in the dictionary: info = {'a': 10, 'b': 20} so that both 'a' 
# and 'b' become 100.
# Increase every salary in salaries = {'A': 20000, 'B': 30000} by 10%.
# Sample Output: {'A': 22000.0, 'B': 33000.0}
# Assign a value to a key that doesn't exist (e.g., add 'C': 25000 to salaries). What happens?
ages = {'Anil': 21, 'Sunita': 20}
ages['Anil']=22
print(ages)
info = {'a': 10, 'b': 20}
for key in info:
    info[key] = 100
print(info)
salaries = {'A': 20000, 'B': 30000}
for key in salaries:
    salaries[key]+=(salaries[key]//10)
print(salaries)

# 4. Add Dictionary Items
# Dynamic addition of new items allows for scalable and flexible data storage.
# Add 'Bangalore': 12000000 to cities = {'Delhi': 18000000, 'Mumbai': 20000000}.
# Add a key 'status' with value 'active' to user = {'name': 'Riya'} only if it doesn’t exist.
# Given a list ['dog', 'cat', 'rabbit'], create a dictionary with words as keys and their lengths as values.
# Expected Output: {'dog': 3, 'cat': 3, 'rabbit': 6}
# Merge two dictionaries: d1 = {'x': 1} and d2 = {'y': 2}.
# Expected Output: {'x': 1, 'y': 2}

cities = {'Delhi': 18000000, 'Mumbai': 20000000}
cities.update({'Banglore':12000000})
user = {'name': 'Riya'}
if 'status' not in user.keys():
    user.update({'status':'active'})
print(user)
lst=['dog', 'cat', 'rabbit']
d={}
for item in lst:
    d[item]=len(item)
print(d)
d1 = {'x': 1}
d2 = {'y': 2}
d1.update(d2)
print(d1)

# 5. Remove Dictionary Items
# Sometimes, you need to clean up or adjust your dictionary as data changes.
# Remove key 'math' from marks = {'math': 80, 'science': 85} using del.
# Use .pop() to remove 'name' from info = {'name': 'Amit', 'city': 'Pune'} and print the value removed.
# Remove all items from the dictionary: d = {'x': 1, 'y': 2}.
# Write a program to remove key 'z' from d = {'x': 1, 'y': 2} only if it exists.
# Expected Output: If not found, print 'Key not found'.
marks = {'math': 80, 'science': 85}
del(marks['math'])
print(marks)
info = {'name': 'Amit', 'city': 'Pune'}
info.pop('name')
print(info)
d = {'x': 1, 'y': 2}
d.clear()
print(d)
d = {'x': 1, 'y': 2}
if 'z' in d.keys():
    d.pop('z')
else: print("Key not exist")

# 6. Loop Dictionaries
# Iterating over dictionaries lets you process or filter keys and values.
# Loop and print all keys in d = {'a': 10, 'b': 20, 'c': 30}.
# Loop and print all values in the same dictionary.
# Loop and print each key and its value together.
# Print only the subjects with marks above 60 from scores = {'math': 75, 'science': 55, 'english': 82}.
# Sample Output:
# math
# english
d = {'a': 10, 'b': 20, 'c': 30}
for key in d:
    print(key)
for key in d:
    print(d[key])
for key,value in d:
    print(key,":",value)
scores = {'math': 75, 'science': 55, 'english': 82}
for key in scores.items():
    if scores[key]>=60:
        print(key)

# 7. Copy Dictionaries
# Copying dictionaries is critical when you need to manipulate data without affecting the original.
# Make a shallow copy of d = {'p': 2, 'q': 3} and print the copy.
# Show what happens when you do b = a with a = {'x': [1, 2]} and then modify b['x']. What happens to a?
# Log Session a copy of original = {'car': 'red', 'bike': 'blue'}. Change the 'car' in the copy to
# 'green' and print both dictionaries.
# Expected Output: Original remains unchanged.
# Explain (with code) the difference between a shallow copy and a deep copy using a nested dictionary.
# Show the effect of changing an inner list.
d = {'p': 2, 'q': 3}
copy=d.copy()
print(copy)
a = {'x': [1, 2]}
b=a
b['x']=[10,20]
print(a,"    ",b)
original = {'car': 'red', 'bike': 'blue'}
copy=original.copy()
copy['car']='green'
print(original,copy)
# 8. Nested Dictionaries
# Nested dictionaries help organize complex data, like student records or configurations.
# Represent student info with name, age, and a marks dictionary (math, english) using nested
# dictionaries for two students.
# Access and print the english marks of 'Rahul' in:

#         students = {

#           'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},

#           'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}

#         }
        
# Expected Output: 88
# For each student in the above students dictionary, print the name and all subject marks.
# Add 'science': 93 to 'Simran''s marks in the nested dictionary.
students = {
           'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
           'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
           }
print(students['Rahul']['marks']['english'])