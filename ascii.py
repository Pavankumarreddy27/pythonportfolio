import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
user_choice = int(input("type 0 for rock or type 1 for paper or type 2 for scissors? "))
print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0 :
    print("you selected a wrong number")
elif computer_choice == user_choice :
    print('match draw')
elif user_choice == 0 and computer_choice == 2:
    print("you wins")
elif user_choice == 2 and computer_choice == 0:
    print("you loose")
elif computer_choice > user_choice:
    print("you lose")     
elif user_choice > computer_choice:
    print("you wins")    