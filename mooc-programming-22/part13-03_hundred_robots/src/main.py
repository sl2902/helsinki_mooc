# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load('robot.png')

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
init_x, init_y = 40, 50
for i in range(10):
    for j in range(10):
        window.blit(robot, (width + (width * .8 * j) + (10 * i), height + 20 * i))
    # init_x += 4
    # init_y += 1
    #rotated_robot = pygame.transform.rotate(robot, 30)
    #window.blit(rotated_robot, (init_x*(j + 1), init_y*(i + 1)))
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()