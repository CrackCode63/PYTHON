# We are dicussing about the sets methods
# There are two types of sets
# 1. Mutable
# 2. Immutable

# Following methods on the sets
# 1. union()
# 2. update()
# 3. intersection()
# 4. intersection_update()
# 5. symmetric_difference()
# 6. symmetric_difference_update()
# 7. difference()
# 8. difference_update()
# 9. isdisjoint()
# 10. issuperset()
# 11. issubset()
# 12. add()
# 13. remove()
# 14. discard()
# 15. pop()
# 16. del()
# 17. clear()

# 1. union()
# The union() method returns a new set with all items from both sets.
# The union() method does not remove any duplicates in the new set.
# The union() method can be used to combine two sets.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a.union(b)
print(c)
# Output:
# {1, 2, 3, 4, 5, 6, 7, 8}

# 2. update()
# The update() method inserts the items in set2 into set1.
# The update() method does not return a new set of items.
# The update() method can be used to add one set to another.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.update(b)
print(a)
# Output:
# {1, 2, 3, 4, 5, 6, 7, 8}

# 3. intersection()
# The intersection() method returns a new set with only items that are present in both sets.
# The intersection() method does not remove any duplicates in the new set.
# The intersection() method can be used to find the common items in two sets.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a.intersection(b)
print(c)
# Output:
# {4, 5}

# 4. intersection_update()
# The intersection_update() method inserts the items in set2 into set1.
# The intersection_update() method removes any items that are not present in both sets.
# The intersection_update() method does not return a new set of items.
# The intersection_update() method can be used to find the common items in two sets.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.intersection_update(b)
print(a)
# Output:
# {4, 5}

# 5. symmetric_difference()
# The symmetric_difference() method returns a new set with items that are not present in both sets.
# The symmetric_difference() method does not remove any duplicates in the new set.
# The symmetric_difference() method can be used to find the items that are not common in two sets.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a.symmetric_difference(b)
print(c)
# Output:
# {1, 2, 3, 6, 7, 8}

# 6. symmetric_difference_update()
# The symmetric_difference_update() method inserts the items in set2 into set1.
# The symmetric_difference_update() method removes any items that are not present in both sets.
# The symmetric_difference_update() method does not return a new set of items.
# The symmetric_difference_update() method can be used to find the items that are not common in two sets.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.symmetric_difference_update(b)
print(a)
# Output:
# {1, 2, 3, 6, 7, 8}

# 7. difference()
# The difference() method returns a new set with items that are only present in the original set.
# The difference() method does not remove any duplicates in the new set.
# The difference() method can be used to find the items that are only present in the first set.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a.difference(b)
print(c)
# Output:
# {1, 2, 3}

# 8. difference_update()
# The difference_update() method removes the items that are present in both sets.
# The difference_update() method does not return a new set of items.
# The difference_update() method can be used to find the items that are only present in the first set.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.difference_update(b)
print(a)
# Output:
# {1, 2, 3}

# 9. isdisjoint()
# The isdisjoint() method returns True if two sets have a null intersection.
# The isdisjoint() method returns False if two sets have at least one common item.
# The isdisjoint() method can be used to check if two sets have any items in common.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a.isdisjoint(b)
print(c)
# Output:
# False

# 10. issuperset()
# The issuperset() method returns True if all items in the specified set are present in the original set.
# The issuperset() method returns False if items are not present.
# The issuperset() method can be used to check if all items in a set are present in another set.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5}
c = a.issuperset(b)
print(c)
# Output:
# True

# 11. issubset()
# The issubset() method returns True if all items in the original set are present in the specified set.
# The issubset() method returns False if items are not present.
# The issubset() method can be used to check if all items in a set are present in another set.
# Example:
a = {1, 2, 3, 4, 5}
b = {4, 5}
c = a.issubset(b)
print(c)
# Output:
# True

# 12. add()
# The add() method adds an item to a set.
# The add() method can be used to add one item to a set.
# Example:
a = {1, 2, 3, 4, 5}
a.add(6)
print(a)
# Output:
# {1, 2, 3, 4, 5, 6}

# 13. remove()
# The remove() method removes an item from a set.
# The remove() method can be used to remove one item from a set.
# Example:
a = {1, 2, 3, 4, 5}
a.remove(3)
print(a)
# Output:
# {1, 2, 4, 5}

# 14. discard()
# The discard() method removes an item from a set if it is present in the set.
# The discard() method does not raise an error if the item is not present in the set.
# The discard() method can be used to remove one item from a set.
# Example:
a = {1, 2, 3, 4, 5}
a.discard(3)
print(a)
# Output:
# {1, 2, 4, 5}

# 15. pop()
# The pop() method removes an item from a set.
# The pop() method can be used to remove one item from a set.
# Example:
a = {1, 2, 3, 4, 5}
a.pop()
print(a)
# Output:
# {1, 2, 3, 4}

# 16. del()
# The del() method removes the specified item from a set.
# The del() method can be used to remove one item from a set.
# Example:
a = {1, 2, 3, 4, 5}
del a
print(a)
# Output:
# NameError: name 'a' is not defined

# 17. clear()
# The clear() method removes all items from a set.
# The clear() method can be used to remove all items from a set.
# Example:
a = {1, 2, 3, 4, 5}
a.clear()
print(a)
# Output:
# set()



