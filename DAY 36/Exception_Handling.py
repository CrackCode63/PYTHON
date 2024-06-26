# We are going to learn about exception handling and error handling.
# We are going to learn exception handling & error handling.
# What is Exception Handling?
# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exception would disrupt the normal operation of a program.

# Exceptions in Python
# Python has many built-in exceptions that raised when your program encountes error (something in the program goes wrong).
# When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

# Python try...except
# try...except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

# Syntax:
# try:

try:
    a = int(input("Enter a number: "))
    print(f"Multiplication table of {a} is: ")
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except:
  print("Invalid Input!")

print("Some imp lines of code")
print("End of program")