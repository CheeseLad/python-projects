#!/usr/bin/env python3

import random
playing = 1
print("Welcome to Rock, Paper, Scissors!")

while playing == 1:
  p1 = input("What do you pick? Rock, Paper or Scissors? Enter here: ").lower()
  randint = random.randint(1, 3)


  if randint == 1:
      p2 = "rock"
  elif randint == 2:
      p2 = "paper"
  elif randint == 3:
      p2 = "scissors"

  print("You have picked: " + p1)
  print("Player 2 has picked: " + p2)

  if p1 == "rock" and p2 == "rock":
      print("It's a draw!")
  elif p1 == "rock" and p2 == "paper":
      print("Player 2 wins!")
  elif p1 == "rock" and p2 == "scissors":
      print("You win!")
  elif p1 == "paper" and p2 == "rock":
      print("You win!")
  elif p1 == "paper" and p2 == "paper":
      print("It's a draw!")
  elif p1 == "paper" and p2 == "scissors":
      print("Player 2 wins!")
  elif p1 == "scissors" and p2 == "rock":
      print("Player 2 wins!")
  elif p1 == "scissors" and p2 == "paper":
      print("You win!")
  elif p1 == "scissors" and p2 == "scissors":
      print("It's a draw!")

  replay = input("Would you like to play again? Enter Yes or No: ").lower()
  if replay == "yes":
      playing = 1
  elif replay == "no":
      playing = 0
