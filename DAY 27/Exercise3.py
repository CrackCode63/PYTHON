# We are creating kaun banega crorepati game.

print("We are going to play Kaun Banega Crorepati")
prizes = [1, 2, 5, 10]  # List of prizes for each question (in rupees)
questions = ["2+2", "3+3", "4+4", "5+5"]  # List of questions

current_question = 0
winning_amount = 0

for question in questions:
  print(question)
  answer = eval(question.split('+')[0]) + eval(question.split('+')[1])
  user_answer = int(input("Enter your answer: "))
  if user_answer == answer:
    winning_amount = prizes[current_question]  # Update winning amount
    print("Correct! You have won", winning_amount, "Rupees")
    current_question += 1  # Move to next question (optional)
  else:
    print("You lose. You won", winning_amount, "Rupees")
    break  # Exit the loop after a wrong answer (optional)

    
