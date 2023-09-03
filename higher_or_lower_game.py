#!/usr/bin/env python3

import random

def main():
  print("Welcome to higher or lower!")
  low = int(input("Choose your lowest value: "))
  high = int(input("Choose your highest value: "))
  number = random.randint(low, high)
  guess = int(input("Take your guess: "))
  if guess > number:
    print("The number is lower!")
  elif guess < number:
    print("The number is higher!")
  while guess != number:
    guess = int(input("Take your guess: "))
    if guess > number:
      print("The number is lower!")
    elif guess < number:
      print("The number is higher!")
  if guess == number:
    print(f"You guessed correctly! The number is {number}!".format(number))
      
  if high <= low:
    print("Please make sure the higher number is greater than the lower. Restarting program.\n----------------------------------")
    main()
  









if __name__ == "__main__":
  main()