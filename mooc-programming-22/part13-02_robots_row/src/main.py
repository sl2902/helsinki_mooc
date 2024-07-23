# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load('robot.png')

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
init_x, init_y = 30, 50
for _ in range(10):
    window.blit(robot, (init_x, init_y))
    init_x += width
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
