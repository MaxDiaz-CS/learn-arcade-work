# Camel 4
# Still not done going to resubmit by friday night along with CIS 120

import random

# Introduction
print("Get Out of Mongolia!")
print("You have stolen a prized camel from the Khan with goal of selling it.")
print("The Mongol horde want their Khan's prized camel back and are chasing you across the steppes!")
print("You have to survive the trek across the steppes until you get to Song Kingdom")
print("The mongols are merciless towards anyone they feel that been crossed.")
print("So surely being allowed to be captured is surely isn't an option.")
print("You will face off on certain decisions along the journey in order to stave off certain disasters.")
print("Now the only remaining question is, are you ready?")
print()

# Variables for the game
done = False
miles_traveled = 0
thirst = 0
canteen = 3
mongols_starting_distance = -10
camel_exhaustion = 0

# The Great Mongol Chase options
while not done:
    print("A. Drink some refreshing water from your canteen.")
    print("B. Make your camel move at moderate speed.")
    print("C. Force the Camel go at full speed.")
    print("D. Stop for the night and let the camel rest.")
    print("E. Stop and check how far you have come.")
    print("Q. Quit.")
    print()

    random.choice = input("What's the best course of action? ")

    if random.choice.upper() == "A":
        if canteen > 0:
            canteen -= 1
            thirst = 0
            print("You drank some water from your Canteen ")
            print("Now your thirst has been quench.")
            print()
        else:
            print("Your canteen is empty. Now you have to endure the trip without water until you reach the next town.")
            print()

    elif random.choice.upper() == "B":
        normal_speed = random.randrange(5, 12)
        enemy_speed = random.randrange(6, 15)
        miles_traveled += miles_traveled
        thirst += 1
        camel_exhaustion += 1
        miles_traveled = miles_traveled + normal_speed
        mongols_starting_distance = mongols_starting_distance + enemy_speed

        if random.randrange(21) == 0:
            thirst = 0
            camel_exhaustion = 0
            canteen = 3
            print("You have arrived at a small town.")
            print()
        else:
            print("You did some good progress today, you have move a total of ", normal_speed)
            print("Despite the good progress the mongols are still hot on your heels")
            print("BETTER GET MOVING!!!!!!!!!")
            print()

    elif random.choice.upper() == "C":
        thirst += 1
        full_speed = random.randrange(7, 23)
        enemy_speed = random.randrange(6, 15)
        miles_traveled = miles_traveled + full_speed
        mongols_starting_distance = mongols_starting_distance + enemy_speed

        camel_exhaustion -= camel_exhaustion + random.randrange(1, 5)
        if random.randrange(21) == 0:
            thirst = 0
            camel_exhaustion = 0
            canteen = 3
            print("you have arrived at a local town and have resupplied")
            print()
        else:
            print("You did some good progress today, you have move a total of ", full_speed)
            print("Despite the good progress the mongols are still hot on your heels")
            print("BETTER GET MOVING!!!!!!!!!")
            print()

    elif random.choice.upper() == "D":
        print("you decided to camp for the night and let your camel rest for the night.")
        print()
        camel_exhaustion = 0
        enemy_speed = random.randrange(6, 15)
        mongols_starting_distance = mongols_starting_distance + enemy_speed

    elif random.choice.upper() == "E":
        print("Distance traveled", miles_traveled)
        print("Drinks left in the canteen", canteen)
        print("Mongols are still", miles_traveled - mongols_starting_distance, "behind you.")
        print()

    if random.choice.upper() == "Q":
        print("Goodbye.")
        print()
        done = True

# Game Loop
if not done:
    if miles_traveled >= 200:
        print("You have won")
        print()
        done = True

    if thirst > 3:
        print("you have died of thirst")
        print("GAMEOVER!")
        print()
elif thirst > 3:
    print("you're really thirsty")
    print()

if camel_exhaustion > 8:
    print("Your Camel has died from exhaustion")
    print("GAMEOVER!")
    print()
elif camel_exhaustion > 5:
    print("Your camel is getting exhausted")
    print()

if miles_traveled - mongols_starting_distance <= 0:
    print("The Mongols caught up to you!")
    print("GAMEOVER!")
    print()
elif miles_traveled - mongols_starting_distance <= 15:
    print("The Mongols are getting close!")
    print()
