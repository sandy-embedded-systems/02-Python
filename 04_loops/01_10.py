#1. Print all 3-digit numbers such that the sum of the cubes of their digits equals the number itself.
# Example: 153 → 1³ + 5³ + 3³ = 153
for num in range(100, 1000):
    temp=num
    sum_of_cubes=0
    while temp >0:
        digit=temp%10
        sum_of_cubes+=digit**3
        temp //= 10
    if sum_of_cubes==num:
        print(num)
print()

#2. For a given number, print its multiplication table from 1 to 10, but don’t use the * operator.
num=int(input("Enter a number: "))
for i in range(1,11):
    result=0
    for _ in range(i):
        result+=num   # adding num i times
    print(f"{num} x {i} = {result}")

# 3.Using only loops, print all prime numbers between 2 and n (n is user input).
n=int(input("ENter n:"))
for i in range(2,n):
    j=2
    while j<i:
        if temp%j==0: break
        j+=1
    if j==i: print(i)
print()

#4. For a given number of rows, print the following number pyramid pattern:
# 1
# 1 2
# 1 2 3
# ...
# 1 2 ... n
n=int(input("Enter n:"))
for i in range(1,n):
    for j in range(1,i):
        print(j,end=" ")
    print()
print()

#5. Take an integer input and print its digits in reverse order (don’t use slicing or strings).
num=int(input("Enter a number:"))
while num:
    print(num%10,end=" ")
    num//=10
print()

#6 Check if the input number reads the same backward as forward, using only loops and arithmetic.
num=int(input("Enter a number:"))
temp=num
sum=0
while num:
    sum+=(num%10)
    num//=10
if sum==temp:
    print("palindrome")
else:print("not a palindrome")

# 7 Ask for two numbers and compute their Greatest Common Divisor (GCD) using repeated subtraction
# or division with loops.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
while a!= b:
    if a>b:
        a=a-b
    else:
        b=b-a
print("GCD is:", a)
# 8 Print a hollow square pattern of size n (n ≥ 3).
# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
n = int(input("Enter size (n >= 3): "))

if n < 3:
    print("Size must be at least 3")
else:
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print() 
print()

#9. Take an integer and, using only loops, sum its digits repeatedly until only a single digit remains.
# Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2
num=int(input("Enter a number:"))
while num<9:
    sum=0
    temp=num;
    while temp:
        sum+=(temp%10)
        temp//=10
    if sum<9:
        print(sum)
        break
    num=sum

#10. Input a number and count how many digits it contains, using only arithmetic and loops.
num=int(input("Enter a number:"))
count=0
while num:
    count+=1
    num//=10
print(count)
