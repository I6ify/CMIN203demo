import time
import random
from words import word_list


def new_word():
    word = random.choice(word_list)
    return word.upper()

name = input("What is your name? \n")

print("Hello, " + name, ", time to play hangman!")

time.sleep(0.5)

print("Start guessing...")
time.sleep(0.5)


guesses = ''

turns = 10

while turns > 0:

 failed = 0

 for char in word:

  if char in guesses:

   print(char)
  else:
   print("_"),
   failed += 1

 if failed == 0:
  print("You won \n")

 break


guess = input("Guess a character: \n")

guesses += guess


if guess not in word:

    turns -= 1

    print("Wrong! \n")

    print ("You have", + turns, "more guesses")

if turns == 0:
  print("You lose!")
