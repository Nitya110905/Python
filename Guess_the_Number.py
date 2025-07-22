import random
original = random.randint(1,50)

print("Enter your desired no. among 1-50")
print("You need to guess it in 5 chances!")
count = 0

while True:
    user = int(input("Enter No. :"))

    count += 1

    if user>50:
        print("Invalid choice!!")
        break
    elif user < original and count < 5:
        print(f"{user} is less than the number to be guessed!!!")
    elif user > original and count < 5:
        print(f"{user} is greater than the number to be guessed!!!")
    elif user == original and count < 5:
        print("You Won!!!")
        break
    else:
        print(f"The No. to be guessed was {original}")
        print("Better Luck Next Time Champ!!!")
        break