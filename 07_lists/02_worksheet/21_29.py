# Task: Write a Python function to reverse a list at a specific location.
# Sample input: [1, 2, 3, 4, 5, 6], position: 3
# Output: [1, 2, 3, 6, 5, 4]
def reverse_specific(lst,pos):
    index=pos-1
    lst[index:]=lst[index:][::-1]
    return lst
print(reverse_specific([1, 2, 3, 4, 5, 6],3))

# Task: Write a Python function to find the length of the longest increasing sub-sequence in a list of numbers.
# Sample input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
# Output: 6
# (The longest increasing subsequence is [10, 22, 33, 50, 60, 80])
def lis_length(arr):
    n=len(arr)
    dp=[1]*n

    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)

    return max(dp)

arr=[10,22,9,33,21,50,41,60,80]
print(lis_length(arr))


# Task: Write a Python function that generates all the permutations of the elements in a given list.
# Sample input: [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
def permute(lst):
    if len(lst)==0:
        return [[]]

    result=[]
    for i in range(len(lst)):
        remaining=lst[:i]+lst[i+1:]
        for p in permute(remaining):
            result.append([lst[i]]+p)
    return result

print(permute([1,2,3]))


# Task: Write a Python function to find the k-th smallest element in a list.
# Sample input: [7, 10, 4, 3, 20, 15], k = 3
# Output: 7
def kth_smallest(lst,k):
    temp=sorted(lst)
    if k>len(lst): return None
    else : return temp[k-1]
print(kth_smallest([7, 10, 4, 3, 20, 15],3))

# Task: Write a Python function to check if a given list is a palindrome (reads the same forwards and backwards).
# Sample input: [1, 2, 3, 2, 1]
# Output: True
def check_palindrome(lst):
    i,j=0,len(lst)-1
    while i<j:
        if lst[i]!=lst[j]:
            print("No a palindrome")
            return
        i+=1
        j-=1
    print("palindrome")
check_palindrome([1, 2, 3, 2, 1])
# Task: Write a Python function to find the union and intersection of two lists.
# Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
# Output: Union: [1, 2, 3, 4, 5, 6]
# Intersection: [3, 4]
def union_inter(lst1,lst2):
    list_union=list(set(lst1).union(lst2))
    list_inter=list(set(lst1).intersection(lst2))
    print(list_union)
    print(list_inter)
union_inter([1, 2, 3, 4], [3, 4, 5, 6])

# Task: Write a Python function to remove duplicates from a list while preserving the original 
# order of the remaining elements.
# Sample input: [1, 2, 2, 3, 4, 4, 5, 6, 5]
# Output: [1, 2, 3, 4, 5, 6]
def rem_dups(lst):
    seen=set()
    result=[]
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(rem_dups([1, 2, 2, 3, 4, 4, 5, 6, 5]))

# Task: Write a Python function to find the maximum sum sub-sequence in a list (sub-sequence, 
# not necessarily contiguous).
# Sample input: [2, -1, 2, 3, 4, -5]
# Output: 11
# (The maximum sum subsequence is 2 + 2 + 3 + 4)
lst=[2, -1, 2, 3, 4, -5]
sum=0
for item in lst:
    if item>0:
        sum+=item
print(sum)


# Task: Write a Python function to find the longest common subsequence between two lists.
# Sample input: [1, 3, 4, 1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]
# Output: [3, 4, 1, 3]
def lcs(a,b):
    m=len(a)
    n=len(b)
    dp=[[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    i=m
    j=n
    result=[]
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            result.append(a[i-1])
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1

    result.reverse()
    return result

a=[1,3,4,1,2,3,4,1]
b=[3,4,1,2,1,3]
print(lcs(a,b))