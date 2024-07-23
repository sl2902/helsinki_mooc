# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
w, h = 640, 480
window = pygame.display.set_mode((w, h))

robot = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")
x = w//2 - robot.get_width()/2
y = h//2 - robot.get_height()/2

xx = robot2.get_width()/2
yy = robot2.get_height()/2

to_right, d = False, False
to_left, a = False, False
up, w = False, False
down, s = False, False
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
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a = True
            if event.key == pygame.K_d:
                d = True
            if event.key == pygame.K_w:
                w = True
            if event.key == pygame.K_s:
                s = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                a = False
            if event.key == pygame.K_d:
                d = False
            if event.key == pygame.K_w:
                w = False
            if event.key == pygame.K_s:
                s = False

        if event.type == pygame.QUIT:
            exit() 

    
    if to_right:
        x += speed
    if to_left:
        x -= speed
    if up:
        y -= speed
    if down:
        y += speed
    
    if d:
        xx += speed
    if a:
        xx -= speed
    if w:
        yy -= speed
    if s:
        yy += speed

        
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot2, (xx, yy))
    pygame.display.flip()

    clock.tick(60)
