import random
import os


def init():
    global started, dead, frames_while_dead_elapsed, ended, first_pipe, pipe_x, pipe_height, pipe_y, second_pipe_x, second_pipe_height, second_pipe_y, score, bird_angle, pipe_colour_green, unmovable
    started = False
    dead = False
    frames_while_dead_elapsed = 0
    ended = False
    first_pipe = True

    pipe_x = screen_width
    pipe_height = random.randint(25, 475)
    pipe_y = screen_height - pipe_height

    second_pipe_x = pipe_x + distance_between_pipes
    second_pipe_height = random.randint(25, 450)
    second_pipe_y = screen_height - second_pipe_height

    score = 0
    bird_angle = 0
    pipe_colour_green = random.choice([True, False])

    unmovable = False


def choose_pipe_colour():
    global pipe_colour_green
    pipe_colour_green = random.choice([True, False])


def set_bird_pictures():
    global bird_colour, wing_down, wing_mid, wing_up
    bird_colour = random.choice(["yellow", "blue", "red"])
    wing_up = os.path.join("data", "sprites", "birds", bird_colour, "up.png")
    wing_down = os.path.join("data", "sprites", "birds", bird_colour, "down.png")
    wing_mid = os.path.join("data", "sprites", "birds", bird_colour, "mid.png")


started = False
dead = False
frames_while_dead_elapsed = 0
ended = False
score = 0
unmovable = False

# -------------------------------------------------------------------------------------------------
fps_target = 62
screen_width, screen_height = 400, 600

# -------------------------------------------------------------------------------------------------
bird_colour = None
bird_x = screen_width * 0.4
bird_y = screen_height // 2
bird_change_y = 0
bird_height = 20
bird_width = 30
bird_angle = 0
bird_oscillation_angle = 0
bird_flap_state = 0
wing_up = None
wing_mid = None
wing_down = None

# -------------------------------------------------------------------------------------------------
distance_between_pipes = 300

# -------------------------------------------------------------------------------------------------
pipe_x = screen_width
pipe_height = random.randint(70, 450)
pipe_y = screen_height - pipe_height
pipe_width = 70
pipe_gap = 130

# -------------------------------------------------------------------------------------------------
second_pipe_x = pipe_x + distance_between_pipes
second_pipe_height = random.randint(70, 450)
second_pipe_y = screen_height - second_pipe_height

# -------------------------------------------------------------------------------------------------
pipe_velocity = -3.54
first_pipe = True
pipe_colour_green = random.choice([True, False])

if pipe_colour_green:
    top_pipe_path = os.path.join("data", "sprites", "pipes", "top_pipe.png")
    bottom_pipe_path = os.path.join("data", "sprites", "pipes", "bottom_pipe.png")
else:
    top_pipe_path = os.path.join("data", "sprites", "pipes", "top_pipe_red.png")
    bottom_pipe_path = os.path.join("data", "sprites", "pipes", "bottom_pipe_red.png")

# -------------------------------------------------------------------------------------------------
floor_width = 672
floor_x = 0
second_floor_x = floor_x + floor_width

# -------------------------------------------------------------------------------------------------
number0_path = os.path.join("data", "sprites", "numbers", "0.png")
number1_path = os.path.join("data", "sprites", "numbers", "1.png")
number2_path = os.path.join("data", "sprites", "numbers", "2.png")
number3_path = os.path.join("data", "sprites", "numbers", "3.png")
number4_path = os.path.join("data", "sprites", "numbers", "4.png")
number5_path = os.path.join("data", "sprites", "numbers", "5.png")
number6_path = os.path.join("data", "sprites", "numbers", "6.png")
number7_path = os.path.join("data", "sprites", "numbers", "7.png")
number8_path = os.path.join("data", "sprites", "numbers", "8.png")
number9_path = os.path.join("data", "sprites", "numbers", "9.png")
