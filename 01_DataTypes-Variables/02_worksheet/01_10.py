#1.Given the assignment a = b = 10, what happens if you later set b = 20?
# What is the value of a? Explain why.
a=b=10
b=20
print(a,b) #the assignment happens in the first line itself, so two different variable
print()

#2.What will be the output and the type of each variable?Explain your answer
x = 2
print(type(x))
y = 2.0
print(type(y))
z = "2"
print(type(z))
w = x + int(z)
print(type(w))
v = str(x) + z
print(type(v))
print()

#3.What is the difference between mutable and immutable data types in Python?
# Name three types from each category.

#4.Given x = [1, 2, 3] and y = x, then x[0] = 9. What are the values of x and y? Explain the behavior.
x=[1,2,3]
y=x
print(x)
print(y)
print() #here x and y are list data type, they are mutable. when we use print() on list, it prints all values 
        # along with the square brackets

#5.How does Python treat variable names that have the same value but are of different data types?
#For example, what is the result of 3 == 3.0 and 3 is 3.0?
print(3==3.0) #when using '==' operator, python checks values not the data types,so ths results in True
print(3 is 3.0) # here 'is' checks the object identity not the values, so this is false because
                # 3 is int and 3.0 is float
print()

#6.What is the result of the following code? Explain your answer.
a = (5)
b = (5,)
print(type(a)) #here a is an integer, because (5) is == 5
print(type(b)) #here b is touple because, (5,) is!= 5. 
print()

#7.What happens if you try to use a list as a dictionary key? Why?
# dictionary={ 
#     [1,2,3]:"Hello"
# }     # this result in TypeError: because dict only allows hashable key, but list is a mutable .
        # so python prevents keys from changing once they are confirmed.

#8. What is the difference between None, 0, False, and "" in Python? Are they the same or different as variables? 
# How does Python treat them in conditional statements?
 
#9. Does Python automatically convert between integer and float types? Show a code example and explain what happens.
i=10
f=2.4
res=i+f
print(res,"  ",type(res))
print()

#10.What will be the output and types in this code?
a = "5"
b = 5
c = a * b
d = b * a
print(c, d) # o/p:55555 55555
            # because in python, is a string multiplied with an integer, the result is nothing but the same
            # string but repeated given no.of times.but add or subtract results in error
