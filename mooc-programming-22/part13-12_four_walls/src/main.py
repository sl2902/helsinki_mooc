# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
w, h = 640, 480
window = pygame.display.set_mode((w, h))

robot = pygame.image.load("robot.png")
x = w//2 - robot.get_width()/2
y = h//2 - robot.get_height()/2

to_right = False
to_left = False
up = False
down = False
speed = 5

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
    if  x < 0:
        x = 0
    elif x + robot.get_width() > w:
        x = w - robot.get_width()
    elif y < 0:
        y = 0
    elif y + robot.get_height() > h:
        y = h - robot.get_height()
    else:
        if to_right:
            x += speed
        if to_left:
            x -= speed
        if up:
            y -= speed
        if down:
            y += speed


    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
