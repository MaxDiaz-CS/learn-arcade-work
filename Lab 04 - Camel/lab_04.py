# Camel 4
# finally completed

import random


def main():
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
    mongols_starting_distance = -25
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

        random_choice = input("What's the best course of action? ")

        if random_choice.upper() == "Q":
            print("You have decided to quit the game\n")
            done = True

        elif random_choice.upper() == "E":
            print("Miles Traveled", miles_traveled, "currently.")
            print("There's", canteen, "drinks remaining.")
            print("The Mongols are only", miles_traveled - mongols_starting_distance, "miles away.\n")
            print()

        elif random_choice.upper() == "D":
            camel_exhaustion = 0
            mongols_starting_distance += random.randrange(9, 16)
            print("You and your camel are fully rested and ready for the next leg of the journey.\n")

        elif random_choice.upper() == "C":
            full_speed = random.randrange(10, 25)
            thirst += 1
            camel_exhaustion = 0
            miles_traveled += full_speed
            mongols_starting_distance += random.randrange(9, 14)
            camel_exhaustion += random.randrange(1, 4)
            oasis = random.randrange(20)
            print("You have traveled", full_speed, "miles.\n")
            if oasis == 10:
                print("You encountered a small village")
                canteen = 3
                thirst = 0
                camel_exhaustion = 0
                print("you were able to restock on food and water for the remaining portion of the journey\n")

        elif random_choice.upper() == "B":
            thirst = thirst + 1
            camel_exhaustion = camel_exhaustion + 1
            normal_speed = random.randrange(5, 12)
            enemy_distance = random.randrange(7, 20)
            miles_traveled = miles_traveled + normal_speed
            mongols_starting_distance = mongols_starting_distance + enemy_distance

            if random.randrange(21) == 0:
                print("You encountered a small village")
                canteen = 3
                thirst = 0
                camel_exhaustion = 0
                print("you were able to restock on food and water for the remaining portion of the journey")
                print("You have traveled", normal_speed, "miles.\n")

            else:
                print("Mongols still on your heels.\n")

        elif random_choice.upper() == "A":
            if canteen > 0:
                canteen -= 1
                thirst = 0
                print("Your thirst has been quenched\n")
            else:
                print("It seems you ran out of water\n")

            # Game Loop

        if miles_traveled >= 250:
            print("You made it across the Steppes into the Song Kingdom! You won the game!")

            done = True

        if miles_traveled <= mongols_starting_distance:
            print("You have been captured by the mongols! You have lost the game!")
            print("You were skinned alive as a example to other who dare to steal from the Khan.\n")
            done = True

        if thirst >= 5:
            print("You have died of thirst!")
            print("your remains are currently picked apart by wild animals of the steppes.\n")
            done = True

        elif thirst >= 3:
            print("You are thirsty!\n")

        if camel_exhaustion >= 5:
            print("Your Camel has died! You lost!")
            print("The mongols found you and killed you. Then they proceeded to take back the prized camel back to "
                  "the Khan\n")
            done = True

        elif camel_exhaustion >= 6:
            print("Your Camel is exhausted!!!\n")

        if miles_traveled - camel_exhaustion <= 15:
            print("The Mongols are very close!!!!\n")


main()
