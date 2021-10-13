# Not done
# currently re reading chapters 15 to 17 to understand lists
# probably going to resubmit this monday
# going to setup a meeting for monday to make sure I get all of the points

class Rooms:
    def __init__(self):
        self.north = ""
        self.south = 0
        self.west = 0
        self.east = 0


def main():
    room_list = [1, 2]

    for i in range(4):
        user_input = input("Enter a room: ")
        user_input = int(user_input)
        room_list.append(user_input)
        print(room_list)


main()
