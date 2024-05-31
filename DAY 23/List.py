# Here, we are going to learn about list

# List is a collection of items
# List is mutable
# List is ordered
# List is indexed
# List is iterable
# List is sequence


l = [3,4,5,6,7] # List items are seperated by commas and enclosed within sqare brackets
# The items of list might be have different data types.
print(l)
print(type(l))

# We can access each item by their index
print(l[0])
print(l[2])
print(l[3])
print(l[4])

# Can we add a new item to the above list 

l.append(8)
print(l)


# Check wheather the given item is in the list or not

x = int(input("Enter the no. : " ))

if x in l:
    print("Yes, the number is in the list")
else:
    print("No, the number is not in the list")

# Now, we are going to learn about slicing
# Slicing is a way to extract a subset of items from a list
# Slicing is done by using colon operator

print(l[:]) # This line print all the list items.
print(l[0:2]) # This line print the first two items of the list.
print(l[2:]) # This line print the items from 2nd index to the last index

# Negative Indexing
print(l[-1]) # This line print the last item of the list.
print(l[-2]) # This line print the second last item of the list.
print(l[-3]) # This line print the third last item of the list.

# Slicing with jump index
print(l[0:4:2]) # This line print the first four items of the list by escaping the one list item
print(l[0:4:3]) # This line print the first four items of the list by escaping the two list item

# List comprehension
# List comprehension is a way to create a list by using a for loop and if condition
# List comprehension is a one liner code to create a list

list = [i for i in range(4) ]
print(list)
