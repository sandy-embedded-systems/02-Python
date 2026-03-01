# Description: Compute the element-wise sum of multiple tuples of equal length.
# This exercise teaches how to combine tuples by adding corresponding elements, often used in mathematical and data processing tasks.
# Input: t1 = (1, 2, 3, 4), t2 = (3, 5, 2, 1), t3 = (2, 2, 3, 1)
# Output: (6, 9, 8, 6)
t1 = (1, 2, 3, 4) 
t2 = (3, 5, 2, 1) 
t3 = (2, 2, 3, 1)
lst=[]
i=0
while i<len(t1):
    lst.append(t1[i]+t2[i]+t3[i])
    i+=1
t=tuple(lst)
print(t)

# Description: Calculate the product by multiplying all the numbers in a tuple.
# This is useful for aggregate calculations and is commonly found in mathematical programming and statistics.
# Input: t = (4, 3, 2, 2, -1, 18)
# Output: -864
t4 = (4, 3, 2, 2, -1, 18)
prod=1
for ele in t4:
    prod*=ele
prod(prod)

# Description: Convert a tuple of positive integers into a single integer by concatenating their values.
# This is a common data transformation task, often seen in problems that require generating a unique number
# from a sequence.
# Input: t = (1, 2, 3)
# Output: 123
t5 = (1, 2, 3)
res=0
for i in t5:
    res=res*10+i
print(res)

# Description: Sort a tuple of (string, float) pairs by the float value in descending order.
# Sorting by a specific field is essential in data analysis and organization, especially when dealing 
# with mixed data types.
# Input: t = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))
# Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
t6 = (('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))
t_list = list(t6)
def get_float(pair):
    return float(pair[1])
t_list.sort(key=get_float, reverse=True)
print(t_list)

# Description: Find all possible pair combinations from two tuples, combining each element from the first
# tuple with each from the second.
# This problem introduces the concept of Cartesian product and is useful for combinatorial tasks.
# Input: t1 = (1, 2), t2 = (3, 4)
# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]
t7 = (1, 2)
t8 = (3, 4)
lst=[]
sample=[]
for i in t7:
    for j in t8:
        sample.append(i)
        sample.append(j)
        lst.append(tuple(sample))
        sample.clear()
print(lst)

# Description: Compute the frequency of each element in a tuple and return the result as a dictionary.
# Element frequency counting is widely used for data summarization, analytics, and validation tasks.
# Input: t = (1, 2, 2, 3, 3, 3)
# Output: {1: 1, 2: 2, 3: 3}
def findFreq(tup):
    result={}
    for n in tup:
        if n not in result:
            result[n]=1
        else: result[n]+=1
    return result
print(findFreq((1, 2, 2, 3, 3, 3)))


# Description: Filter a list of tuples, keeping only those where the tuple length or value at a specific
# index meets a condition.
# This task helps develop conditional filtering skills and deeper data selection logic in nested structures.
# Input: lst = [(1, 2, 3), (4, 5), (6, 7, 8)], Keep tuples of length 3
# Output: [(1, 2, 3), (6, 7, 8)]
lst = [(1, 2, 3), (4, 5), (6, 7, 8)]
k=3
i=0
while i<len(lst):
    if len(lst[i])<3:
        lst.remove(lst[i])
    i+=1
print(lst)

# Description: Check if a specified value is present in any of the inner tuples in a tuple of tuples.
# This teaches how to search through nested tuples, which is useful in multi-dimensional data handling.
# Input: t = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')),
# Check:'White'
# Output: True
t9= (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
check=input("Enter word to check:")
flag=True
for item in t9:
    if check in item:
        flag=False
        print(True)
        break
if flag: print(False)

# Description: Convert a tuple of key-value pairs into a dictionary.
# This conversion is fundamental in Python for transitioning between sequence and mapping data types for fast lookups.
# Input: t = (('a', 1), ('b', 2), ('c', 3))
# Output: {'a': 1, 'b': 2, 'c': 3}
t10= (('a', 1), ('b', 2), ('c', 3))
result={}
for item in t10:
    result[item[0]]=item[1]
print(result)

# Description: Perform elementwise AND and XOR operations between two tuples of integers of equal length.
# Elementwise bitwise operations are crucial in low-level data processing and algorithm optimization.
# Input: t1 = (1, 2, 3), t2 = (2, 2, 2)
# Output: AND: (0, 2, 2), XOR: (3, 0, 1)
t11=(1, 2, 3)
t12=(2, 2, 2)
and_result=tuple(t1[i] & t2[i] for i in range(len(t1)))
xor_result=tuple(t1[i] ^ t2[i] for i in range(len(t1)))
print("AND:", and_result)
print("XOR:", xor_result)