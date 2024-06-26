# Custom Error in python
# What is custom error?
# Custom error is a user-defined error. It is a class that inherits from the Exception class.
# It is used to raise an error when a specific condition is not met.
# It is also used to raise an error when a specific condition is met.
# How to create a custom error in python?
# To create a custom error in python, you need to create a class that inherits from the Exception.
class CustomError(Exception):
    def __init__(self, message):
         self.message = message
# How to raise a custom error in python?
# To raise a custom error in python, you need to use the raise keyword.
raise CustomError("This is a custom error message")
# How to handle a custom error in python?
# To handle a custom error in python, you need to use the try-except block.
# try:
    # Code that may raise a custom error
# except CustomError as e:
#     # Code to handle the custom error
#     raise Exception("Error")
# # How to create a custom error with a custom message in python?



# raise keyword:
# The raise keyword is used to raise an exception. It is used to raise an exception when a specific condition is not met. It is also used to raise an exception when a specific condition is met. It is used to raise an exception when a specific condition is not met. It is also used to raise an exception when a specific condition is met. 

a = int(input("Enter the no between 1 to 9: "))
if a < 1 or a > 9:
    raise Exception("Invalid Input")
else:
    print("Valid Input")