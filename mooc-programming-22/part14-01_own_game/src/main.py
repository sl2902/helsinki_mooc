# Complete your game here
import pygame
import math
from random import randint, choice

class GetRich:
    """
    A rain of coins
    The player moves the robot to the left and right along the bottom of the screen.
    Coins rain from the sky. The robot must collect these.
    Also monsters rain from the sky. The robot must avoid these.
    """
    width, height = 640, 480

    def __init__(self, 
                lives: int=3, 
                speed: int = 4, 
                num_coins: int = 4,
                num_monsters: int = 3
        ):
        pygame.init()
        self.lives = lives
        self.score = 0
        self.speed = speed
        self.num_coins = num_coins
        self.num_monsters = num_monsters
        self.game_font = pygame.font.SysFont("Arial", 20)
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((GetRich.width, GetRich.height))
        pygame.display.set_caption("Get Rich or Die Trying!")
    
        self.load_sprites()
        self.robot_x = 0
        self.robot_y = GetRich.height - self.sprites['robot'].get_height()
        self.to_left, self.to_right = False, False
        self.escape, self.new_game_start = False, False
        self.pause_counter = -1

        self.game_play()
    
    def load_sprites(self):
        imgs = {'robot': 'robot.png',
        'coin': 'coin.png',
        'monster': 'monster.png'}
        self.sprites = {k: pygame.image.load(imgs[k]) for k in imgs}
    
    def init_coins(self):
        return [[randint(0, GetRich.width - self.sprites['coin'].get_width()), -choice(range(50, 1001, 50))] for i in range(self.num_coins)]
    
    def init_monsters(self):
        return [[randint(0, GetRich.width - self.sprites['monster'].get_width()), -choice(range(100, 1001, 100))] for i in range(self.num_monsters)]

    
    def init_robot(self):
        pass
    
    def game_play(self):
        coins = self.init_coins()
        monsters = self.init_monsters()
        while 1:
            self.check_events()
            if self.has_lives() and not self.escape:
                self.update_window(coins, monsters)
                self.update_robot_coords()
                self.boundary_check()
            elif self.has_lives() and self.escape:
                if self.pause_counter % 2 == 0:
                    self.update_game_play("GAME PAUSED!")
                    self.new_game_start = True
                else:
                    self.escape = False
            elif not self.has_lives():
                self.update_game_play("GAME OVER!")
                self.new_game_start = True
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_SPACE:
                    self.escape = False
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    self.pause_counter += 1
                    self.escape = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
            if event.type == pygame.QUIT:
                exit()
    
    def update_window(self, coins: list, monsters: list):
        for i in range(self.num_coins):
            coins[i][1] += 1
            if coins[i][1] + self.sprites['coin'].get_height() >= GetRich.height:
                coins[i][0] = randint(0, GetRich.width - self.sprites['coin'].get_width())
                coins[i][1] = -choice(range(50, 1001, 50))
            if self.is_coin_collected(i, coins):
                self.update_score()

        for i in range(self.num_monsters):
            monsters[i][1] += 1
            if monsters[i][1] + self.sprites['monster'].get_height() >= GetRich.height:
                monsters[i][0] = randint(0, GetRich.width - self.sprites['monster'].get_width())
                monsters[i][1] = -choice(range(100, 1001, 100))
            if self.is_monster(i, monsters):
                self.update_lives()

        self.window.fill((211, 211, 211))
        # display the coins
        for i in range(self.num_coins):
            self.window.blit(self.sprites['coin'], (coins[i][0], coins[i][1]))
        # display the monsters
        for i in range(self.num_monsters):
            self.window.blit(self.sprites['monster'], (monsters[i][0], monsters[i][1]))
        # display help, robot, score and lives
        self.window.blit(self.sprites['robot'], (self.robot_x, self.robot_y))
        self.display_help()
        self.display_counter()
        pygame.display.flip()
        self.clock.tick(60)
    
    def get_robot_coords(self):
        return (self.robot_x, self.robot_y)
    
    def set_robot_x_coords(self, x: int):
        self.robot_x = x
        # self.robot_y = y
    
    def update_robot_coords(self):
        robot_x, robot_y = self.get_robot_coords()
        if self.to_right:
            self.set_robot_x_coords(robot_x + self.speed)
        if self.to_left:
            self.set_robot_x_coords(robot_x - self.speed)
    
    def boundary_check(self):
        robot_x, robot_y = self.get_robot_coords()
        if robot_x < 0:
            self.set_robot_x_coords(0)
        elif robot_x + self.sprites['robot'].get_width() > GetRich.width:
            self.set_robot_x_coords(GetRich.width - self.sprites['robot'].get_width())
    
    def is_coin_collected(self, idx: int, coins: list):
        robot_x, robot_y = self.get_robot_coords()
        if coins[idx][1] + self.sprites['coin'].get_height() >= robot_y:
            robot_center = robot_x + self.sprites['robot'].get_width() / 2
            coin_center = coins[idx][0] + self.sprites['coin'].get_width() / 2
            if abs(robot_center - coin_center) <= (self.sprites['robot'].get_width() + self.sprites['coin'].get_width()) / 2:
                coins[idx][0] = randint(0, GetRich.width - self.sprites['coin'].get_width())
                coins[idx][1] = -choice(range(50, 1001, 50))
                return True
        return False
    
    def is_monster(self, idx:int , monsters: list):
        robot_x, robot_y = self.get_robot_coords()
        if monsters[idx][1] + self.sprites['monster'].get_height() >= robot_y:
            robot_center = robot_x + self.sprites['robot'].get_width() / 2
            monster_center = monsters[idx][0] + self.sprites['monster'].get_width() / 2
            if abs(robot_center - monster_center) <= (self.sprites['robot'].get_width() + self.sprites['monster'].get_width()) / 2:
                monsters[idx][0] = randint(0, GetRich.width - self.sprites['monster'].get_width())
                monsters[idx][1] = -choice(range(100, 1001, 100))
                return True
        return False
    
    def display_help(self):
        scorer = self.game_font.render(f"Spacebar - New", True, (255, 0, 0))
        self.window.blit(scorer, (scorer.get_width()//2 - 70, 20))
        if self.pause_counter % 2 == 0:
            life_counter = self.game_font.render("Esc - Resume", True, (255, 0, 0))
        else:
            life_counter = self.game_font.render("Esc - Pause", True, (255, 0, 0))
        self.window.blit(life_counter, (scorer.get_width()//2 + life_counter.get_width()//2 + 25, 20))
    
    def display_counter(self):
        scorer = self.game_font.render(f"Score: {self.score}", True, (255, 0, 0))
        self.window.blit(scorer, (GetRich.width - 151 - scorer.get_width()//2, 20))
        life_counter = self.game_font.render(f"Lives: {self.has_lives()}", True, (255, 0, 0))
        self.window.blit(life_counter, (GetRich.width - 151 - life_counter.get_width() + scorer.get_width() + 40, 20))
    
    def update_game_play(self, mesg: str):
        text = self.game_font.render(mesg, True, (255, 0, 0))
        self.window.fill((211, 211, 211))
        self.window.blit(text, (GetRich.width//2 - text.get_width()//2, GetRich.height//2 - text.get_height()//2))
        self.display_help()
        self.display_counter()
        pygame.display.flip()
    
    def update_score(self):
        self.score += 1
    
    def update_lives(self):
        if self.lives != 0:
            self.lives -= 1
    
    def has_lives(self):
        return self.lives
    
    def new_game(self):
        if self.new_game_start:
            new_game = GetRich()
            new_game.load_sprites()
            new_game.game_play()
            self.new_game_start = False

if __name__ == "__main__":
    GetRich()

