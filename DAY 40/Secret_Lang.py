import string
import random

# Function to transform the string by removing the first letter and appending it to the end
def transform_string(s):
    return s[1:] + s[0]

# Function to generate random string of specified length
def random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def game(a):
    print("The string is:", transform_string(a))

# Input message
a = input("Enter the message: ")

if len(a) < 3:
    print(a[::-1])  # Reverse the string if it has less than 3 letters
else:
    transformed = transform_string(a)
    random_prefix = random_string(3)
    random_suffix = random_string(3)
    encrypted_message = random_prefix + transformed + random_suffix
    print("Encrypted message:", encrypted_message)