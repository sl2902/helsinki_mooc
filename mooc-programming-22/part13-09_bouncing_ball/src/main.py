# WRITE YOUR SOLUTION HERE:
import random
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()

x = random.randint(0, 640-ball.get_width())
y = random.randint(0, 480-ball.get_height())
dx, dy = 1, 1
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # ball_rect = ball_rect.move(dx, dy)
    x += dx
    y += dy
    if x <= 0 or x + ball.get_width() >= 640:
        dx = -dx
    if y <= 0 or y + ball.get_height() >= 480:
        dy = -dy

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))   
    pygame.display.flip()
    clock.tick(60)
