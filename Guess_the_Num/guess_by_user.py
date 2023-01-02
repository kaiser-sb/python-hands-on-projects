import random as rd

max = int(input("\n\nEnter the largest number within which you're guessing a number (positive integer only) : "))
min = 1
comp = rd.randint(min, max)
count = 1
res = input(f"\n\nOK... My guess is {comp}. Is it correct? Enter Y/N : ").lower()

while res == "n" and res != "y":
    q = input("\n\nUmmm that's unfortunate. Is my guess greater or lesser than your number? Enter G/L : ").lower()
    if q == "g" or q == "greater":
        max = comp - 1
        comp = rd.randint(min, max)
        count += 1
        res = input(f"\n\nOK... My guess is {comp}. Is it correct? Enter Y/N : ").lower()
    elif q == "l" or q == "lesser":
        min = comp + 1
        comp = rd.randint(min, max)
        count += 1
        res = input(f"\n\nOK... My guess is {comp}. Is it correct? Enter Y/N : ").lower()
    else:
        print("\n\nPlease enter a valid input!")
        res = "n"

    

print(f"\n\nWoohoo!! I got it right after {count} attempts! You guessed {comp}\n\n")
