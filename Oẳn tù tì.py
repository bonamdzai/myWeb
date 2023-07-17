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
import random
choose = input("You choose? Rock or Paper or Scissors?\n")
if choose.lower() == "rock" or choose.lower() == "paper" or choose.lower() == "scissors":
    list = [rock, paper, scissors]
    computer = random.choice(list)
    print(computer)
else:
    print("Invalid. You lose!")
