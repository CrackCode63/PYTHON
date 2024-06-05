# What is recursion in python?
# Recursion is a process (a function) that calls itself.
# Recursion is a way of programming or solving a problem.
# The most common real-world example of recursion is the Fibonacci sequence.
# Each number in the sequence is the sum of the two preceding numbers.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
# The Fibonacci sequence is often used as an example of recursion.
# The Fibonacci sequence is defined as follows:
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# This sequence adds up to the Fibonacci number.
# The Fibonacci sequence is a series of numbers.
# Each subsequent number is the sum of the previous two.
# The first two numbers in the Fibonacci sequence are 0 and 1.
# Program for the Fibonacci sequence or recursion in Python.
def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n - 1) + fibo(n - 2)
    

print(fibo(10))

# Now, We have to calculate factorial using recursion.
# Factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120
# Factorial of 0 is 1.(By definition)
# Factorial of negative number cannot be computed.
# Factorial is not defined for non-integer values.
# Factorial of a non-integer value is not defined.
def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n * factorial(n-1)

x = int(input("Enter the number: "))
print(factorial(x))
   
