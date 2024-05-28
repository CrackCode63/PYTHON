# We are going to learn about function arguments
# Arguments are the values that are passed into a function
# We can pass in as many arguments as we want
# We can also pass in no arguments at all
# We can also pass in a variable number of arguments

def average(a,b):
    print("The average is:",(a+b)/2)

average(2,2)

# What is default arguments?
# Default arguments are arguments that have a default value
# If we don't pass in a value for the argument, the default value will be used
# We can have as many default arguments as we want
# We can also have a mix of required and default arguments
def average(a,b=0):
    print("The average is:",(a+b)/2)
average(a = 1)

# What is keyword arguments?
# Keyword arguments are arguments that are passed in using the keyword name
# We can have as many keyword arguments as we want
# We can also have a mix of required and keyword arguments
 


