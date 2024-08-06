# We are going to learn local and global variable in python.
# What is local variable in python?
# A local variable is a variable that is defined inside a function. It is only accessible within that function and is destroyed when the function is completed.

# What is global variable in python?
# In Python, a global variable is a variable that is defined outside of a function or class and is accessible from anywhere in the program. Global variables are shared by all parts of the program, and changes made to a global variable are reflected everywhere.

# Let's see an example of local and global variable in python.
def local_variable_example():
    # This is a local variable
    local_var = 10
    print("Local variable: ", local_var)

# Now let's see how to access local variable outside the function.
# We can't access local variable outside the function because it is destroyed when the function is completed.
# So, we have to return the local variable from the function to access it outside the function.
def local_variable_example():
    # This is a local variable
    local_var = 10
    return local_var
print("Local variable: ", local_variable_example())

# Now let's see an example of global variable in python.
x = 10  # This is a global variable
def global_variable_example():
    # This is a global variable
    global x  # We have to use global keyword to access global variable inside the function.
    x = 20  # We can change the value of global variable inside the function.
    
print("Global variable before function call: ", x)
global_variable_example()
print("Global variable after function call: ", x)  # We can access global variable outside the function.
    
