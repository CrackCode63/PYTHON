# finally keyword:
# it is used to execute the code block after the try and except block.
# it is used to execute the code block even if the try and except block fails.

try:
    l = [1,2,3,4,5,6]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Index out of range")
finally:
    print("This is finally block") # this line execute at any cost.
