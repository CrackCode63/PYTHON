questions = [
    ["Which language is used to create fb?", "Python" , "Java" , "C++" , "C" , "C#"  , "None"],

    ["Which language is used to create google?", "Python" , "Java" , "C++" , "C" , "C#"  , "None"], 

    ["Which language is used to create BGMI?", "Python" , "Java" , "C++" , "C" , "C#"  , "None"],

    ["Which language is used to create Flappy Bird?", "Python" , "Java" , "C++" , "C" , "C#"  , "None"]
             ]

levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000]

for i in range(0,len(questions) ):
    question   = questions[i]
    print(f"Questions for Rs. {levels[i]}")
    print(f"a.{questions[1]}     b.{question[2]}")
    print(f"c.{questions[3]}     d.{question[4]}")

    reply = int(input("Enter your answer(1-4)"))
    if reply == questions[-1]:
        print("Correct you won {levels[i]}")
    else:
        print("Wrong answer you lost ")
        break 