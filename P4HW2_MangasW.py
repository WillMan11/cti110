# CTI 110
# P4HW2
# MangasW
# 3/11/2022
import random

def human_guesses():
  guessesUsed = 0
  
  print("I'm thinking of a number between 1 and 20.")
  number = random.randint(1, 20)
  
  for tries in range(6):
    guessesUsed += 1
    guess = int(input("What's your guess? "))
    
    if guess > number:
      print("That's too high.")
    elif guess < number:
      print("That's too low")
    else: # guessed it
      break # leave the loop early
  
  # either we guessed, or ran out of tries
  if guess == number:
    print("Congratulations! The number was", number)
    print("You got it in" , guessesUsed)
  else:
    print("Too bad! The number was", number)

def computer_guesses():
  MAX_NUM = 20
  print("Think of a number between 1 and", MAX_NUM)
  print("You can type it here, I won't peek.")
  answer = input()
  # guess the middle number first
  guess = MAX_NUM // 2
  lowest = 1
  highest = MAX_NUM
  print("Please type yes, too high, or too low as y,h,l")
  for guess in range(4):
    guess = (lowest + highest) // 2
    print("Is your number", guess,"? (y/h/l)")
    result = input()
    if result == "y":
      print("Yay! I win!")
      break
    elif result == "l":#too low
      print("I'll guess higher next time")
      # guess higher
      lowest = guess + 1
    elif result == "h":#too high
      print("I'll guess lower next time")
      # guess lower
      highest = guess -1
            
  # won or lost
  if result == "y":
      print("Thanks for playing")
  else:
    print("I almost got it")
    

def main():
  #human_guesses()
  print("OK, my turn.")
  computer_guesses()

# start the program
main()
