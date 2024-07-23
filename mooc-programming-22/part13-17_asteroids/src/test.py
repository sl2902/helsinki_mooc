import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
pygame.display.set_caption("Asteroids")
 
robot = pygame.image.load("robot.png")
x = 0
y = height-robot.get_height()
 
rock = pygame.image.load("rock.png")
number = 5
positions = []
for i in range(number):
    positions.append([randint(0,width-rock.get_width()),-randint(100,1000)])
 
to_right = False
to_left = False
 
points = 0
 
clock = pygame.time.Clock()
 
font = pygame.font.SysFont("Arial", 24)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
 
        if event.type == pygame.QUIT:
            exit()
 
    if to_right:
        x += 2
    if to_left:
        x -= 2
 
    for i in range(number):
        positions[i][1] += 1
        if positions[i][1]+rock.get_height() >= height:
            # game ends
            exit()
        if positions[i][1]+rock.get_height() >= y:
            robot_middle = x+robot.get_width()/2
            rock_middle = positions[i][0]+rock.get_width()/2
            if abs(robot_middle-rock_middle) <= (robot.get_width()+rock.get_width())/2:
                # the robot caught an asteroid
                positions[i][0] = randint(0,width-rock.get_width())
                positions[i][1] = -randint(100,1000)
                points += 1
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    for i in range(number):
        screen.blit(rock, (positions[i][0], positions[i][1]))
 
    text = font.render("Points: "+str(points), True, (255, 0, 0))
    screen.blit(text, (width-150, 10))
 
    pygame.display.flip()
 
    clock.tick(60)