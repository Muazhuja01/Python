import random

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

choice = input("Welcome to the rock paper scissors championship. What do you choose?\n"
               "   Choose 1 for rock, 2 for paper, 3 for scissors\n    ")
computers_choice = random.randint(1,3)

if choice == "1":
    print(f"You chose: {rock}")
    if computers_choice == 1:
        print(f"Computer chose: {rock}\nDraw")
    if computers_choice == 2:
        print(f"Computer chose: {paper}\nYou Lose!")
    if computers_choice == 3:
        print(f"Computer chose: {scissors}\nYou Win!")
elif choice == "2":
    print(f"You chose: {paper}")
    if computers_choice == 1:
        print(f"Computer chose: {rock}\nYou Win!")
    if computers_choice == 2:
        print(f"Computer chose: {paper}\nDraw")
    if computers_choice == 3:
        print(f"Computer chose: {scissors}\nYou Lose!")
elif choice == "3":
    print(f"You chose: {scissors}")
    if computers_choice == 1:
        print(f"Computer chose: {rock}\nYou Lose!")
    if computers_choice == 2:
        print(f"Computer chose: {paper}\nYou Win!")
    if computers_choice == 3:
        print(f"Computer chose: {scissors}\nDraw")