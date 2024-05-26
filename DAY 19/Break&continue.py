# We are going to learn about break and continue statements
# break statement is used to exit the loop
# Example:

for i in range(10):
    if i == 10:
        break
    print("5 * ",i+1," = ",5 * (i+1))

print("\n")

# continue statement is used to skip the current iteration and continue with the next iteration

for i in range(12):
    if i == 10:
        continue
    print("5 * ",i+1," = ",5 * (i+1))
