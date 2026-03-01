# Description: Convert a list to a tuple and a tuple to a list using built-in functions.
# Mastering conversion between these types is vital for interoperability in Python programs.
# Input: lst = [1, 2, 3], tup = (4, 5, 6)
# Output: Tuple: (1, 2, 3)
# List: [4, 5, 6]
lst = [1, 2, 3]
tup = (4, 5, 6)
print("Tuple:",list(tup))
print("List:",tuple(lst))

# Description: Add an item to a tuple by converting it to a list and back to a tuple.
# This demonstrates tuple immutability and how to work around it for adding elements.
# Input: t = (1, 2, 3), Add: 4
# Output: (1, 2, 3, 4)
t = (1, 2, 3)
lst=list(t)
lst.append(4)
new_t=tup(lst)
print(new_t)

# Description: Remove a specific element from a tuple by converting it to a list and back.
# Removing elements from tuples is a common interview question testing immutability handling.
# Input: t = (1, 2, 3, 4), Remove: 2
# Output: (1, 3, 4)
t1 = (1, 2, 3, 4)
lst.clear()
lst=list(t1)
lst.remove(2)
new_t1=tuple(lst)
print(new_t1)

# Description: Convert a tuple of characters to a string and then back to a tuple.
# Useful for text manipulation and transitioning between data representations.
# Input: t = ('P', 'y', 't', 'h', 'o', 'n')
# Output: String: "Python"
# Tuple: ('P', 'y', 't', 'h', 'o', 'n')
t2 = ('P', 'y', 't', 'h', 'o', 'n')
s="".join(t2)
print(s)


# Description: Convert a tuple of string numbers to a tuple of integers using comprehension.
# This is important for data cleaning and type conversion in real-world datasets.
# Input: t = (("11", "22"), ("33", "44"))
# Output: ((11, 22), (33, 44))
t3= (("11", "22"), ("33", "44"))
res_tup=tuple(tuple((int(x) for x in item)) for item in t3 )
print(res_tup)


# Description: Find the index of a specified value in a tuple using the index() method.
# Locating elements within tuples is crucial for data lookup and manipulation.
# Input: t = ("cat", "dog", "rabbit"), Find: "dog"
# Output: 1
t4 = ("cat", "dog", "rabbit")
print(t4.index("dog"))

# Description: Count how many times a particular value occurs in a tuple.
# Element frequency counting is useful for analytics and validation tasks.
# Input: t = (1, 2, 3, 2, 2, 4), Count: 2
# Output: 3
t5 = (1, 2, 3, 2, 2, 4)
print(t5.count(2))

# Description: Reverse the order of items in a tuple and print the result.
# This practice is helpful in problems requiring reverse traversal or reordering.
# Input: t = (10, 20, 30, 40)
# Output: (40, 30, 20, 10)
t6 = (10, 20, 30, 40)
lst.clear()
lst=list(t6)
lst.reverse()
new_t6=tuple(lst)
print(new_t6)

# Description: Identify and print elements that occur more than once in a tuple.
# Spotting duplicates in sequences is common in data cleaning and interviews.
# Input: t = (2, 4, 6, 2, 8, 4, 6, 2)
# Output: 2, 4, 6
t7 = (2, 4, 6, 2, 8, 4, 6, 2)
seen = set()
duplicates = []
for x in t7:
    if x in seen and x not in duplicates:
        duplicates.append(x)
    seen.add(x)
print(*duplicates)

# Description: Check whether all elements in a tuple are unique using set comparison.
# Ensures data integrity in scenarios where duplicate values are not allowed.
# Input: t = (1, 2, 3, 4, 5)
# Output: True
t8 = (1, 2, 3, 4, 5)
set1=set(t8)
if len(t8) ==len(set1):
    print(True)
else: print(False)
