import random

game = ["ROCK","PAPER","SCISSOR"]

# while True:
#     original = random.choice(game)
#     user = input("Enter your choice between Rock, Paper and Scissor! Type exit to leave!")
#     user = user.upper()
#     if user == "EXIT":
#         print("Thank You !!!")
#         break
#     elif user == original:
#         print(f"{user} against {original} ! Hence it's a draw!!!")
#     elif user == "ROCK":
#         if(original == "SCISSOR"):
#             print(f"{user} won against {original}! You Won!!!")
#         else:
#             print(f"{user} lost against {original}! You Lost!!!")
#     elif user == "SCISSOR":
#         if(original == "PAPER"):
#             print(f"{user} won against {original}! You Won!!!")
#         else:
#             print(f"{user} lost against {original}! You Lost!!!")
#     elif user == "PAPER":
#         if(original == "ROCK"):
#             print(f"{user} won against {original}! You Won!!!")
#         else:
#             print(f"{user} lost against {original}! You Lost!!!")
#     elif user == "EXIT":
#         print("Thank You !!!")
#         break
#     else:
#         print("Invalid choice!!!")



# A More Simpler & Organized Way!
while True:
    original = random.choice(game)  # Moved inside the loop
    user = input("Enter your choice between Rock, Paper and Scissor! Type exit to leave: ")
    user = user.upper()

    if user == "EXIT":
        break
    elif user not in game:
        print("Invalid choice!!!")
        continue

    print(f"You chose {user}, computer chose {original}.")

    if user == original:
        print("It's a draw!!!")
    elif (user == "ROCK" and original == "SCISSOR") or \
         (user == "PAPER" and original == "ROCK") or \
         (user == "SCISSOR" and original == "PAPER"):
        print("You Won!!!")
    else:
        print("You Lost!!!")

# The backslash \ you’re seeing after or isn’t part of the logic—it’s actually a line continuation character in Python
