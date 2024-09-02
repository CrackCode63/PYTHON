# Classes and Objects in py
# Classes are templates for creating objects. They define the properties and methods of an object.
# Objects are instances of classes and have their own set of attributes (data) and methods (functions that operate on that data).
# In Python, we can define a class using the class keyword.

class Person:
    name = "Abhi"
    age = 25
    # The above code defines a class called Person with two attributes: name and age.
    # These attributes are shared by all instances of the class.

a = Person()
# The above code creates an object called a of the class Person.
print(a.name)  # Outputs: Abhi
print(a.age)   # Outputs: 25

a.name = "Aman"
a.age = 32
# The above code changes the name and age of the object a to "Aman" and 32 respectively.
print(a.name)  # Outputs: Aman
print(a.age)   # Outputs: 32
