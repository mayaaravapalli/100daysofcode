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

choices = [rock, paper, scissors] 

user_choice = input("what do you choose? 0 for rock, 1 for paper, 2 for scissors: ")
user_choice = int(user_choice)
computer_choice = random.randint(0, len(choices)-1)
if user_choice > 2:
  print("Your choice is out of range. You lose.")
else:
  print(f'''User Choice: {choices[user_choice]}
        Computer Choice: {choices[computer_choice]}''')

if user_choice == computer_choice:
  print("its a draw")
elif user_choice == 0 and computer_choice == 2:
  print("rock beats scissors, you win")
elif user_choice == 2 and computer_choice == 0:
  print("rock beats scissors, you lose")
elif user_choice == 1 and computer_choice == 2: 
  print("scissors beats paper, you lose")
elif user_choice == 2 and computer_choice == 1: 
  print("scissors beats paper, you win")
elif user_choice == 1 and computer_choice == 0:
  print("paper beats rock, you win")
elif user_choice == 0 and computer_choice == 1:
  print("paper beats rock, you lose")