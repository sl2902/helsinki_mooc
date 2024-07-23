# WRITE YOUR SOLUTION HERE:
import pygame
import random
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load('robot.png')

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
x = list(range(0, 640-width))
y = list(range(0, 480-height))
random.shuffle(x)
random.shuffle(y)
for i in range(1000):
    init_x, init_y = random.choice(list(zip(x, y)))
    window.blit(robot, (init_x,  init_y))
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
