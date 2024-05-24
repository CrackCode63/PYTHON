# We are going to study loop in this tut.
# Loop is a sequence of instructions that are executed repeatedly.
# Loop is used to execute a block of code multiple times.
# Loop is used to iterate over a sequence (such as a list or a string).
# Loop is used to iterate over a collection of items.
# Loop is used to iterate over a range of numbers.
# Loop is used to iterate over a file.
# Loop is used to iterate over a directory.
# Loop is used to iterate over a database.
# Loop is used to iterate over a web page.
# Loop is used to iterate over a web service.
# Loop is used to iterate over a web socket.
# 
# There are three types of loops
# 1. For loop
# 2. While loop
# 3. Do while loop

# Now learn about for loops

name = "unnati"
for i in name:
    print(i)


# Loops in list

color = ["Red", "Green", "Blue", "Yellow"]
for babu in color:
    print(babu)
    for bachha in babu:
        print(bachha)

# range() function 
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before
# a specified number.
# Syntax: range(start, stop, step)
# start: The starting value of the sequence. Default is 0.
# stop: The end value of the sequence. This value is exclusive.
# step: The step size. Default is 1.

for k in range(5):
    print(k)

for k in range(1, 10, 2):
    print(k)