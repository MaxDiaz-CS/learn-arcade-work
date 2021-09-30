# Lab 04: Camel game
import random

# Introduction
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the Mobi Desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("Desert trek and out run the natives.")
print()

# initiate variables
done = False
milesTraveled = 0
nativesTraveled = -20
camelTiredness = 0
thirst = 0
canteen = 3
oasis = -1
# Game loop
while not done:

    # options
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print()

    # Take user's input
    userInput = input("What will you do? ")

    # Check if they want to quit
    if userInput.upper() == "Q":
        done = True
    # Status update
    elif userInput.upper() == "E":
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteen)
        print("The natives are", milesTraveled - nativesTraveled, "miles behind you.")
        print()
    # stop for the night
    elif userInput.upper() == "D":
        print("You stop for the night.")
        print("Your camel is happy.")
        print("The natives don't stop.")
        print()
        camelTiredness = 0
        nativesTraveled += random.randrange(7, 15)
    # full speed ahead
    elif userInput.upper() == "C":
        miles = random.randrange(10, 21)
        milesTraveled += miles
        thirst += 1
        camelTiredness += random.randrange(1, 4)
        nativesTraveled += random.randrange(7, 15)
        oasis = random.randrange(20)
        if oasis == 10:
            thirst = 0
            camelTiredness = 0
            canteen = 3
            print("As you travel you happen upon an oasis!")
            print("You fill your canteen and your stomach with water, and")
            print("Your camel is rested!")
            print("The natives continue the chase.")
            print()
        else:
            print("You push onward at full speed, moving a total of", miles, "miles")
            print("Your thirst increases.")
            print("The natives continue the chase.")
            print()
    # mid-speed ahead
    elif userInput.upper() == "B":
        miles = random.randrange(5, 13)
        milesTraveled += miles
        thirst += 1
        camelTiredness += 1
        nativesTraveled += random.randrange(7, 15)
        oasis = random.randrange(20)
        if oasis == 10:
            thirst = 0
            camelTiredness = 0
            canteen = 3
            print("As you travel you happen upon an oasis!")
            print("You fill your canteen and your stomach with water, and")
            print("Your camel is rested!")
            print("The natives continue the chase.")
            print()
        else:
            print("You move forward, moving a total of", miles, "miles")
            print("Your thirst increases.")
            print("The natives continue the chase.")
            print()
    # Drink from canteen
    elif userInput.upper() == "A":
        if canteen > 0:
            canteen -= 1
            thirst = 0
            print("You take a drink")
        else:
            print("Your canteen is empty. You imagine yourself as a lifeless, dry husk.")

    # Status updates
    # Thirst
    if thirst > 5:
        print("You died of thirst!")
        print("Game Over.")
        print()
        done = True
    elif thirst > 4:
        print("You are thirsty!")
    # Distance traveled / win check
    if milesTraveled >= 200:
        print("Congratulations! You have crossed the entire desert!")
        print("You win!")
        print()
        done = True
    # Camel's tiredness
    if camelTiredness > 8:
        print("Your camel died of exhaustion!")
        print("With no camel, the natives catch up to you and kill you")
        print("on the spot.")
        print("Game Over.")
        print()
        done = True
    elif camelTiredness > 5:
        print("Your camel is tired.")
        print()
    # Natives distance from you
    if milesTraveled - nativesTraveled <= 0:
        print("The natives have caught up with you!")
        print("They kill you on the spot, and take their camel back.")
        print("Game Over.")
        print()
        done = True
    elif milesTraveled - nativesTraveled < 15:
        print("You see faint shapes on the horizon behind you.")
        print("The natives are getting close!")
        print()

# Exit message
print("Exiting Game. Goodbye.")
input("")
