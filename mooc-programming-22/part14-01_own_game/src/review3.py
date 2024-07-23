import math
import pygame
 
WIDTH = 40
HEIGHT = 30
 
TILE_SIZE = 20
 
 
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))
    pygame.display.set_caption("DDA")
    clock = pygame.time.Clock()
 
    maze = [[False] * WIDTH for _ in range(HEIGHT)]
    player_x = WIDTH * TILE_SIZE // 2 + TILE_SIZE // 2
    player_y = HEIGHT * TILE_SIZE // 2 + TILE_SIZE // 2
 
    mouse_x = 0
    mouse_y = 0
 
    while True:
 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        if keys[pygame.K_SPACE]:
            maze[mouse_y // TILE_SIZE][mouse_x // TILE_SIZE] = True
        if keys[pygame.K_LEFT]:
            player_x -= TILE_SIZE
        if keys[pygame.K_RIGHT]:
            player_x += TILE_SIZE
        if keys[pygame.K_UP]:
            player_y -= TILE_SIZE
        if keys[pygame.K_DOWN]:
            player_y += TILE_SIZE
 
        screen.fill((0, 0, 180))
 
        for y in range(HEIGHT):
            for x in range(WIDTH):
                c = (0, 0, 0) if maze[y][x] else (0,0,128)
                pygame.draw.rect(screen, c, (x * TILE_SIZE + 1, y * TILE_SIZE + 1, TILE_SIZE - 2, TILE_SIZE - 2))
 
        pygame.draw.circle(screen, (255, 255, 0), (player_x, player_y), 5)
        pygame.draw.circle(screen, (0, 255, 0), (mouse_x, mouse_y), 5)
 
        # DDA
        angle = math.atan2(mouse_y - player_y, mouse_x - player_x)
        dx = math.cos(angle)
        dy = math.sin(angle)
 
        step_size_y, step_size_x = (math.sqrt(1 - dy ** 2) * TILE_SIZE, math.sqrt(1 - dx ** 2) * TILE_SIZE)
 
        start_x = player_x
        start_y = player_y
 
        ray_length_x = 0
        ray_length_y = 0
 
        # Offset from tile top-left corner
        col = int(player_x // TILE_SIZE)
        row = int(player_y // TILE_SIZE)
        if dx < 0:
            ray_length_x = (start_x - (col * TILE_SIZE))
        else:
            ray_length_x = ((col + 1) * TILE_SIZE - start_x)
        if dy < 0:
            ray_length_y = (start_y - (row * TILE_SIZE))
        else:
            ray_length_y = ((row + 1) * TILE_SIZE - start_y)
 
        tile = []
        distance = 0
        while distance < max((WIDTH * TILE_SIZE), (HEIGHT * TILE_SIZE)):
 
            if ray_length_x < ray_length_y:
                # Increase
                distance = ray_length_x
                ray_length_x += step_size_x
 
            else:
                distance = ray_length_y
                ray_length_y += step_size_y
 
            _xy = [
                start_x + distance * dx,
                start_y + distance * dy,
            ]
 
            col = int(_xy[0] // TILE_SIZE)
            row = int(_xy[1] // TILE_SIZE)
 
            #pygame.draw.circle(screen, (100, 0, 0), _xy, 5)
 
            try:
                if not (0 < col < WIDTH) or not (0 < row < HEIGHT):
                    break
                if maze[row][col]:
                    tile = [
                        col * TILE_SIZE,
                        row * TILE_SIZE,
                    ]
                    break
            except IndexError:
                print("OUT OF BOUNDS")
                break
 
        pygame.draw.line(screen, (255, 0, 0), (player_x, player_y), (mouse_x, mouse_y), 1)
 
        if len(tile):
            target = [
                start_x + distance * dx,
                start_y + distance * dy,
            ]
            print(step_x, step_y, target, (dx, dy))
 
            pygame.draw.line(screen, (0, 255, 0), (start_x, start_y), target, 5)
 
            #pygame.draw.line(screen, (255, 0, 0), (start_x, start_y), target)
            pygame.draw.rect(screen, (255, 255, 0), (tile[0], tile[1], TILE_SIZE, TILE_SIZE))
 
        pygame.display.update()
        pygame.display.flip()
        clock.tick(10)
 
if __name__ == "__main__":
    main()
 


