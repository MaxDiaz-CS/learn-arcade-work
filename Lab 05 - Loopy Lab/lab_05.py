# LOOPY LAB 5
import arcade

SCREEN_WIDTH = 1425
SCREEN_HEIGHT = 720


def outlines():
    arcade.draw_rectangle_outline(180, 180, 350, 355, arcade.color.WHITE)
    arcade.draw_rectangle_outline(180, 540, 350, 355, arcade.color.WHITE)
    arcade.draw_rectangle_outline(535, 180, 350, 355, arcade.color.WHITE)
    arcade.draw_rectangle_outline(535, 540, 350, 355, arcade.color.WHITE)
    arcade.draw_rectangle_outline(890, 180, 350, 355, arcade.color.WHITE)
    arcade.draw_rectangle_outline(890, 540, 350, 355, arcade.color.WHITE)
    arcade.draw_rectangle_outline(1245, 180, 350, 355, arcade.color.WHITE)
    arcade.draw_rectangle_outline(1245, 540, 350, 355, arcade.color.WHITE)


def bottom_square_1():
    for row in range(36):
        for column in range(36):
            x = column * 10 + 5
            y = row * 10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def bottom_square_2():
    for row in range(35):
        for column in range(35):
            x = column * 10 + 365
            y = row * 10 + 13
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE)


def bottom_square_3():
    for row in range(35):
        for column in range(35):
            x = column * 10 + 721
            y = row * 10 + 13
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE)


def bottom_square_4():
    for row in range(35):
        for column in range(35):
            x = column * 10 + 1075
            y = row * 10 + 13
            if row % 2 == 0 and column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLUE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def upper_square_1():
    for column in range(35):
        for row in range(column + 1):
            x = column * 10 + 13
            y = row * 10 + 365
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def upper_square_2():
    for row in range(35):
        for column in range(35 - row):
            x = column * 10 + 365
            y = row * 10 + 365
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def upper_square_3():
    for row in range(35):
        for column in range(row + 1):
            x = (34 - column) * 10 + 720
            y = row * 10 + 370
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def upper_square_4():
    for row in range(37):
        for column in range(row - 1):
            x = column * 10 + 1077
            y = row * 10 + 350
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    outlines()

    bottom_square_1()
    bottom_square_2()
    bottom_square_3()
    bottom_square_4()
    upper_square_1()
    upper_square_2()
    upper_square_3()
    upper_square_4()

    # Finish and run
    arcade.run()


# Call the main function to get the program started.
main()
