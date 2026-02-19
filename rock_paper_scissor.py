import random
print("Welcome to rock Paper Scissors!")
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
user_choice = int(input("Enter your choice: 1 for rock, 2 for paper, 3 for scissors:\n"))
if user_choice == 1:
    print(f"You have chosen rock {rock}")
elif user_choice == 2:
    print(f"You have chosen paper {paper}")
elif user_choice == 3:
    print(f"You have chosen scissors {scissors}")
else:
    print("Invalid choice. You loose.")

computer_choice = random.randint(1, 3)
if computer_choice == 1:
    print(f"Computer has chosen rock {rock}")
elif computer_choice == 2:
    print(f"Computer has chosen paper {paper}")
else:
    print(f"Computer has chosen scissors {scissors}")

if user_choice < 0 or user_choice >= 4:
    print("Wrong entry. You lose.")
elif user_choice == 1 and computer_choice == 3:
    print("You win.")
elif computer_choice == 1  and user_choice == 3:
    print("You lose.")
elif user_choice > computer_choice:
    print("You win.")
elif computer_choice > user_choice:
    print("You lose.")
elif user_choice == computer_choice:
    print("It is a draw.")




