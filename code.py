#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art




global user_Guessed_number

def divisible_by(number):
  if number%2 == 0:
    print("the number is even")
  elif number%3 == 0:
    print("the number is divisible by 3")
  elif number%5 == 0:
    print("the number is divisible by 5")
  elif number%7 == 0:
    print("the number is divisible by 7")
  elif number%11 == 0:
    print("the number is divisible by 11")


def guess_the_number(chances_left):
  guess_number = random.randint(1,100)
  while chances_left>0:
    print("################################################################")
    user_Guessed_number = int(input("\nEnter the number you think is guess number  "))
    
    if guess_number == user_Guessed_number:
      print("you have won\n")
      print(art.logo[1])
      return
      
    elif guess_number > user_Guessed_number:
      
      print("your guess number is too less, try greater\n")
      
      
    else:
      print("your guess number is too high, try smaller\n")
      
    chances_left -=1
    
    if chances_left==0:
      print("You have lost\n")
      print(art.logo[0])
      print(f"the number was {guess_number}")
      return 
      
    print(f"you have {chances_left} chances left choose wisely")
    
    if chances_left ==3:
      divisible_by(guess_number)

    if chances_left ==1:
      print(f"the number is {guess_number - user_Guessed_number} more then current user guess number")
    

  



easy = int(input("Choose difficulty: do you want the game to be easy? 1.yes 2.no "))


if easy ==1:
  print("you have 10 chances ")
  chances_left =10
  guess_the_number(chances_left)
  
else:
  print("you have 5 chances ")
  chances_left = 5
  guess_the_number(chances_left)
  
