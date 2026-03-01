#11. Can variable names start with an underscore (_) or contain special characters like $ or @? Explain the rules.

# A variable name may contains:
# letters (a-z) ,(A-Z)
# Digits (not first)
# Underscore	
# No Special characters	
# No Starting with digit	
# NO Keyword names	
# Case sensitive

#12. What is the difference between single quotes ('), double quotes ("), and triple quotes (''' or """) for strings?
# Are they the same data type?

# All of them create same data type,i.e, str type
# they helps us in avoiding escape sequence requirements

#13.Explain the difference between an empty list [], an empty tuple (), and an empty dictionary {} in
# terms of their types and mutability.

#14. Given the code: What is the value of y and why?
x = [1, 2, 3]
y = x
x = [4, 5, 6]
print(y) # y =[ 1,2,3] ,same as x before modifying
print()

#15. How does variable assignment differ between mutable and immutable objects? Illustrate with an example.

#16.Explain what happens here:
#Why might this print False?
x = 1000
y = 1000
print(x is y) # 0
print()

#17. How do you convert between data types (e.g., string to int, int to float, list to tuple) in Python? 
#Show a code example.
value=int("12345") # this can be done by using explicit typecasting
f=float(2)
t=tuple([1,2,3,4])

#18. What will be printed?Why?
x = "10"
y = 2
print(x * y) #1010
print(y * x) #1010   reason:In python, a string can be multiplied with integer to make it repeatedly

#18. Is type(5) == int always True? Is isinstance(5, int) always True? Explain the difference.
print(type(5)==int) # this will check the exact type equality,not subclass relation
print(isinstance(5,int)) # this will check ,instanst of a class or it's subclass relation when inherited
print()

#19. Can a Python variable change its data type after assignment? Give an example and explain the implications.
x=10 #here it is int
x=10.4 #here it is float
x="hello" #here it is str   so, variable in python don't have fixed types, this proves
          # Python is dynamically typed
          