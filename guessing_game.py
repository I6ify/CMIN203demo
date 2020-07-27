import time

name = input("what is your name? ")

print ("Hello, " + name, "time to play!")
print ()

time.sleep(2)

print ("Begin!")

time.sleep(1)

word = "secret"
guesses = ''
guess = input("guess a character: ")
guesses += guess
turns = 10

while turns > 0:
  failed = 0
  for char in word:

    if char in guesses:
      print (char,)
    else:
        print ("_",)
  break

if guess not in word:
          turns -=1
          print ("incorrect, try again")
if turns == 0:
          print ("You Lose.")
