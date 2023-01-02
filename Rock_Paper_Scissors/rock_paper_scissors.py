import random as rd

def play(game_count):
    
    count = 1
    user = 0
    comp = 0
    while count <= game_count:
        print("*" *50)
        print(f"\nGame {count} of {game_count}\n")
        print("*" *50)
        
        user_choice = input("\n\nEnter your choice (rock, paper or scissors) : ").lower()
        comp_choice = rd.choice(choices)
        print(f"\n\nYou chose {user_choice} and Computer chose {comp_choice}")
    
        if user_choice == "rock" and comp_choice == "scissors":
            print("\n\nRock smashes scissors! You win!! :)\n")
            user += 1
            count += 1
        elif user_choice == "rock" and comp_choice == "paper":
            print("\n\nPaper covers rock! You lose :(\n")
            comp += 1
            count += 1
        elif user_choice == "paper" and comp_choice == "rock":
            print("\n\nPaper covers rock! You win!! :)\n")
            user += 1
            count += 1
        elif user_choice == "paper" and comp_choice == "scissors":
            print("\n\nScissors cut paper! You lose :(\n")
            comp += 1
            count += 1
        elif user_choice == "scissors" and comp_choice == "paper":
            print("\n\nScissors cut paper! You win! :)\n")
            user += 1
            count += 1
        elif user_choice == "scissors" and comp_choice == "rock":
            print("\n\nRock smashes scissors! You lose :(\n")
            comp += 1
            count += 1
        else:
            print(f"\n\nIt's a tie!\n")
            count += 1
    print("\n\n*************** FINAL RESULT ***************")
    print()
    print(f"\n\tYou : {user}\t\tComputer : {comp}")
    
choices = ["rock", "paper", "scissors"]
print("\n\n************ ROCK, PAPER AND SCISSORS ************")
game_count = int(input("\n\nHow many games do you want to play? : "))
print()
play(game_count)
print()
print("\n**************** THANKS FOR PLAYING !! ****************\n")