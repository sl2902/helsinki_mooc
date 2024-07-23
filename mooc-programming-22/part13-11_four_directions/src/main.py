# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 320 - robot.get_width()/2
y = 240 - robot.get_height()/2

to_right = False
to_left = False
up = False
down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False

        if event.type == pygame.QUIT:
            exit()
        
    if x >= 640 or x <= 0 or y <= 0 or y >= 480:
        x = 320
        y = 240
        continue 

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if up:
        y -= 2
    if down:
        y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
