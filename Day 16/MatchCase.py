# We are going to study about match case statement.
# It is used to match the value of a variable with a set of values.

x = int(input("enter the value of x: "))
match x:
    case 0:
        print("Zero")
    case 4:
        print("Four")
    case _:
        print("Something else and the value is:",x)
