# In this code, We are going to perform some operation on strings.
# We are going to use the string methods to perform the operations.
# Examples.

name = "ABHISHEK"

# we are perform slicing on string
print(name[0:3]); #It start slicing from index 0 to 2. It doesn't include 3. 
# prints the first three characters of the string.
print(name[0:5]); 
# prints the first five characters of the string.
print(name[0:-3]) # Here -3 represent string lenght-3 = 5
# prints the first five characters of the string.
# This can be written as:
print(name[:5]) # prints the first five characters of the string.
# And
print(name[:len(name) - 3]) #The output of this line same as above.
print(name[-3:-3])


# Here are some basic methods of strings.
print(name.upper()); 
# This will print the string in upper case.
print(name.lower()); 
# This will print the string in lower case.

