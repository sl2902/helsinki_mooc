
# WRITE YOUR SOLUTION HERE:
import pygame
import random
import math
from  datetime import datetime

pygame.init()
w, h = 640, 480
window = pygame.display.set_mode((w, h))


robot_x = 100
robot_y = 50

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    now = datetime.now().time()
        
    # time = str(now)[:8] 
   
    hrs = now.hour
    mins = now.minute
    secs = now.second

    angle_hr = 2 * math.pi * (hrs + mins / 60 + secs / 3600) / 12 - math.pi / 2
    angle_min = 2 * math.pi * (mins + secs / 60) / 60 - math.pi / 2
    angle_sec = 2 * math.pi * secs / 60 - math.pi / 2
    
    hr_x = (w//2) + math.cos(angle_hr) * (w//2)/4
    hr_y = (h//2) + math.sin(angle_hr) * (w//2)/4
    min_x = (w//2) + math.cos(angle_min) * ((w//2) * 4) // 10
    min_y = (h//2) + math.sin(angle_min) * ((w//2) * 4) // 10
    sec_x = (w//2) + math.cos(angle_sec) * ((w//2) * 5) // 10
    sec_y = (h//2) + math.sin(angle_sec) * ((w//2) * 5) // 10
    # print(sec_x, sec_y)

    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 0, 0), (w//2, h//2), 200, width=5)
    pygame.draw.circle(window, (255, 0, 0), (w//2, h//2), 10, width=0)
    
    pygame.draw.line(window, (0, 0, 255), (hr_x, hr_y), (w//2, h//2), 5)
    pygame.draw.line(window, (0, 0, 255), (min_x, min_y), (w//2, h//2), 3)  
    pygame.draw.line(window, (0, 0, 255), (sec_x, sec_y), (w//2, h//2), 2) 
    # now = datetime.now().time()
    pygame.display.set_caption(str(now)[:8]) 

    # window.blit(text, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)
# import pygame
# import math
# from datetime import datetime
 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
 
# def circle(color: int, radius: int):
#     pygame.draw.circle(screen, color, (middle_x, middle_y), radius)
 
# def hand(length: int, thickness: int, proportion: float):
#     angle = 2*math.pi*proportion-math.pi/2
#     end_x = middle_x+math.cos(angle)*length
#     end_y = middle_y+math.sin(angle)*length
 
#     pygame.draw.line(screen, (0, 0, 255), (middle_x, middle_y), (end_x, end_y), thickness)
 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
 
#     hours = datetime.now().hour%12
#     minutes = datetime.now().minute
#     seconds = datetime.now().second
 
#     pygame.display.set_caption(str(datetime.now().time())[:8])
 
#     screen.fill((0, 0, 0))
 
#     middle_x = width/2
#     middle_y = height/2
 
#     circle((255, 0, 0), 200)
#     circle((0, 0, 0), 195)
#     circle((255, 0, 0), 10)
 
#     hand(185, 1, seconds/60)
#     hand(180, 2, (minutes+seconds/60)/60)
#     hand(150, 5, (hours+minutes/60+seconds/3600)/12)
 
#     pygame.display.flip()