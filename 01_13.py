#1. Assign two integer variables and print their sum, difference, product, and quotient.
var1=20
var2=10
print("sum=",var1+var2)
print("difference=",var1-var2)
print("product=",var1*var2)
print("quotient=",var1/var2)

# 2. Store two float numbers, add them, and print the result rounded to two decimal places
float_1=2.34
float_2=1.75
result=float_1+float_2
print("folat addtion result:",result)
print()

# 3.Concatenate two strings stored in separate variables with a space between them and display.
str1="hello"
str2="world"
concat=str1+ " "+str2
print("concatination:",concat)
print()

# 5.Compare two integers and print boolean results for each comparison 
v1=20
v2=30
print("Boolean results: ",v1==v2,v1!=v2,v1<v2,v1>v2,v1<=v2,v1>=v2)
print()

# 6.Log Session integer, float, string, and boolean variables, and use 
# the type() function to print each data type.
int_var=10
float_var=3.4
str_var="hello"
bool_var=True
print(type(int_var)) 
print(type(float_var)) 
print(type(str_var)) 
print(type(bool_var)) 
print()

#7.Convert a numeric string ("50") to an integer and a float, then print the converted values and their types.
string="1234"
int_var=int(string)
print(type(int_var))
str1="3.456"
float_var=float(str1)
print(type(float_var))
print()

#8.Add an integer (25) and a numeric string ("25") after converting the string explicitly, and print the result.
int_var=25
n_str="25"
print("result=",int_var+int(n_str))
print()

#9.Assign two complex numbers, then print their sum, difference, and product.
z1=complex(1,2)
z2=complex(4,7)
print("sum=",z1+z2)
print("difference=",z1-z2)
print("product=",z1*z2)

#10.Identify valid Python variable names: data1, 1data, _data, data_1, data-1, True, totalSum.
print("data1:true\n1data:false\n_data:true")
print("data_1:true\ndata-1:false\nTrue:false\ntotalSum:true")
#11.Assign "Python", 3.14, and True to variables using a single-line assignment, and print each value.
s1,f1,i1="Python",3.14,33

#12.Swap two variable values in one line and print the values before and after swapping.
a=10
b=20
print("before swap:",a,b)
a,b=b,a
print("after swap:",a,b)

#13.Assign an integer to a variable, then reassign it to a float and string sequentially,
# printing type and value after each step.
x=10
print("x=",x,"   ",type(x))
x=22.4
print("x=",x,"   ",type(x))
x="hello"
print("x=",x,"   ",type(x))
