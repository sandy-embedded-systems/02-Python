#14.Define a constant PI = 3.14159 and calculate the circumference of 
# a circle with radius 5, then print the result.
PI=3.14159
rad=5
print("circumference=",2*PI*rad)
print()

#15.Assign your name, age, and favorite number to variables and display them using an f-string.
name="santhosh"
age=23
fav=0
print(f"My name is {name},i am {age} years old and my fav number is {fav}")
print()

#16.Calculate and print the quotient and remainder of two integers using // and %.
value=390
divisior=5
print("quotient=",value//divisior,"\nremainder=",value%divisior)
print()

#17.Use augmented assignment (+=, -=, *=, /=) on a variable initialized as 10, printing its value at each step.
value=10
value+=10
print("+= ",value)
value-=5
print("-= ",value)
value*=2
print("*= ",value)
value/=5
print("/= ",value)
print()

#18.Assign and print the string Python's "syntax" is easy, properly using escape characters.
s1=""" Python's "syntax" is easy"""
print(s1)
print()

#19.Perform arithmetic (+, *) with boolean values (True, False) and print the results.
print("add:",True+False)
print("mul:",True*False)
print()

#20.Add an integer (5) to a string ("Hello"), observe the error, and explain why it occurs.
x=10
s="hello"
#print(x+s) TypeError:addtion between a number and a character literal is not supported

#21.Assign a very large integer to a variable and print its value and data type.
large=1234567890278572
print(large)
print(type(large))
print()

#22.Assign the same value (100) simultaneously to three variables (a, b, and c), then print each variable.
a=b=c=100
print(a,b,c)
print()

#23.Assign None to a variable, then print its value and type.
var=None
print(var,"  ",type(var))
print()

#24.Perform arithmetic between integer (10) and float (3.5) variables, then print the result and its type.
int_var=10
float_var=3.5
res=int_var+float_var
print("addtion:",res,"   ",type(res))
print()

#25. Slice the string "PythonProgramming" into "Python" and "Programming" separately and print both results.
string="PythonProgramming"
print("part1: ",string[:6])
print("part2: ",string[6:])
print()

