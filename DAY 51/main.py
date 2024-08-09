# We are going to learn seek() and tell()
# seek() is used to move the file pointer to a specific location in the file
# tell() is used to get the current location of the file pointer

# Let's create a file and write some data into it
file = open("test.txt", "w")
file.write("Hello, World!")
file.close()
# Now, let's open the file and use seek() and tell() functions
file = open("test.txt", "r+")
file.seek(0)  # Move the file pointer to the beginning of the file
print(file.tell())  # Get the current location of the file pointer
# Output: 0

# Now, let's move the file pointer to the 7th character in the file
file.seek(7)
print(file.tell())  # Get the current location of the file pointer
# Output: 7

# Now, let's read the file from the current location of the file pointer
print(file.read(1))  # Read 1 character from the file
# Output: W
# Now, let's close the file
file.close()
