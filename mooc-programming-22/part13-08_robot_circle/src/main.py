# WRITE YOUR SOLUTION HERE:
import pygame
import math
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
angle = 0
clock = pygame.time.Clock()
num = 10
def generate_robots(num: int=10, width: int=320, height: int=240, 
                    angle: float=0, radius: int=100, offset: int=0) -> list:
    coord = []
    for i in range(num):
        x = width + math.cos(angle + offset*i) * radius - robot.get_width() / 2
        y = height + math.sin(angle + offset*i) * radius - robot.get_height() / 2
        coord.append((x, y))
        offset = (36*math.pi) / 180
    return coord
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    coord = generate_robots(num=num, angle=angle, radius=150)
    window.fill((0, 0, 0))
    for i in range(num):
        x, y = coord[i][0], coord[i][1]
        window.blit(robot, (x, y))   
    pygame.display.flip()
    angle += .01
    clock.tick(60)
