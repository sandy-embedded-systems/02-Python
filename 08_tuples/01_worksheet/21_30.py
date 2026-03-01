# Description: Sort a list of (name, age) tuples by the second element (age) in ascending order.
# Sorting tuples by a specific key is frequently used for ordering structured data.
# Input: lst = [("Alice", 25), ("Bob", 20), ("Eve", 22)]
# Output: [('Bob', 20), ('Eve', 22), ('Alice', 25)]
lst = [("Alice", 25), ("Bob", 20), ("Eve", 22)]
def get_age(person):
    return person[1]
lst.sort(key=get_age)
print(lst)

# Description: Sort a list of tuples by the total number of digits across all elements in each tuple.
# This requires counting the digits and sorting accordingly, which strengthens comprehension of tuple processing.
# Input: lst = [(1, 2), (10, 11), (3, 44)]
# Output: [(1, 2), (3, 44), (10, 11)]
def get_digits(x):
    digits=0
    for item in x:
        digits+=len(str(item))
    return digits
lst = [(1, 2), (10, 11), (3, 44)]
lst.sort(key=get_digits)
print(lst)


# Description: Change the last value in every tuple in a list to a given value.
# This shows how to modify immutable data structures by reconstructing them.
# Input: lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)], New value: 100
# Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value=100
modified=[]
for t in lst:
    new_tuple=t[:-1]+(new_value,)
    modified.append(new_tuple)
print(modified)


# Description: Remove all empty tuples from a list of tuples and print the cleaned list.
# This is useful for sanitizing input data before processing.
# Input: lst = [(), (), ('a', 'b'), ('c',)]
# Output: [('a', 'b'), ('c',)]
lst = [(), (), ('a', 'b'), ('c',)]
filtered=[]
for item in lst:
    if item:
        filtered.append(item)
print(filtered)


# Description: Count the number of tuples where every element is divisible by a given integer K.
# This builds filtering skills and strengthens logic construction for data validation.
# Input: lst = [(3, 6), (9, 12, 15), (4, 8)], K = 3
# Output: 2
count=0
k=3
lst.clear()
lst = [(3, 6), (9, 12, 15), (4, 8)]
for tup in lst:
    flag=True
    for ele in tup:
        if ele%k!=0: flag=False
    if flag: count+=1
print(count)

# Description: From a list of tuples, keep only those where all numbers are positive.
# Filtering based on condition is commonly used for cleaning or selecting data.
# Input: lst = [(1, 2), (-3, 4), (5, 6)]
# Output: [(1, 2), (5, 6)]
lst.clear()
lst = [(1, 2), (-3, 4), (5, 6)]
temp=[]
for item in lst:
    flag=True
    for ele in item:
        if ele<0: flag=False
    if flag:
        temp.append(item)
print(temp)

# Description: For each tuple in a list, calculate the sum of its elements and print a list of the results.
# Summing elements within tuples is essential for data aggregation and analysis.
# Input: lst = [(1, 2), (2, 3), (3, 4)]
# Output: [3, 5, 7]
lst = [(1, 2), (2, 3), (3, 4)]
temp=[]
for item in lst:
    sum=0
    for ele in item:
        sum+=ele
    temp.append(sum)
print(temp)

# Description: Given a list of pairs (tuples), separate each position into its own list (unzipping).
# Unzipping is key for parallel data processing and converting between row-wise and column-wise formats.
# Input: lst = [(1, 'a'), (2, 'b'), (3, 'c')]
# Output: [1, 2, 3]
# ['a', 'b', 'c']
lst = [(1, 'a'), (2, 'b'), (3, 'c')]
l1=[]
l2=[]
for item in lst:
    l1.append(item[0])
    l2.append(item[1])
print(l1)
print(l2)

# Description: Convert a tuple of nested tuples into a single flat tuple.
# Flattening data structures is often needed for uniform data processing and analysis.
# Input: t = ((1, 2), (3, 4), (5, 6))
# Output: (1, 2, 3, 4, 5, 6)
def flattened(t):
    flat=[]
    for item in t:
        if isinstance(item,tuple):
            flat.extend(flattened(item))
        else:
            flat.append(item)
    return tuple(flat)
print(flattened(((1, 2), (3, 4), (5, 6))))

# Description: Find all unique elements present in a tuple of tuples using set logic.
# This teaches set operations and how to process nested iterable structures.
# Input: t = ((1, 2), (2, 3), (4, 5))
# Output: {1, 2, 3, 4, 5}
tup_1 = ((1, 2), (2, 3), (4, 5))
result=set()
for item in tup_1:
    for n in item:
        result.add(n)
print(result)
