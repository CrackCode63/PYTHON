# We are going to study string meathods in this code.


# We are going to use the string methods to find the length of the string.
a = "abhishek@"
print(len(a))

# Strings are immutable.
# We can not change the value of the string.
# We can only change the value of the string by using the methods.
# We can use the replace method to change the value of the string.


# We are going to use rstrip().
# It takes arguments which we want to remove some character from the end of the string.
# We can say that rstrip() is used to trim trailling characters.
print(a.rstrip("@"))

# We can use lstrip() to remove some character from the start of the string.
# We can say that lstrip() is used to trim leading characters.
print(a.lstrip("a"))

# We are going to use replace()
# It takes two arguments.
# First argument is the character which we want to replace.
# Second argument is the character which we want to replace with.
print(a.replace("a", "A"))

# We are going to use split()
# split() fun is used to split the given string at the specified instance and return the separeted strings as list items.
print(a.split("@"))

# Now, we are using capatalize()
# It is used to convert the first character of the string to upper case.
# This method makes no effect when the first character of the string already capital.
print(a.capitalize())

# We are using center()
# It is used to center the string.
# It takes two arguments.
# First argument is the width of the string.
# Second argument is the character which we want to fill the string.
a1 = print(a.center(40, " "))
# print(len(a1))

# We are using count()
# It is used to count the number of occurences of the character in the string.
print(a.count("a"))

# We are using endswith()
# It is used to check whether the string ends with the specified character or not.
print(a.endswith("@"))
# It takes arguments.
# First argument is the character which we want to check.
# Second argument is the index of the string
print(a.endswith("a", 0, 2))

# We are using find()
# It is used to find the index of the specified character in the string.
# It takes arguments.
# First argument is the character which we want to find.
# Second argument is the index of the string.

print(a.find("a"))
print(a.find("a", 0, 2))


# We are using isalnum()
# It is used to check whether the string is alphanumeric or not.
# It returns True if the string is alphanumeric and False if the string is not alphanumeric.
print(a.isalnum())

# We are using isalpha()
# It is used to check whether the string is alphabetic or not.
# It returns True if the string is alphabetic and False if the string is not alphabetic.
print(a.isalpha())


# We are using islower()
# It is used to check whether the string is in lower case or not.
# It returns True if the string is in lower case and False if the string is not in lower case.
print(a.islower())

# We are using isprintable()
# It is used to check whether the string is printable or not.
# It returns True if the string is printable and False if the string is not printable.
print(a.isprintable())

# We are using isspace()
# It is used to check whether the string is space or not.
# It returns True if the string is space and False if the string is not space.
print(a.isspace())

# We are using istitle()
# It is used to check whether the string is in title case or not.
# It returns True if the string is in title case and False if the string is not in title case.
print(a.istitle())

# We are using startswith()
# It is used to check whether the string starts with the specified character or not.
# It takes arguments.
# First argument is the character which we want to check.
# Second argument is the index of the string.
print(a.startswith("a"))


# We are using swapcase()
# It is used to swap the case of the string.
# It returns the string with swapped case.
print(a.swapcase())

# We are using title()
# It is used to convert the string to title case.
# It returns the string in title case.
print(a.title())


