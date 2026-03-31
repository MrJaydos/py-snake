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

