# Take a number as input and calculate its factorial using loops (no recursion).
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

# For n rows, print a right-aligned triangle pattern:
#     *
#    **
#   ***
#  ****
# *****
n=int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

# Print the sum of all odd numbers from 1 up to n (inclusive), using loops only.
sum=0
n=int(input("Enter number of rows: "))
for i in range(1, n + 1):
    sum+=i
print(sum)

# Check if a given number is a perfect number (sum of divisors excluding itself), using only loops.
num = int(input("Enter a number: "))
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
if sum_div == num:
    print("Perfect number")
else:
    print("Not a perfect number")

# Print all numbers from n down to 1 using a single loop.
n=int(input("Enter number of rows: "))
while n!=1:
    print(n,end=" ")
    n-=1

# Input an integer and count how many times 0 appears in it (no strings or lists).
num=int(input("Enter a number:"))
count=0
while num:
    if(num%10 ==0): count+=1
    num//=10
print(count)

# Using only loops and arithmetic, compute the sum of all numbers below 1000 that are multiples of 3 or 5.
sum=0
for i in range(1,1000):
    if i%3==0 or i%5==0: sum+=i
print(sum)

# Input a number and find its smallest divisor greater than 1 (using only loops).
num=int(input("Enter a number:"))
for i in range(2,num):
    if num%i==0:
        print(i)
        break

# For n rows, print the following double triangle pattern:
# *
# **
# ***
# **
# *
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    print("*" * i)
for i in range(n-1,0,-1):
    print("*" * i)
# Input n and print the nth Fibonacci number using only variable updates and a loop (no lists, no recursion).
n=int(input("Enter n: "))
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    a=0
    b=1
    for _ in range(2,n+1):
        c=a+b
        a=b
        b=c
    print(b)
