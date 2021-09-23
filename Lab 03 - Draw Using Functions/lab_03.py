
"""Lab 3 Moving Functions"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_ocean():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.BLUE)


def draw_sun(x, y):
    # Sun
    arcade.draw_circle_filled(y, x, 50, arcade.color.RED)


def draw_cloud(x, y):
    # Cloud
    arcade.draw_circle_filled(400 + x - 200, 540 + y - 400, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(340 + x - 200, 470 + y - 400, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(340 + x - 200, 440 + y - 400, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(310 + x - 200, 530 + y - 400, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(230 + x - 200, 450 + y - 400, 60, arcade.color.WHITE)


def draw_cloud_second(x, y):
    # second Cloud
    arcade.draw_circle_filled(320 + x - 200, 460 + y - 400, 55, arcade.color.WHITE)
    arcade.draw_circle_filled(260 + x - 200, 380 + y - 400, 55, arcade.color.WHITE)
    arcade.draw_circle_filled(260 + x - 200, 360 + y - 400, 55, arcade.color.WHITE)
    arcade.draw_circle_filled(230 + x - 200, 450 + y - 400, 55, arcade.color.WHITE)
    arcade.draw_circle_filled(160 + x - 200, 370 + y - 400, 55, arcade.color.WHITE)


# Canoes
def draw_rect(x, y):
    arcade.draw_rectangle_filled(130 + x - 300, 200 + y - 300, 150, 70, arcade.color.REDWOOD)


def draw_rect_two(x, y):
    arcade.draw_rectangle_filled(250 + x - 300, 250 + y - 300, 150, 70, arcade.color.REDWOOD)


def draw_triangle(x, y):
    arcade.draw_triangle_filled(220 + x - 400, 137 + y - 400, 280 + x - 400, 137 + y - 400, 280 + x - 400, 60 + y - 400,
                                arcade.color.REDWOOD)
    arcade.draw_triangle_filled(0 + x - 400, 237 + y - 400, 60 + x - 400, 237 + y - 400, 60 + x - 400, 160 + y - 400,
                                arcade.color.REDWOOD)


def draw_triangle_two(x, y):
    arcade.draw_triangle_filled(480 + x - 300, 137 + y - 300, 425 + x - 300, 137 + y - 300, 425 + x - 300, 60 + y - 300,
                                arcade.color.REDWOOD)
    arcade.draw_triangle_filled(270 + x - 300, 237 + y - 300, 205 + x - 300, 237 + y - 300, 205 + x - 300,
                                160 + y - 300, arcade.color.REDWOOD)


def on_draw(delta_time):
    arcade.start_render()
    draw_sun(on_draw.sun1_y, 500)
    draw_ocean()
    draw_cloud(on_draw.cloud1_y, 375)
    draw_cloud_second(on_draw.cloud2_y, 300)
    draw_rect(on_draw.rect1_y, 200)
    draw_rect_two(on_draw.rect2_y, 250)
    draw_triangle(on_draw.triangle1_y, 400)
    draw_triangle_two(on_draw.triangle2_y, 300)
    on_draw.rect1_y += 2
    on_draw.rect2_y += 2
    on_draw.triangle1_y += 2
    on_draw.triangle2_y += 2
    on_draw.sun1_y -= 1
    on_draw.cloud1_y -= 2
    on_draw.cloud2_y += 2


on_draw.sun1_y = 550
on_draw.cloud1_y = 450
on_draw.cloud2_y = 375
on_draw.rect1_y = 370
on_draw.rect2_y = 30
on_draw.triangle1_y = 245
on_draw.triangle2_y = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Ocean")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    # Finish and run
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


# Call the main function to get the program started.
main()
