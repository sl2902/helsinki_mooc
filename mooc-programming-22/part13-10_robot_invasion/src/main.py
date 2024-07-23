# WRITE YOUR SOLUTION HERE:
import random
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

direction, velocity = 1, 1
num = random.choice([1, 15])
clock = pygame.time.Clock()

def build_robots(lb: int=0, ub: int=5):
    coords = []
    # for i in range(random.randint(lb, ub)):
    for _ in range(ub):
        coords.append([[random.randint(0, 640-robot.get_width()), random.randint(100, 1000) * -1], 1])
    return coords

coords = build_robots(num)
to_remove = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if len(coords) < 5:
        coords.extend(build_robots(ub=num))
    window.fill((0, 0, 0))
    for i in range(len(coords)):
        # print(coords[i])
        window.blit(robot, tuple(coords[i][0]))

        if coords[i][1] == 1:
            coords[i][0][1] += velocity
            # if coords[i][0][1] > 240:
            #     coords.extend(build_robots(ub=num)[:1])
            if coords[i][0][1] + robot.get_height() >= 480:
                # direction
                coords[i][1] = 2
        elif coords[i][1] == 2:
            lr = -velocity if coords[i][0][0] < 320 else velocity
            coords[i][0][0] += lr
            if coords[i][0][0] <= 0 or coords[i][0][0] + robot.get_width()>= 640:
                # print(i, 'floor')
                to_remove.append(coords[i])
                if len(to_remove) >= 5:
                    coords[:] = [coord for i, coord in enumerate(coords) if coord not in to_remove]
                    to_remove = []
                    break
    pygame.display.flip()
    clock.tick(60)
