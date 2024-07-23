# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 5
clock = pygame.time.Clock()
x_left, y_right = True, False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if x_left:
        x += velocity
    if velocity > 0 and x+robot.get_width() >= 640:
        x = 640 - robot.get_width() 
        y += velocity
        # print('first', x, y, velocity)
    if velocity > 0 and y+robot.get_height() >= 480:
        velocity = -velocity
        # print('second', x, y, velocity)
    if velocity < 0 and x <= 0:
        # velocity = velocity
        x_left = False
        y += velocity
        # print('third', x, y, velocity)
    if velocity < 0 and y <= 0:
        velocity = -velocity
        x_left = True

    clock.tick(60)
