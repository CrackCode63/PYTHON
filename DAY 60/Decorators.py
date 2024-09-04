# What is Decorators in python
# =====================================
# Decorators are a special kind of function in Python that can modify or extend the behavior of another function without permanently changing the original function.
# They are a powerful tool for implementing design patterns, such as the Singleton pattern, the Factory pattern, and the Observer pattern.
# Decorators are often used to add additional functionality to existing functions, such as logging, authentication, or caching.

# Example of decorators
# ======================
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
    # Example of using the decorator

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
    # Output: Something is happening before the function is called. Hello! Something is happening after the function
