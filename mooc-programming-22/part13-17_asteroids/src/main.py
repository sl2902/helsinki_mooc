# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
rock = pygame.image.load("rock.png")
robot = pygame.image.load("robot.png")

# rock_coord = rock.get_rect()
# robot_coord = robot.get_rect()
# robot_rect = pygame.Rect(*robot.get_rect().center, 0, 0).inflate(100, 100)
 
# number of rocks (the same rocks are reused)
coord = robot.get_rect()
centerx, centery = coord.centerx, coord.centery
number = 10
x = 0
y = height - robot.get_height()
speed = 4
score, life = 0, 1
to_left, to_right = False, False

game_font = pygame.font.SysFont("Arial", 24)
# text = game_font.render(f"Score: {score}", True, (255, 0, 0))

 
# causes the new random start position to be drawn immediately
rocks = [[-1000, height] for i in range(number)]
 
clock = pygame.time.Clock()
while True:
    if life:
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
        for i in range(number):
            if rocks[i][1]+rock.get_height() < height:
                # the rock falls downwards
                rocks[i][1] += 1
            else:
                if rocks[i][0] < -rock.get_width() or rocks[i][0] > width:
                    rocks[i][0] = randint(0,width-rock.get_width())
                    rocks[i][1] = -randint(100, 1000)

        for i in range(number):
            if x - centerx < rocks[i][0] < x + centerx and y - centery < rocks[i][1] < y + centery:
                # print(x - centerx, x + centerx, y - centery, y + centery)
                # print(rocks[i][0], rocks[i][1])
                score += 1
                rocks[i][0] = randint(0,width-rock.get_width())
                rocks[i][1] = -randint(100, 1000)
            
        
        # ensure robot stays within the boundary
        if x < 0:
            x = 0
        elif x + robot.get_width() > width:
            x = width - robot.get_width()

        if to_right:
            x += speed
        if to_left:
            x -= speed
    
        screen.fill((0, 0, 0))
        screen.blit(robot, (x, y))
        scorer = game_font.render(f"Score: {score}", True, (255, 0, 0))
        screen.blit(scorer, (width - scorer.get_width() - 5, 20))
        
        for i in range(number):
            if rocks[:][i][1] + rock.get_height() >= height:
                rocks[i][0] = randint(0,width-rock.get_width())
                rocks[i][1] = -randint(100, 1000)
                life -= 1
                if life == 0:
                    break
            else:
                screen.blit(rock, (rocks[i][0], rocks[i][1]))
        pygame.display.flip()
        
        if life == 0:
            text = game_font.render(f"GAME OVER", True, (255, 0, 0))
            screen.fill((0, 0, 0))
            screen.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
            pygame.display.flip()
        clock.tick(60)
    else:
        screen.fill((0, 0, 0))
        screen.blit(scorer, (width - scorer.get_width() - 5, 20))
        screen.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit()
