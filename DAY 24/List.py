# We are going to learn list
# List is a collection of items
# List is mutable
# List is ordered
# List is indexed
# List is iterable
# List is sequence

# list methods

# append() - add an item to the end of the list
# clear() - remove all items from the list
# copy() - returns a copy of the list
# count() - returns the number of items in the list with the specified value
# extend() - add all items of a list into the current list, to the end of the
# current list
# index() - returns the index of the first item with the specified value
# insert() - adds an item at the specified position
# pop() - removes the item at the specified position
# remove() - removes the item with the specified value
# reverse() - reverses the order of the list
# sort() - sorts the list

# Example
my_list = [1, 2, 3, 4, 5]
# Applying all methods to this list
my_list.append(6)
print(my_list)
my_list.clear()
print(my_list)
my_list.copy()
print(my_list)
my_list.count(1)
print(my_list)
my_list.extend([1, 2, 3])
print(my_list)
my_list.index(1)
print(my_list)
my_list.insert(0, 0)
print(my_list)
my_list.pop(2)
my_list.sort()
print(my_list)