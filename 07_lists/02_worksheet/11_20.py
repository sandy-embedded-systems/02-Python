# Task: Write a Python program to find the common elements between two lists.
# Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
# Output: [3, 4]
def common(l1,l2):
    common_list=[]
    for item in l1:
        if item in l2:
            common_list.append(item)
    return common_list
print(common([1, 2, 3, 4], [3, 4, 5, 6]))
# Task: Write a Python program to flatten a shallow list.
# Sample input: [[1, 2], [3, 4], [5, 6]]
# Output: [1, 2, 3, 4, 5, 6]
def flatten(lst):
    flat=[]
    for item in lst:
        if isinstance(item,list):
            flat.extend(flatten(item))
        else: flat.append(item)
    return flat
l=[[1, 2], [3, 4], [5, 6]]
print(flatten(l))

# Task: Write a Python program to create a list of squares from 1 to 10 using list comprehension.
# Sample input: Range: 1 to 10
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
start=int(input("start of range:"))
end=int(input("End of range:"))
if start>end:
    start,end=end,start
lst=[x**2 for x in range(start,end+1)]
print(lst)

# Task: Write a Python program to create a list of even numbers from a given list using list comprehension.
# Sample input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [2, 4, 6, 8, 10]
def even_list(lst):
    even=[x for x in lst if x%2==0]
    return even
print(even_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Task: Write a Python program to remove all occurrences of a specific element from a list.
# Sample input: [1, 2, 3, 2, 4, 2, 5], element to remove: 2
# Output: [1, 3, 4, 5]
def remEle(lst,ele):
    for item in lst:
        if item ==ele:
            lst.remove(item)
    return lst
lst=[1, 2, 3, 2, 4, 2, 5]
print(remEle(lst,2))

# Task: Write a Python program to insert an element at a specified position in a list.
# Sample input: [1, 2, 3, 4], element: 5, position: 2
# Output: [1, 2, 5, 3, 4]
def insert_ele(lst,ele,pos):
    if pos>len(lst):
        return
    else: lst.insert(pos,ele)
l=[1,2,3,4]
insert_ele(l,5,2)
print(l)

# Task: Write a Python program to combine two lists into a dictionary.
# Sample input: ['a', 'b', 'c'], [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}
def combine(lst1, lst2):
    if len(lst1)!=len(lst2):
        print("Combination not possible")
        return None 
    result={}
    for key, value in zip(lst1, lst2):
        result[key]=value
    return result
print(combine(['a', 'b', 'c'], [1, 2, 3]))

# Task: Write a Python program to unzip a list of tuples into individual lists.
# Sample input: [(1, 'a'), (2, 'b'), (3, 'c')]
# Output: [1, 2, 3], ['a', 'b', 'c']
def unzip(lst):
    lst1=[]
    lst2=[]
    for tup in lst:
        lst1.append(tup[0])
        lst2.append(tup[1])
    return lst1,lst2
print(unzip([(1, 'a'), (2, 'b'), (3, 'c')]))
    
# Task: Write a Python program to create a list of numbers from 1 to 20, where each number is squared if 
# it is even, and cubed if it is odd.
# Sample input: Range: 1 to 20
# Output: [1, 4, 27, 16, 125, 36, 343, 64, 729, 100, 1331, 144, 2197, 196, 3375, 256, 4913, 324, 6859, 400]
def create():
    lst=[]
    for i in range(1,21):
        if i%2!=0:
            lst.append(i**3)
        else: lst.append(i**2)
    return lst
print(create())

# Task: Write a Python program to create a 3x3 matrix using nested list comprehensions.
# Sample input: Rows: 3, Columns: 3
# Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
# Dimensions
rows=3
cols=3
matrix=[[i for _ in range(cols)] for i in range(rows)]
print(matrix)
