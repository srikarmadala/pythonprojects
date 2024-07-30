rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n")
)

comp_choice = random.randint(0, 2)
print(f"You choose {choice}")
game = [choice, comp_choice]
if game[0] == game[1]:
    print(f"Draw!\nComputer choose {comp_choice}")
elif game[0] == 0 and game[1] == 1:
    print(f"{rock}\nComputer choose\n{paper}\n You lost")
elif game[0] == 0 and game[1] == 2:
    print(f"{rock}\nComputer choose {comp_choice}\n{scissors}\n You won")
elif game[0] == 1 and game[1] == 0:
    print(f"{paper}\nComputer choose {comp_choice}\n{rock}\n You won")
elif game[0] == 1 and game[1] == 2:
    print(f"{paper}\nComputer choose {comp_choice}\n{scissors}\n You lost")
elif game[0] == 2 and game[1] == 1:
    print(f"{scissors}\nComputer choose {comp_choice}\n{paper}\n You won")
elif game[0] == 2 and game[1] == 0:
    print(f"{scissors}\nComputer choose {comp_choice}\n{rock}\n You lost")
else:
    print("You typed invalid number, you lose!")

