# What is string?
#  String is a sequence of character that enclosed within the double quotes.
#  String is immutable, it means we can not change the value of string.
# It ends with the null character.
name = "abhi"
print(name)

fruit = '''He said, 
Hi Abhi
"I want to eat banana"'''
print(fruit)
# This is used to print multiline string.

# Accessing the character of a string by its index
#  The index of a string starts with 0.
#  The last index of a string is (length of string - 1).
#  If we try to access the character of a string by its index which is out of range then it will give an error.
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# This is not a profession way to accessing every character of a string.
#  We can use for loop to access every character of a string.
for a in name:
    print(a)

# We will discuss about loops in further tutorials.
