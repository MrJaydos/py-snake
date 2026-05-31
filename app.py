import pygame
import time
import random

snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Jaydos Snake - 2 Player')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

# Player 1: WASD, green, starts left
p1_position = [200, 240]
p1_body = [[200, 240], [190, 240], [180, 240], [170, 240]]
p1_direction = 'RIGHT'
p1_change = 'RIGHT'
p1_score = 0

# Player 2: arrow keys, blue, starts right (facing left)
p2_position = [520, 240]
p2_body = [[520, 240], [530, 240], [540, 240], [550, 240]]
p2_direction = 'LEFT'
p2_change = 'LEFT'
p2_score = 0

fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True


def show_scores():
    font = pygame.font.SysFont('times new roman', 20)
    p1_surf = font.render('P1 (WASD): ' + str(p1_score), True, green)
    p2_surf = font.render('P2 (Arrows): ' + str(p2_score), True, blue)
    game_window.blit(p1_surf, (10, 10))
    p2_rect = p2_surf.get_rect()
    p2_rect.topright = (window_x - 10, 10)
    game_window.blit(p2_surf, p2_rect)


def game_over(winner):
    game_window.fill(black)
    big_font = pygame.font.SysFont('times new roman', 50)
    small_font = pygame.font.SysFont('times new roman', 30)

    if winner == 'draw':
        msg = "It's a Draw!"
        color = white
    elif winner == 'p1':
        msg = 'Player 1 Wins!'
        color = green
    else:
        msg = 'Player 2 Wins!'
        color = blue

    over_surf = big_font.render(msg, True, color)
    over_rect = over_surf.get_rect()
    over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(over_surf, over_rect)

    score_surf = small_font.render(f'P1: {p1_score}   P2: {p2_score}', True, white)
    score_rect = score_surf.get_rect()
    score_rect.midtop = (window_x / 2, window_y / 2)
    game_window.blit(score_surf, score_rect)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()


def is_dead(pos, own_body, other_body):
    if pos[0] < 0 or pos[0] > window_x - 10:
        return True
    if pos[1] < 0 or pos[1] > window_y - 10:
        return True
    for block in own_body[1:]:
        if pos[0] == block[0] and pos[1] == block[1]:
            return True
    for block in other_body:
        if pos[0] == block[0] and pos[1] == block[1]:
            return True
    return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1_change = 'UP'
            if event.key == pygame.K_s:
                p1_change = 'DOWN'
            if event.key == pygame.K_a:
                p1_change = 'LEFT'
            if event.key == pygame.K_d:
                p1_change = 'RIGHT'
            if event.key == pygame.K_UP:
                p2_change = 'UP'
            if event.key == pygame.K_DOWN:
                p2_change = 'DOWN'
            if event.key == pygame.K_LEFT:
                p2_change = 'LEFT'
            if event.key == pygame.K_RIGHT:
                p2_change = 'RIGHT'

    # Validate P1 direction (can't reverse)
    if p1_change == 'UP' and p1_direction != 'DOWN':
        p1_direction = 'UP'
    if p1_change == 'DOWN' and p1_direction != 'UP':
        p1_direction = 'DOWN'
    if p1_change == 'LEFT' and p1_direction != 'RIGHT':
        p1_direction = 'LEFT'
    if p1_change == 'RIGHT' and p1_direction != 'LEFT':
        p1_direction = 'RIGHT'

    # Validate P2 direction (can't reverse)
    if p2_change == 'UP' and p2_direction != 'DOWN':
        p2_direction = 'UP'
    if p2_change == 'DOWN' and p2_direction != 'UP':
        p2_direction = 'DOWN'
    if p2_change == 'LEFT' and p2_direction != 'RIGHT':
        p2_direction = 'LEFT'
    if p2_change == 'RIGHT' and p2_direction != 'LEFT':
        p2_direction = 'RIGHT'

    # Move P1
    if p1_direction == 'UP':
        p1_position[1] -= 10
    if p1_direction == 'DOWN':
        p1_position[1] += 10
    if p1_direction == 'LEFT':
        p1_position[0] -= 10
    if p1_direction == 'RIGHT':
        p1_position[0] += 10

    # Move P2
    if p2_direction == 'UP':
        p2_position[1] -= 10
    if p2_direction == 'DOWN':
        p2_position[1] += 10
    if p2_direction == 'LEFT':
        p2_position[0] -= 10
    if p2_direction == 'RIGHT':
        p2_position[0] += 10

    # P1 body growth and fruit collection
    p1_body.insert(0, list(p1_position))
    if p1_position[0] == fruit_position[0] and p1_position[1] == fruit_position[1]:
        p1_score += 10
        fruit_spawn = False
    else:
        p1_body.pop()

    # P2 body growth and fruit collection
    p2_body.insert(0, list(p2_position))
    if p2_position[0] == fruit_position[0] and p2_position[1] == fruit_position[1]:
        p2_score += 10
        fruit_spawn = False
    else:
        p2_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

    # Render
    game_window.fill(black)

    for pos in p1_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    for pos in p2_body:
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white,
                     pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    d1 = is_dead(p1_position, p1_body, p2_body)
    d2 = is_dead(p2_position, p2_body, p1_body)

    if d1 and d2:
        game_over('draw')
    elif d1:
        game_over('p2')
    elif d2:
        game_over('p1')

    show_scores()
    pygame.display.update()
    fps.tick(snake_speed)
