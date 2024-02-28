# This project was inspired by the coding challenge https://www.101computing.net/battle-of-the-knights/
import random
import time
from os import system

system("cls")

k1_health = k2_health = 100

# List of first names
first_names = [
    "Arthur", "Edward", "William", "Geoffrey", "Roland",
    "Percival", "Lancelot", "Gawain", "Tristan", "Galahad",
    "Baldwin", "Oliver", "Hector", "Godfrey", "Geraint", "Lionel",
    "Alden", "Cedric"
]

# List of titles
titles = [
    "the Valiant", "the Fearless", "the Bold", "the Gallant", "the Resolute",
    "the Brave", "the Dauntless", "the Mighty", "the Noble",
    "the Fierce", "the Intrepid", "the Valorous", "the Lionhearted", "the Indomitable",
    "the Steadfast", "the Unyielding", "the Unflinching", "the Stalwart"
]

k1_name = f"{random.choice(first_names)} {random.choice(titles)}"

segment = k1_name.split(' ')

first_names.remove(segment[0])  # remove the first name of knight 1 from the list of first names
titles.remove(f"{segment[1]} {segment[2]}") # remove the title of knight 1 from the list of titles

k2_name = f"{random.choice(first_names)} {random.choice(titles)}"


def k1_attack():
    line1 = "  O   /"
    line2 = "- + -/ "
    line3 = " / \   "

    return line1, line2, line3

def k2_attack():
    line1 = "\   O  "
    line2 = " \- + -"
    line3 = "   / \ "

    return line1, line2, line3

def k1_defend():
    line1 = "  O  |"
    line2 = "- + -|"
    line3 = " / \ |"

    return line1, line2, line3

def k2_defend():
    line1 = "|  O  "
    line2 = "|- + -"
    line3 = "| / \ "

    return line1, line2, line3

def rest():
    line1 = "  O  "
    line2 = "- + -"
    line3 = " / \ "

    return line1, line2, line3

def victory():
    line1 = "\ O /"
    line2 = "  +  "
    line3 = " / \ "

    return line1, line2, line3

def death():
    line1 = "/-+-O"

    return line1

# reduce a random amount of health
def reduce_health():
    return random.randint(7, 15)

for t in range(3, 0, -1):
    # print the initial position
    print(f"Battle starts in {t}")

    for k in range(3):
        print(f"{k1_attack()[k]}    {k2_attack()[k]}")

    time.sleep(1)
    system("cls")

for k in range(3):
    print(f"{k1_attack()[k]}    {k2_attack()[k]}")
print(f"{k1_name}: {k1_health}")
print(f"{k2_name}: {k2_health}")

time.sleep(1.5)

while True:
    # clear the screen before every iteration
    system("cls")

    # select a random position for both knights
    k1_rand_pos = random.choice([k1_attack, k1_attack, k1_defend, rest])
    k2_rand_pos = random.choice([k2_attack, k2_attack, k2_defend, rest])
    
    if k1_rand_pos == k1_attack and k2_rand_pos == k2_attack:
        k1_health -= reduce_health()
        k2_health -= reduce_health()

    elif k1_rand_pos == k1_attack and k2_rand_pos == rest:
        k2_health -= reduce_health()

    elif k1_rand_pos == rest and k2_rand_pos == k2_attack:
        k1_health -= reduce_health()
    
    # prevent showing negative health
    if k1_health < 0:
        k1_health = 0
    
    if k2_health < 0:
        k2_health = 0

    # print the position of both knights
    for i in range(3):
        print(f"{k1_rand_pos()[i]}    {k2_rand_pos()[i]}")
    
    print(f"{k1_name}: {k1_health}")
    print(f"{k2_name}: {k2_health}")

    time.sleep(1.5)

    if k1_health == 0 and k2_health == 0:
        print(f"\n{death()}    {death()}")
        break

    elif k1_health == 0:
        print()
        for j in range(2):
            print(f"         {victory()[j]}")
        print(f"{death()}    {victory()[2]}")
        break

    elif k2_health == 0:
        print()
        for j in range(2):
            print(victory()[j])
        print(f"{victory()[2]}    {death()}")
        break

system("pause")
