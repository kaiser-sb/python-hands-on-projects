import random as rd

limit = int(input("\n\nEnter the largest positive integer within which you want me to guess a number : "))
comp = rd.randint(1, limit)

print(f"\n\nI have guessed a number between 1 and {limit}!")

user = int(input(f"\n\nEnter your guess between 1 and {limit} : "))
count = 1

while user != comp:
    if user > comp :
        print("\n\nYou entered a number greater than my guess! \n\n")
        user = int(input("Enter your next guess : "))
        count += 1
    else:
        print("\n\nYou entered a number lesser than my guess! \n\n")
        user = int(input("Enter your next guess : "))
        count += 1

print(f"\n\nYou have finally got it right after {count} attempts! The final number is {comp}\n\n")








