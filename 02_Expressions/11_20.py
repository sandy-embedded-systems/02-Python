#1. Find the Largest of Three Numbers Using Only Expressions
# Without using if, elif, or any function, write an expression to find the largest of three given numbers.
# Sample Input: a = 14, b = 27, c = 19
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
res=a if (a>=b and a>=c) else (b if b>=c else c)
print("Largest=",res)
print()

# 2.Check if a Number is a Power of Two
# Write a single Boolean expression to check if a number is a power of two.
# Sample Input: n = 32
num=int(input("Enter a number:"))
exp= True if (num & num-1) else False
print(exp)
print()

# 3. Find the Second Largest of Three Numbers
# Write an expression (no functions, no if) to get the second largest value among three numbers.
# Sample Input: a = 20, b = 12, c = 18
second = (
    (a if a < b else b) if (a if a < b else b) > c
    else (c if c < (a if a > b else b) else (a if a > b else b))
)
print(second)
print()

# 4. Toggle a Specific Bit in an Integer
# Given a number and a bit position, write an expression to toggle (flip) that bit.
# Sample Input: n = 12, bit_position = 2
num=int(input("Enter a number:"))
bit_pos=int(input("Enter bit position to toggle:"))
num^=1<<bit_pos
print("number after toggle:",num)
print()
# 5.Count the Number of 1 Bits in an Integer (No Loops)
# Write an expression (using built-in functions) to count how many 1s are in the binary representation of a number.
# Sample Input: n = 29
num=int(input("Enter a number:"))
print("No.of set bits:",num.bit_count())
print()

# 6. Find the Sign of a Number as -1, 0, or 1 (Using Only Expressions)
# Write a single expression that gives -1 for negative numbers, 0 for zero, and 1 for positive numbers.
# Sample Input: n = -56
num=int(input("Enter a number:"))
res= -1 if num<0 else ( 0 if num==0 else 1)
print(res)
print()

#7. Check If a Number is a Multiple of 4 but Not of 8
# Write an expression that is True only if a number is divisible by 4 but not by 8.
# Sample Input: n = 12
num=int(input("Enter a number:"))
res= True if num%4==0 and num%8 !=0 else False
print(res)
print()

# 8.Rotate Bits Left by k Positions
# Given a number (assume 8 bits) and a value k, write an expression to rotate its bits to the left by k positions.
# Sample Input: n = 150, k = 2
num=int(input("Enter a number:"))
k=int(input("Enter no.of rotations:"))
print("before rotation:",bin(num))
num= ((num<<k)|(num>>(32-k)))&0xFFFFFFFF
print("after rotation:",bin(int(num)))
print()

# 9. Find the Difference Between the Largest and Smallest of Three Numbers (Using Only Expressions)
# Write an expression to find the difference between the largest and the smallest of three numbers.
# Sample Input: a = 8, b = 27, c = 14
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
large= a if a>=b and a>=c else ( b if b>=c else c)
small = a if a<=b and a<=c else (b if b<=c else c)
print("difference:",large-small)
print()

#10. Set the nth Bit of a Number
# Write an expression that sets the nth bit of a given integer to 1 (leave other bits unchanged).
# Sample Input: n = 9, bit_position = 3
num=int(input("Enter a number:"))
bit_pos=int(input("Enter bit position:"))
num|=1<<bit_pos
print(num)
print()
