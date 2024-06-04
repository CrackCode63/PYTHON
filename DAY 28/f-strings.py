# What is f-strings?
# f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

# It is also possible to use the format method.
# The format method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
name = "John"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
