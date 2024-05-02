# today we learn about how to take user input in pyhton
# we can take user input in python using input() function

# syntax:
# input()
# this function will take user input and store it in a variable and returns value as a string and character.

# example:

name = input("enter your name: ") 
print("your name is: ", name)

# as we see input function returns value as a string and character.
# if we want to take input as a number we have to convert it into a number.
# example:

age = int(input("enter your age: "))
print("your age is: ", age)

# we can also take multiple input from user using input() function.
# example:

name, age = input("enter your name and age: ").split()
print("your name is: ", name)
print("your age is: ", age)

# in the above line we use split( function to split the string into a list.
# we can also use split() function to split the string into a list.
# example:

name, age = input("enter your name and age: ").split(",")
print("your name is: ", name)
print("your age is: ", age)