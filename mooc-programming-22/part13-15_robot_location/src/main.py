# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
w, h = 640, 480
window = pygame.display.set_mode((w, h))

robot = pygame.image.load("robot.png")
robot_x = random.randint(0, w-robot.get_width())
robot_y = random.randint(0, h-robot.get_height())
target_x = 0
target_y = 0
coord = robot.get_rect()
centerx, centery = coord.centerx, coord.centery

clock = pygame.time.Clock()

while True:
    xmin, ymin = 0, 0
    xmax, ymax = robot.get_width(), robot.get_height()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x = event.pos[0] - robot.get_width() / 2
            target_y = event.pos[1] - robot.get_height() / 2

        if event.type == pygame.QUIT:
            exit(0)

    if abs(robot_x - centerx) < target_x < abs(robot_x + centerx) or abs(robot_y - centery) < target_y < abs(robot_y + centery):
        robot_x = random.randint(0, w-robot.get_width())
        robot_y = random.randint(0, h-robot.get_height())


    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)
