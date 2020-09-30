import sys
import os
import pygame
import math
import constants as c
import random
from colours import *

# Initialises PyGame and declares necessary variables
pygame.init()
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((c.screen_width, c.screen_height))
c.set_bird_pictures()
font = pygame.font.SysFont(None, 44)

# All the variables about the bird that are dependent on PyGame, so they aren't in the constants file
wing_up_image = pygame.image.load(c.wing_up).convert_alpha()
wing_up_image = pygame.transform.smoothscale(wing_up_image, (c.bird_width, c.bird_height))
wing_down_image = pygame.image.load(c.wing_down).convert_alpha()
wing_down_image = pygame.transform.smoothscale(wing_down_image, (c.bird_width, c.bird_height))
wing_mid_image = pygame.image.load(c.wing_mid).convert_alpha()
wing_mid_image = pygame.transform.smoothscale(wing_mid_image, (c.bird_width, c.bird_height))
rotated_bird = wing_up_image

# Background and floor variables
background_image = pygame.image.load(os.path.join("data", "sprites", "background.png")).convert_alpha()
floor = pygame.image.load(os.path.join("data", "sprites", "floor.png")).convert_alpha()
second_floor = pygame.image.load(os.path.join("data", "sprites", "floor.png")).convert_alpha()

# Pipe pictures
top_pipe_image = pygame.image.load(c.top_pipe_path).convert_alpha()
bottom_pipe_image = pygame.image.load(c.bottom_pipe_path).convert_alpha()
top_pipe_rect = top_pipe_image.get_rect()
bottom_pipe_rect = bottom_pipe_image.get_rect()

# Number pictures
number0_image = pygame.image.load(c.number0_path).convert_alpha()
number1_image = pygame.image.load(c.number1_path).convert_alpha()
number2_image = pygame.image.load(c.number2_path).convert_alpha()
number3_image = pygame.image.load(c.number3_path).convert_alpha()
number4_image = pygame.image.load(c.number4_path).convert_alpha()
number5_image = pygame.image.load(c.number5_path).convert_alpha()
number6_image = pygame.image.load(c.number6_path).convert_alpha()
number7_image = pygame.image.load(c.number7_path).convert_alpha()
number8_image = pygame.image.load(c.number8_path).convert_alpha()
number9_image = pygame.image.load(c.number9_path).convert_alpha()
number_image_list = [number0_image, number1_image, number2_image, number3_image, number4_image, number5_image, number6_image, number7_image, number8_image, number9_image]


def check_for_collisions():
    # Is the bird's horizontal position overlapping the first pipes
    if c.pipe_x - c.bird_width <= c.bird_x <= c.pipe_x + c.pipe_width:

        # Checks if hit the bottom pipe
        if c.bird_y + c.bird_height >= c.pipe_y:
            return True

        # Checks if hit the top pipe
        if c.bird_y <= c.pipe_y - c.pipe_gap:
            return True

    # Horizontal for second pipe pair
    if c.second_pipe_x - c.bird_width <= c.bird_x <= c.second_pipe_x + c.pipe_width:
        # Bottom pipe
        if c.bird_y + c.bird_height >= c.second_pipe_y:
            return True

        # Top pipe
        if c.bird_y <= c.second_pipe_y - c.pipe_gap:
            return True

    # Checks if hit the floor
    if c.bird_y + c.bird_height >= c.screen_height - 10:
        return True

    return False


def message_to_screen(msg, colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [c.screen_width // 4 + 25, c.screen_height // 5])


def generate_score_board(score):
    score_length = len(str(score))
    left = 0.5 * c.screen_width
    if score_length == 1:
        left = 0.5 * c.screen_width - 11
    elif score_length % 2 == 0:
        left -= 24 * (score_length // 2)
    else:
        left = 0.5 * c.screen_width - 35
    scoreboard_numbers = [int(i) for i in str(score)]
    return scoreboard_numbers, left


# Game loop.
while not c.ended:
    # Update
    pygame.display.set_caption("Flappy Bird - {} FPS".format(round(clock.get_fps(), 2)))

    if not c.dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not c.unmovable:
                    c.bird_change_y = -8
                elif event.key == pygame.K_s and not c.started:
                    c.bird_change_y = 0
                    c.started = True

        if not c.started:
            # The bird moving up and down at the start
            c.bird_y = (c.screen_height // 2) + 10 * math.sin(c.bird_oscillation_angle)
            c.bird_oscillation_angle += 0.1
            c.bird_oscillation_angle %= 2 * math.pi

        if c.started:
            # Checks if passed the first pipe pair
            if c.pipe_x + c.pipe_width <= c.bird_x + c.bird_width + 2 and c.first_pipe:
                c.first_pipe = False
                c.score += 1

            # Checks if passed the second pipe pair
            if c.second_pipe_x + c.pipe_width <= c.bird_x + c.bird_width + 2 and not c.first_pipe:
                c.first_pipe = True
                c.score += 1

            # Checks if pipe is off-screen to the left, if so then it moves it back to the right side
            if c.pipe_x < -c.pipe_width:
                c.pipe_x = c.second_pipe_x + c.distance_between_pipes
                c.pipe_height = random.randint(25, 450)
                c.pipe_y = c.screen_height - c.pipe_height

            # Same for second pipe pair
            if c.second_pipe_x < -c.pipe_width:
                c.second_pipe_x = c.pipe_x + c.distance_between_pipes
                second_pipe_height = random.randint(25, 450)
                second_pipe_y = c.screen_height - second_pipe_height

            # Checks if floor has gone off-screen
            if c.floor_x < -c.floor_width:
                c.floor_x = c.second_floor_x + c.floor_width
            if c.second_floor_x < -c.floor_width:
                c.second_floor_x = c.floor_x + c.floor_width

            fps = clock.get_fps()
            # Bird is accelerating at 0.4 pixels per frame squared
            c.bird_change_y += 0.4

            # Limits the velocity to 15 pixels per frame
            if c.bird_change_y > 15:
                c.bird_change_y = 15

            # Adds the velocity
            c.bird_y += c.bird_change_y
            c.pipe_x += c.pipe_velocity
            c.second_pipe_x += c.pipe_velocity

            c.floor_x += c.pipe_velocity
            c.second_floor_x += c.pipe_velocity

            # Sets the angle of the bird dependent on the velocity
            if c.bird_change_y < 0:
                c.bird_angle = -4 * c.bird_change_y
            elif 15 > c.bird_change_y > 0:
                c.bird_angle = -4 * c.bird_change_y
            else:
                c.bird_angle = -60

        if check_for_collisions():
            print("ouch")
            c.dead = True

    c.bird_flap_state += 0.5
    c.bird_flap_state %= 30

    if 10 >= c.bird_flap_state > 0:
        rotated_bird = pygame.transform.rotate(wing_up_image, c.bird_angle)
    elif 20 >= c.bird_flap_state > 10:
        rotated_bird = pygame.transform.rotate(wing_mid_image, c.bird_angle)
    elif 30 >= c.bird_flap_state > 20:
        rotated_bird = pygame.transform.rotate(wing_down_image, c.bird_angle)

    # Draw.
    # Flashes white for 5 frames
    if c.frames_while_dead_elapsed <= 60 and c.dead:
        gameDisplay.fill((255, 255, 255))
        c.frames_while_dead_elapsed += 1
        message_to_screen("You Died", red)

    elif not c.dead:
        # Background drawing
        gameDisplay.blit(background_image, [0, 0, c.screen_width, c.screen_height])

        # Draw first pipe pair
        gameDisplay.blit(bottom_pipe_image, [c.pipe_x, c.pipe_y, bottom_pipe_rect[0], bottom_pipe_rect[1]])
        gameDisplay.blit(top_pipe_image, [c.pipe_x, c.pipe_y - c.pipe_gap - 826, bottom_pipe_rect[0], bottom_pipe_rect[1]])

        # Draw second pipe pair
        gameDisplay.blit(bottom_pipe_image, [c.second_pipe_x, c.second_pipe_y, top_pipe_rect[0], top_pipe_rect[1]])
        gameDisplay.blit(top_pipe_image, [c.second_pipe_x, c.second_pipe_y - c.pipe_gap - 826, bottom_pipe_rect[0], bottom_pipe_rect[1]])

        # Draw floor
        gameDisplay.blit(floor, [c.floor_x, c.screen_height - 30, c.floor_width, 50])
        gameDisplay.blit(second_floor, [c.second_floor_x, c.screen_height - 30, c.floor_width, 50])

        # Compute and draw score
        score_on_screen = generate_score_board(c.score)[0]
        left_x = generate_score_board(c.score)[1]

        for number in score_on_screen:
            number_image = number_image_list[number]
            number_rect = number_image.get_rect()
            number_width = number_rect[0]
            number_height = number_rect[1]
            gameDisplay.blit(number_image, [left_x, 0.1 * c.screen_height, number_width, number_height])
            left_x += 24

        # Draw bird
        gameDisplay.blit(rotated_bird, [c.bird_x, c.bird_y, c.bird_width, c.bird_height])

    else:
        c.init()

        c.choose_pipe_colour()
        if c.pipe_colour_green:
            c.top_pipe_path = os.path.join("data", "sprites", "pipes", "top_pipe.png")
            c.bottom_pipe_path = os.path.join("data", "sprites", "pipes", "bottom_pipe.png")
        else:
            c.top_pipe_path = os.path.join("data", "sprites", "pipes", "top_pipe_red.png")
            c.bottom_pipe_path = os.path.join("data", "sprites", "pipes", "bottom_pipe_red.png")

        top_pipe_image = pygame.image.load(c.top_pipe_path).convert_alpha()
        bottom_pipe_image = pygame.image.load(c.bottom_pipe_path).convert_alpha()
        c.set_bird_pictures()

        wing_up_image = pygame.image.load(c.wing_up).convert_alpha()
        wing_up_image = pygame.transform.smoothscale(wing_up_image, (c.bird_width, c.bird_height))
        wing_down_image = pygame.image.load(c.wing_down).convert_alpha()
        wing_down_image = pygame.transform.smoothscale(wing_down_image, (c.bird_width, c.bird_height))
        wing_mid_image = pygame.image.load(c.wing_mid).convert_alpha()
        wing_mid_image = pygame.transform.smoothscale(wing_mid_image, (c.bird_width, c.bird_height))

        rotated_bird = wing_up_image

    if not c.started:
        message_to_screen("Press S to Start", blue)

    pygame.display.update()
    clock.tick(c.fps_target)

pygame.quit()
quit()
