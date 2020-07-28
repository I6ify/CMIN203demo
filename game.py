import time
import random
from words import word_list

name = input("what is your name? ")

print ("Hello, " + name, "time to play!")
print ()

def new_word():   #this function grabs a word from a the list
    word = random.choice(word_list)
    return word.upper()

def play(word):  #this is my function which plays the game itself
    hidden_word = '_' * len(word) #string that hold blanks until they are guessed
    guessed = False
    guess_letters = []
    lives = 6
    print(lives)
    print(hidden_word)
    print("\n")
    while not guessed and lives > 0:
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1:
            if guess in guess_letters:
                print("You have already guessed that letter, " + name)
                print("\n")
            elif guess not in word:
                print(guess, "is not in the word, " + name)
                lives -= 1
                guess_letters.append(guess)
                print("You have " + str(lives), "lives remaining.")
                print("\n")
            else:
                print(guess, "is in the word!")
                guess_letters.append(guess)
                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                print(word_completion)
        elif len(guess) != 1 or isnotalpha():
            print("please enter a single letter, " + name)

    if guessed:
        print("A winner is you!")
    else:
        print("Looks like I win this time, " + name)
        print(word)

def main():
    word = new_word()
    play(word)


if __name__ == "__main__":
    main()
