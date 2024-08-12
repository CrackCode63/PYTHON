# Map, filters and Reduce

# Map
# Map is a function that takes in a function and a list as arguments. It applies the function to each element in the list and returns a new list with the results.

# Filter
# Filter is a function that takes in a function and a list as arguments. It applies the function to each element in the list and returns a new list with the elements for which the function returns True.

# Reduce
# Reduce is a function that takes in a function and a list as arguments. It applies the function to the first two elements of the list, then to the result and the next element, and so on, until it has processed all elements in the list.

# Map, Filter and Reduce are all higher-order functions, meaning they take in other functions as arguments.

l = [1,2,3,4,5,6]
newl = [0]*len(l)
for item in range(len(l)):
    newl[item] = l[item]*l[item]

print(newl)

# Another Way
l = [1, 2, 3, 4, 5, 6]
newl = []
for i in range(len(l)):
    newl.append(l[i] * l[i])

print(newl)

# By using map function
l = [1, 2, 3, 4, 5, 6]
newl = list(map(lambda x: x*x, l))
print(newl)

# Now Filter funtion
l = [1, 2, 3, 4, 5, 6]
# Filter function is used to filter out the elements from the list which do not satisfy the given condition
newl = list(filter(lambda x: x%2==0, l))
print(newl)

# Now reduce function
from functools import reduce
l = [1, 2, 3, 4, 5, 6]
# Reduce function is used to apply a rolling computation to sequential pairs of values in a list
# The function takes two arguments and returns a value
newl = reduce(lambda x, y: x+y, l)
print(newl)


