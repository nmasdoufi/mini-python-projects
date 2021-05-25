import random
import pyfiglet
from PIL import Image

ascii_banner = pyfiglet.figlet_format("Dice Rolling Simulator")
print(ascii_banner)

count = 0
rolled_count = 0

choice = input("Would you like to start? (y for yes): ")


while choice ==  'y':

    num = random.randint(1,6)
    print(f"You rolled a {num}\n")
    im = Image.open(f'/full/path/to/image/{num}.png')
    print(im.show())

    choice = input("Would You like to Continue? ")

    count += num
    rolled_count += 1


print("Your rolls add up to ", count)
print("You rolled", rolled_count, "times.")