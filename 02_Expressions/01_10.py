#1.Calculate the Square of a Number
#Write an expression to calculate the square of a number.
#Sample Input: n = 7
num=int(input("Enter an integer:"))
print("square=",num**2)
print()

#2.Evaluate a Quadratic Expression
#Given values for x, a, b, and c, write an expression to compute ax² + bx + c.
#Sample Input: a = 2, b = 3, c = 4, x = 5
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
x=int(input("Enter x:"))
result=a*x**2 +b*x +c
print(result)
print()

#3.Find the Remainder (Modulo Operation)
# Write an expression to get the remainder when one number is divided by another.
# Sample Input: num = 29, divisor = 6
num=int(input("Enter number:"))
divisor=int(input("Enter divisor:"))
print("remainder=",num%divisor)
print()

#4.Check if a Number is Positive, Negative, or Zero (Conditional Expression)
# Use a single line expression to print whether a number is positive, negative, or zero.
# Sample Input: num = -8
num=int(input("Enter a number:"))
if num<0:
    print("Negative")
elif num==0:
    print("Zero")
else:
    print("positive")
print()

# 5.Get the Absolute Value
# Write an expression to get the absolute value of a number.
# Sample Input: n = -12
num=int(input("Enter a number:"))
print(abs(num))
print()

# 6.Swap Two Numbers Without Using a Third Variable
# Swap two variables’ values using a single line of code.
# Sample Input: a = 15, b = 8
print("before swap:" ,a,b)
a,b=b,a
print("after swap:",a,b)
print()

#7. Calculate the Average of Three Numbers
# Write an expression to find the average of three numbers.
# Sample Input: x = 5, y = 8, z = 10
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
print("arv=",(a+b+c)/3)
print()

#8. Use the Ternary Operator to Find the Minimum of Two Numbers
# Use a single expression to find the smaller of two numbers.
# Sample Input: a = 20, b = 13
print("min=",a if a<b else b)
print()

# 9.Bitwise OR and XOR
# Write expressions to calculate the result of bitwise OR and bitwise XOR between two numbers.
# Sample Input: x = 9, y = 5
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(a|b)
print(a^b)

# 10.Check if a Number is Divisible by Both 2 and 3
# Write a single expression that evaluates to True if a number is divisible by both 2 and 3, otherwise False.
# Sample Input: num = 18
num=int(input("Enter a number:"))
res=True if num%2 ==0 and num%3==0 else False
print(res)
