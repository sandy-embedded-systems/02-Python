# Task: Write a Python program to sum all the items in a list.
# Sample input: [1, 2, 3, 4, 5]
# Output: 15
def sum_elements(list):
    sum=0
    for item in list:
        if isinstance(item,int):
            sum+=item
    return sum
print(sum_elements([1, 2, 3, 4, 5]))
# Task: Write a Python program to multiply all the items in a list.
# Sample input: [1, 2, 3, 4]
# Output: 24
def product_elements(list):
    prod=1
    for item in list:
        if isinstance(item,int):
            prod*=item
    return prod
print(product_elements([1, 2, 3, 4, 5]))
# Task: Write a Python program to get the largest number from a list.
# Sample input: [1, 2, 3, 4, 5]
# Output: 5
def largest(list):
    large=list[0]
    for item in list:
        if item>large:
            large=item
    return large
print(largest([1, 2, 3, 4, 5]))
# Task: Write a Python program to get the smallest number from a list.
# Sample input: [1, 2, 3, 4, 5]
# Output: 1
def smallest(list):
    small=list[0]
    for item in list:
        if item<small:
            small=item
    return small
print(smallest([1, 2, 3, 4, 5]))
# Task: Write a Python program to count the number of strings where the string length is 2 or more and 
# the first and last character are the same from a given list of strings.
# Sample input: ['abc', 'xyz', 'aba', '1221']
# Output: 2
def count_strs(list):
    cnt=0
    for item in list:
        if len(item)>=2 and item[len(item)-1]==item[0]:
            cnt+=1
    return cnt
print(count_strs(['abc', 'xyz', 'aba', '1221']))
# Task: Write a Python program to get a list, sorted in increasing order by the last element in each 
# tuple from a given list of non-empty tuples.
# Sample input: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def get_last_item(x):
    return x[-1]
lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst.sort(key=get_last_item)
print(lst)

# Task: Write a Python program to remove duplicates from a list.
# Sample input: [1, 2, 3, 2, 4, 3, 5]
# Output: [1, 2, 3, 4, 5]
def rem_dups(lst):
    lst=list(set(lst))
    return lst
print(rem_dups([10,20,20,30,30]))

# Task: Write a Python program to check if a list is empty or not.
# Sample input: []
# Output: List is empty
def is_empty(lst):
    if len(lst)==0:
        print("List is empty")
        return 0
    else : return len(lst)
l1=[]
print(not is_empty(l1))

# Task: Write a Python program to clone or copy a list.
# Sample input: [1, 2, 3, 4]
# Output: [1, 2, 3, 4]
l1=[1,2,3,4]
l2=[]
l2=l1.copy()
print(l2)

# Task: Write a Python program to find the list of words that are longer than n from a given list of words.
# Sample input: ['hello', 'world', 'python', 'is', 'great'], n = 4
# Output: ['hello', 'world', 'python', 'great']
def list_strs(lst,n):
    new=[]
    for item in lst:
        if len(item)>n:
            new.append(item)
    return new
l=['hello', 'world', 'python', 'is', 'great']
print(list_strs(l,4))