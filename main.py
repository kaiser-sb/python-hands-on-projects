import random

def get_choices():
  options = ["rock", "paper", "scissors"]
  player_choice = input(" Enter your choice (rock, paper, scissors) : ")
  computer_choice = random.choice(options)
  choices = {
    "player" : player_choice,
    "computer" : computer_choice
  }
  return choices

def check_win(player, computer):
  print(f"\n You chose {player} and Computer chose {computer}")
  if player == computer:
    return "\n It's a tie!"
    
  elif player == "rock": 
    if computer == "scissors":
      return "\n Rock smashes scissors! You win!!"
    else:
      return "\n Paper covers rock. You lose :( "

  elif player == "paper": 
    if computer == "rock":
      return "\n Paper covers rock! You win!!"
    else:
      return "\n Scissors cuts paper. You lose :( "

  elif player == "scissors": 
    if computer == "rock":
      return "\n Rock smashes scissors. You lose :( "
    else:
      return "\n Scissors cuts paper! You win! "


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
