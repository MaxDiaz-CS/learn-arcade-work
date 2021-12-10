"""
Array Backed Grid

Show how to use a two-dimensional list/array to back the display of a
grid on-screen.
"""
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 70
HEIGHT = 70

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

number_cells_selected = 0


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        for row in self.grid:
            print(row)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        # Draw a rectangle
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.BLUE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        number_cells_selected = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    number_cells_selected += 1
        print("Total of " + str(number_cells_selected) + " cells are selected.")

        for row in range(ROW_COUNT):
            number_row_cells_selected = 0
            continuous_count = 0

            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    number_row_cells_selected += 1
                    continuous_count += 1
                if self.grid[row][column] == 0:
                    if continuous_count > 2:
                        print("Row " + str(row) + " has " + str(continuous_count) + " continuous blocks selected.")
                    continuous_count = 0
            if continuous_count > 2:
                print("Row " + str(row) + " has " + str(continuous_count) + " continuous blocks selected.")
            print("Row " + str(row) + " has " + str(number_row_cells_selected) + " cells selected.")

        for column in range(COLUMN_COUNT):
            number_column_cells_selected = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    number_column_cells_selected += 1
            print("Column " + str(column) + " has " + str(number_column_cells_selected) + " cells selected.")
        print("")


def main():

   window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
   arcade.run()


if __name__ == "__main__":
   main()