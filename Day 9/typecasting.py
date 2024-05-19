# today we learn about typecasting
# what is typecasting in python
# typecasting is the process of converting one data type to another data type.
# typecasting is used to convert one data type to another data type.

a="1"
b="2"
print(a+b)
# here the output is 12 because python is a dynamic language and use a and b as a string not an integer number.
# to solve this problem we have to typecast the string to integer


# typecasting
# after converting a and b in integer we can add them
a=int(a)
b=int(b)
print(a+b)
# we can add a and b by using this
# this print function use a and b as a string and convert it in integers because of int function.
print(int(a)+int(b)) 

# there are two types of typecasting
# 1. implicit typecasting
# 2. explicit typecasting

# what is implicit typecasting
# implicit typecasting is when we don't have to typecast the variable but it is done by the python itself.
# it is depend upon the order of the variable.
# some variable has lower order data type and others have higher order data type.
# in typecasting the order of the variable is important.
# when typecasting the lower order variable converts into higher order variable to prevent loss.

# example
a=1
b=2
print(a+b)
# here the output is 3 because python is a dynamic language and use a and b as a integer not a string.

# what is explicit typecasting
# explicit typecasting is when we have to typecast the variable by ourself
# example
a="1"
b="2"
# here we have to typecast the variable a and b
a=int(a)
b=int(b)
print(a+b)
# here the output is 3 because python is a dynamic language and use a and b as a integer not a string.

