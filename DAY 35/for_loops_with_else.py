# We are going to learn how a else used with for loops
# We can use it with while loops
# We can use it with if statements

# Example:

for i in range(5):
    print(i)
else:
    print("sorry!") # Here else is executed because of the last iteration of the loop is processed.


# Another Example:

for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("sorry!") # This part is not executed means that the above loop is break or terminated before completing.

# In this example else is not executed beacuse of the loop does not run completely.
# The execution of else tells us that the loop runs completely.
