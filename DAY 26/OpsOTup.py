# Here are going to learn operation on tuples
# Tuples are immutable
# Tuples are ordered
# Tuples are enclosed in parenthesis
# Tuples are used to group together related data
# Tuples are used to represent mathematical sets
# Tuples are used to represent coordinate pairs
# Tuples are used to represent time periods
# Tuples are used to represent ranges of values

# changing a tuple into list
tuple1 = (1, 2, 3, 4, 5)
list1 = list(tuple1)
print(list1)

# aaplying methods to the list
list1.append(6)
print(list1)

#  another method
list1.extend([7, 8, 9])
print(list1)

# Another method
list1.insert(0, 0)
print(list1)

# Changing list into tuple
list1 = tuple(list1)
print(list1)

# This is the way we can make changes in a tuple by converting into a list and applying desired methods on it.
