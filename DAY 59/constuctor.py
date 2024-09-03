# What is constructor in python?
# =====================================
# A constructor in Python is a special method that is automatically called when an object of a class is instantiated
# It is used to initialize the attributes of the class.
# It is defined with the __init__ method.
# The __init__ method is a special method in Python classes known as a constructor. It is automatically called when an object of a class is instantiated.
# Example of constructor:
class Student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
        # =====================================
        # Here, name, age, rollno are the parameters of the constructor and self is a
        # reference to the current instance of the class and is used to access variables and methods from the
        # class.
        # =====================================
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Roll No: ", self.rollno)
            # =====================================
            # Here, display is a method of the class Student and self is a reference to the current
            # instance of the class and is used to access variables and methods from the class.
            # =====================================
        display(self)
            # =====================================
            # Here, we are calling the display method from the constructor.
            # This is not a good practice as it can lead to infinite recursion.
            # =====================================
            # Creating an object of the class Student


