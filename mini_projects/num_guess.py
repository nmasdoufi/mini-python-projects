import random
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Guess The Number!!!")
print(ascii_banner)

def guess():

    attempt = int(input("Guess the right number: "))
    ran_num = random.randint(1, 15)

    while attempt != ran_num:

        if attempt > ran_num:
            print("Guess Lower")
        elif attempt < ran_num:
            print("Guess Higher")
        else: print("Try again")

        attempt = int(input("Guess the right number: "))
        if attempt == ran_num:
            print("You got it!")


guess()
