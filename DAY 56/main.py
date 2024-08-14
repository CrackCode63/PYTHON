import random

my_list = ['snake','water','gun']
random_item = random.choice(my_list)
print("Lets play snake, water and gun game.")
print("Enter 1 for snake:")
print("Enter 2 for water:")
print("Enter 3 for gun:")
print('Enter your choice for the person:')
choice = int(input())
print('Computer choice is: ',random_item)
if choice == 1:
    user_choice = "snake"
elif choice == 2:
    user_choice = "water"
elif choice == 3:
    user_choice = "gun"
else:
    print("Invalid choice")

print("Your choice ",user_choice)
if user_choice == random_item:
        print("It's a tie!")
elif(user_choice == 'snake' and random_item == 'water') or \
    (user_choice == 'water' and random_item == 'gun') or \
    (user_choice == 'gun' and random_item == 'snake'):
        print("You win!")
else:
        print("Computer wins!")



# print(random_item)

