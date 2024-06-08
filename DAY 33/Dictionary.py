# What is dictionary?
# Dictionary is a collection which is unordered, changeable and indexed.
# Dictionary is a collection of key:value pairs.

# Example:
# In the example below 'name' is the key and 'John' is the value.
thisdict ={
  "name": "John",
  "age": "36",
  "country": "Norway"
}
print(thisdict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Example
print(thisdict["age"])
print(thisdict["name"])
print(thisdict["country"])
# We can access by these values by this methods(It throws an error.).
print(thisdict.get("age"))

# Access values by using loop
for x in thisdict:
  print(thisdict[x])

# Access values by using loop
for x in thisdict:
  print(x)

# Access values by using value()
print(thisdict.values())

# Access items by using item()
print(thisdict.items())
