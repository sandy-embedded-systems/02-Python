# Question: Write a function print_details(name, age) that prints a sentence using both parameters.
# Sample data:
# print_details("Alice", 25)
# Expected output:
# Name: Alice, Age: 25
def print_details(name,age):
    print(f"naem:{name}, age:{age}")
print_details('Bitsilica',7)

# Question: Write a function multiply(x, y) that returns the product of its two arguments.
# Sample data:
def multiply(a,b):
    return a*b
result = multiply(4, 5)
print(result)

# Question: Write a function greet_person(name, greeting) that prints a personalized message like "Hello, John!" using the arguments.
# Sample data:
# greet_person("John", "Hi")
# Expected output:
# Hi, John!
def greet_person(name,greet):
    print(f"{greet}, {name}")
greet_person('Bitsilica','hello')


# Question: Write a function area_of_circle(radius) that returns the area (πr²) of a circle for the given radius.
# Sample data:
# print(area_of_circle(3))
# Expected output:
# 28.274333882308138
def area_of_circle(rad):
    return 3.14*3.14*rad
print(area_of_circle(5))


# Question: Write a function is_negative(number) that returns True if the number is negative, else False.
# Sample data:
# print(is_negative(-7))
# print(is_negative(0))
# Expected output:
# True
# False
def is_negative(num):
    if num<0: return True
    else: return False
print(is_negative(-1))


# Question: Write a function grade(score) that returns 'A' if score ≥ 90, 'B' if 80 ≤ score < 90, 
# 'C' if 70 ≤ score < 80, and 'F' for anything less.
# Sample data:
# print(grade(85))
# print(grade(72))
# print(grade(50))
# Expected output:
# 1
# 2
# 3
# B
# C
# F
def grade(score):
    if score>=90: return 'A'
    elif score<=80 and score<90: return 'B'
    elif score>=70 and score<80: return 'C'
    else: return 'F'
print(grade(90))


# Question: Write a function sign(num) that returns 'Positive' if num > 0, 'Negative' if num < 0, and 'Zero' if num == 0.
# Sample data:
# print(sign(10))
# print(sign(-4))
# print(sign(0))
# Expected output:
# Positive
# Negative
# Zero
def sign(num):
    if num>0: return 'positive'
    if num<0: return 'negative'
    else: return 'zero'
print(sign(20))


# Question: Write a function power(base, exponent=2) that returns base raised to exponent (default is square).
# Sample data:
# print(power(3))
# print(power(2, 5))
# Expected output:
# 1
# 2
def power(base, exp=2):
    return base**exp

print(power(10,3))

