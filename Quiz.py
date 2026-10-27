#This is a simple interactive quiz game
import time
Questions=["How many moons does Jupiter have?",
           "What is the percentage of Nitrogen in air?",
           "What is the largest sea mammal?",
           "What is the chemical formula of table salt?"]

Options=['A.65  B.89  C.115  D.124',
         'A.54%  B.68%  C.78%  D.97%',
         'A.Blue Whale  B.Star fish  C.Shark  D.Octopus',
         'A.KCl  B.NaCl  C.NaOH  D.None of the above']

Answers=["C","C","A","B"]

Guesses=[]
score=0
question_num= 0

for question in Questions:
  print("------------------------------------------------------------")
  print(question)
  for option in Options:
    print(Options[question_num])
    guess=input("Enter the option (A,B,C,D): ").upper()
    Guesses.append(guess)
    if guess==Answers[question_num]:
        score +=1
        print("CORRECT")
        break
    else:
        print(f"INCORRECT, {Answers[question_num]} is the correct answer")
        break
  time.sleep(2)
  question_num=question_num+1

print(f"Answers: {Answers}")
print(f"Guesses: {Guesses}")
total=(score/len(Questions))*100
print(f"You are {total}% accurate")




