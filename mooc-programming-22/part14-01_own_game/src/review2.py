
# FlyingMonster is a game where you are flying through space with a monster. 
# The monster likes eating coins. Luckily these coins fly through the space.
# The monster is very hungry, so it needs 50 coins to happy.
# However there are also doors in space. The monster is allergic to wood.
# So it should defenetly avoided that the monster eats doors.
 
import pygame
from random import randint
 
class FlyingMonster:
    def __init__(self):
        pygame.init()
 
        self.load_images()
 
        self.window = pygame.display.set_mode((640, 560))
 
        self.game_font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Flying Monster")
 
        self.speed = 1
        
        self.new_game()
        self.main_loop()
 
    def load_images(self):
        self.images = {}
        for name in ["coin", "door", "monster", "robot"]:
            self.images[name] = (pygame.image.load(name + ".png"))
 
    def new_game(self):
        #######Coins######
        self.coins = []
        for i in range(7):
            coin_x = randint(640, 1200)
            coin_y = randint(0, (560 - self.images["coin"].get_height()))  
            self.coins.append([coin_x, coin_y])
        #######Coins######
        
        #######Doors######
        self.doors = []
        for i in range(7):
            door_x = randint(640, 1200)
            door_y = randint(0, (560 - self.images["door"].get_height()))   
            self.doors.append([door_x, door_y])
        self.door_eaten = False
        #######Doors######
        
        #####Spwan the Monster#####
        self.monster_x = 10    
        self.monster_y = (560 - self.images["monster"].get_height()) / 2
        self.up = False
        self.down = False
        #####Spwan the Monster#####
        
        self.count = 0
        self.clock = pygame.time.Clock()
 
    def main_loop(self):
        while True:
            self.check_events()
            self.eat_coins()
            self.eat_doors()
            self.draw_window()
 
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True
                if event.key == pygame.K_F2:
                    self.speed = 1
                    self.new_game()
                if event.key == pygame.K_F3:
                    self.speed = 2
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False
 
            if event.type == pygame.QUIT:
                exit()
        
        self.window_barriers()
        
    def window_barriers(self): #Monster must stay in window barriers.
        if self.down:
            if self.monster_y > (560 - self.images["monster"].get_height()):
                self.down = False
            self.monster_y += 2
        if self.up:
            if self.monster_y < 0:
                self.up = False
            self.monster_y -= 2
 
    def eat_coins(self):   #Eat coins that touch the monster and spawn new onece.
        for i in range(7):
            if self.coins[i][1] + self.images["coin"].get_height() >= self.monster_y and self.coins[i][1] <= (self.monster_y + self.images["monster"].get_height()):
                if self.coins[i][0] <= self.monster_x + self.images["monster"].get_width():
                    self.coins[i][0] = randint(0, (640 - self.images["coin"].get_height()))
                    self.coins[i][1] = -randint(self.images["coin"].get_height(), 1000)
                    self.count += 1
    
            if self.coins[i][0] < 0:
                self.coins[i][0] = randint(640, 1200)
                self.coins[i][1] = randint(0, (560 - self.images["coin"].get_height()))   
            else: self.coins[i][0] -= 1
 
    def eat_doors(self):   #Eat doors that touch the monster. The game is over after that.
        for i in range(7):
            if self.doors[i][1] + self.images["door"].get_height() >= self.monster_y and self.doors[i][1] <= (self.monster_y + self.images["monster"].get_height()):
                if self.doors[i][0] <= self.monster_x + self.images["monster"].get_width():
                    self.door_eaten = True
    
            if self.doors[i][0] < 0:
                self.doors[i][0] = randint(640, 1200)
                self.doors[i][1] = randint(0, (560 - self.images["door"].get_height()))   
            else: self.doors[i][0] -= 1
        
    def draw_window(self):
        self.window.fill((100, 0, 0)) 
        self.window.blit(self.images["monster"], (self.monster_x, self.monster_y))
        for i in range(7):
            self.window.blit(self.images["coin"], (self.coins[i][0], self.coins[i][1]))
        
        for i in range(7):
            self.window.blit(self.images["door"], (self.doors[i][0], self.doors[i][1]))
        
        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (450, 525))
    
        self.score = self.game_font.render(f"Score: {self.count}", True, (255, 0, 0))
        self.window.blit(self.score, (500, 0))
 
        if self.door_eaten:  #Gameover after eating a door
            self.speed = 1
            self.window.fill((100, 0, 0))
            game_text1 = self.game_font.render("You ate a door. The monster does not like doors.", True, (255, 0, 0))
            game_text2 = self.game_font.render("The game is over. Press F2 to restart.", True, (255, 0, 0))
            pygame.draw.rect(self.window, (0, 0, 0), (50,100, game_text1.get_width(), game_text1.get_height()))
            pygame.draw.rect(self.window, (0, 0, 0), (50, 200, game_text2.get_width(), game_text2.get_height()))
            self.window.blit(game_text1, (50,100))
            self.window.blit(game_text2, (50,200))
 
        if self.game_solved():   #Game won after eating 50 coins
            self.window.fill((100, 0, 0))
            game_text1 = self.game_font.render("Congratulations, you ate 50 coins.", True, (255, 0, 0))
            game_text2 = self.game_font.render("The flying monster is happy!", True, (255, 0, 0))
            game_text3 = self.game_font.render("Press F2 for a new game, F3 for a faster new game!", True, (255, 0, 0))
            pygame.draw.rect(self.window, (0, 0, 0), (50,100, game_text1.get_width(), game_text1.get_height()))
            pygame.draw.rect(self.window, (0, 0, 0), (50, 200, game_text2.get_width(), game_text2.get_height()))
            pygame.draw.rect(self.window, (0, 0, 0), (50, 300, game_text3.get_width(), game_text3.get_height()))
            self.window.blit(game_text1, (50,100))
            self.window.blit(game_text2, (50,200))
            self.window.blit(game_text3, (50,300))
 
        pygame.display.flip()
        self.clock.tick(self.speed * 180)
        self.window.fill((100, 0, 0)) 
    
    def game_solved(self):
        if self.count >= 50:
            return True
 
if __name__ == "__main__":
    FlyingMonster()


