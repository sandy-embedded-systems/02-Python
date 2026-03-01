# Description: Log Session a tuple containing elements of various data types, 
# including int, float, string, and bool.
# This helps understand how tuples can store heterogeneous data and is useful 
# for practical Python applications.
# Input: No input; directly define the tuple.
# Output: (10, 3.14, "Python", True)
tup=(10, 3.14, "Python", True)
print(tup)


# Description: Print the first and last elements of a tuple using positive and negative indexing.
# Learn how to access tuple elements using both forward and backward indexes, which is essential 
# for tuple manipulation.
# Input: my_tuple = (10, 20, 30, 40, 50)
# Output: 10
# 50
my_tuple = (10, 20, 30, 40, 50)
print("First element:",my_tuple[0],"Last element=",my_tuple[-1])


# Description: Unpack a tuple into three variables and print each variable separately.
# This exercise teaches you how tuple unpacking works and is commonly used in data assignment.
# Input: t = (1, 2, 3)
# Output: 1
# 2
# 3
tuple_pack=(1,2,3)
a,b,c= tuple_pack
print(a,b,c,sep='\n')


# Description: Check if a specified value exists in a tuple and print the result.
# Use the "in" keyword to efficiently search for elements inside a tuple.
# Input: my_tuple = ('a', 'b', 'c'), Check: 'b'
# Output: True
my_tup = ('a', 'b', 'c')
if 'b' in my_tup:
    print(True)
else: print(False)


# Description: Slice a tuple to obtain a sub-tuple containing elements from index 1 to 3.
# Slicing is important for extracting parts of a tuple without modifying the original.
# Input: t = (0, 1, 2, 3, 4, 5)
# Output: (1, 2, 3)
t=(0,1,2,3,4,5)
print(t[1:4])

# Description: Print the number of elements in a tuple using the len() function.
# Knowing the length of tuples is crucial when iterating or validating data.
# Input: t = (10, 20, 30, 40)
# Output: 4
t1 = (10, 20, 30, 40)
print(len(t))

# Description: Iterate through all elements in a tuple and print each one on a separate line.
# Looping over tuples is a fundamental skill for data processing and display.
# Input: t = ("apple", "banana", "cherry")
# Output: apple
# banana
# cherry
t2 = ("apple", "banana", "cherry")
for item in t2:
    print(item)
    
# Description: Join two tuples together using the + operator and print the result.
# Concatenation helps combine multiple tuples into a single sequence for further processing.
# Input: t1 = (1, 2), t2 = (3, 4)
# Output: (1, 2, 3, 4)
t3 = (1, 2)
t4 = (3, 4)
res=t3+t4
print(res)

# Description: Repeat a tuple’s elements multiple times using the * operator.
# Tuple repetition is useful for generating predictable patterns or test data.
# Input: t = (5, 6)
# Output: (5, 6, 5, 6, 5, 6)
t5=(5, 6)
result=t5*3
print(result)

# Description: Find and print the maximum and minimum values in a tuple of numbers.
# This is helpful for statistical analysis and summarizing numeric data in tuples.
# Input: t = (11, 3, 55, 21)
# Output: 55
# 3
t6=(11,3,55,21)
print("min=",min(t6),"   ","max=",max(t6))