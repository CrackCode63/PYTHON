# What is Enumerate function?
# Enumerate function is used to iterate over a list and return the index and value of the list 
# Syntax: enumerate(iterable, start=0)
# Example:


list1 = ["apple", "banana", "cherry"]
for i in enumerate(list1):
    print(i)


# Output:
# (0, 'apple')
# (1, 'banana')
# (2, 'cherry')

# Example:

marks = [1,2,3,4,5,6,7,8,9]
index = 0;
for mark in marks:
    print(mark)
    if(index == 3):
        print("At index :3")
    index +=1

# To solve this problem we use Enumerate function

marks = [1,2,3,4,5,6,7,8,9]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("At index :3")