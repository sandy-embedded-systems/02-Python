# Question: Write a function introduction(name, country='India') that prints a message introducing the person and their country.
# Sample data:
# introduction("Sara")
# introduction("Alex", "USA")
# Expected output:
# My name is Sara and I am from India.
# My name is Alex and I am from USA.
def introduction(name, country="India"):
    print(f"My name is {name} and I am from {country}")

introduction("bitsilica")

# Question: Write a function calculate(a, b) that returns both the sum and difference of a and b.
# Sample data:
# s, d = calculate(10, 3)
# print("Sum:", s)
# print("Difference:", d)
# Expected output:
# Sum: 13
# Difference: 7
def calculate(a,b):
    return a+b,a-b
s,d=calculate(10,7)
print(s,d)

# Question: Write a function string_stats(s) that returns the number of vowels, consonants, and digits in the string s.
# Sample data:
# print(string_stats("Hello123"))
# Expected output:
# (2, 5, 3)
def string_stats(s):
    vowels=0
    consonants=0
    digits=0
    for ch in s:
        if ch.isdigit():
            digits+=1
        elif ch.isalpha():
            if ch.lower() in "aeiou":
                vowels+=1
            else:
                consonants+=1
    return vowels, consonants, digits
print(string_stats("Hello world"))


# Question: Write a function factorial(n) that uses recursion to calculate the factorial of a number.
# Sample data:
# print(factorial(5))
# Expected output:
# 120
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Question: Write a recursive function sum_list(lst) to return the sum of all elements in a list.
# Sample data:
# print(sum_list([1, 2, 3, 4]))
# Expected output:
# 10
def sum_list(lst):
    if len(lst) == 0:      # Base case
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
print(sum_list([1,2,3,4,5]))

# Question: Write a recursive function reverse_string(s) that returns the reversed string.
# Sample data:
# print(reverse_string("python"))
# Expected output:
# nohtyp
def reverse_str(s):
    return s[::-1]
print(reverse_str("Python"))
# Question: Write a recursive function fibonacci(n) that returns the nth Fibonacci number.
# Sample data:
# print(fibonacci(6))
# Expected output:
# 8
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(4))
# Question: Write a function min_max(numbers) that returns both the smallest and largest number 
# in a list (use returning multiple values).
# Sample data:
# small, large = min_max([8, 3, 5, 2, 10])
# print("Smallest:", small)
# print("Largest:", large)
# Expected output:
# 1
# 2
def min_max(numbers):
    if len(numbers) == 0:
        return None   # or raise ValueError("Empty list")

    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest
s,l=min_max([1,2,3,4,5])