import pyfiglet
import random

ascii_banner = pyfiglet.figlet_format("Hangman Game")
print(ascii_banner)

print("Welcome to the Hangman Game!")
print("-"*28)

tries = int(input("How many tries would you like to have(at least 7) : "))

answer_list = ['world', 'hello', 'this', 'python', 'game']

random.shuffle(answer_list)

answer = list(answer_list[0])
display = []
display.extend(answer)

for i in range(len(display)):
    display[i] = "_"

print("The word contains : ")
print(' '. join(display)+ "\n")


while tries!=0 and display!=answer:
    guess = input("Please guess a letter: ")
    guess = guess.lower()
    print(f"\nYou still have {tries - 1} tries.")
    tries -= 1


    for i in range(len(answer)):
        if answer[i] == guess:
            display[i] = guess

    print(' '.join(display))
    print()

if display==answer:
    print("Well done, you guessed the word")
else: print("Unlucky!")