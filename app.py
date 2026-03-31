# importing libraries
import pygame
import time
import random

# Snake Speed Varialble 
snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colours
black = pygame.Color(0, 0, 0)
white = pygame.Color(255,255,255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# initialise game window
pygame.display.set_caption('Jaydos Snake')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Defining snake default position
snake_position = [100, 50]

# Defining first 4 blocks of snake body
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

# Fruit Position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# Setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# Initial Score
score = 0


# Displaying score function
def show_score(choice, color, font, size):
    
    # creating font object score_font
    score_font = pygame.font.SysFont(font,size)

    # Create the display surface object Score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # Create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # Displaying text
    game_window.blit(score_surface, score_rect)


# Game over function
def game_over():

    # Creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # Creating a text surface on which text will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # Setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # Blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # After 2 seconds we will quit the program
    time.sleep(2)

    # Deactivating pygame library
    pygame.quit()

    # Quit the program
    quit()


# Main Function
while True:

    # Handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    # If two keys pressed simultaneously we don't want snake to move into two directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'