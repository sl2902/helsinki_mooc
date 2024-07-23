import pygame
import random
 
class MultGame:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.w_width = width
        self.w_height = height
        self.window = pygame.display.set_mode((self.w_width, self.w_height))
        self.score = 0
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont("Arial", 30)
        self.load_images()
        self.create_walls()
        self.next_round()
 
 
    def next_round(self):
        self.to_right = False
        self.to_left = False
        self.up = False
        self.down = False
        self.player = Player(self.w_height, self.w_width)
        #generate multiplication task:
        self.task()
        #generate 
        self.rooms = []
        self.doors = []
        for i in range(4):
            self.rooms.append(Room(self.w_width/4*i, 0, self.w_width/4*(i+1), self.w_height / 2 - pygame.image.load("door.png").get_height()/2 ))
            self.doors.append(Door(self.w_width*(1+2*i)/8, self.w_height/2))
        self.main_loop()
 
 
    def main_loop(self):
        while True:
            pygame.display.set_caption(f'{self.n1} * {self.n2} = ?')
            self.check_events()
            self.player_move()
            self.draw_window()
            self.check_colisions()
            self.open_doors()
            self.get_coin()
            self.window.blit(self.player.image, (self.player.rect.x - 5, self.player.rect.y))
            pygame.display.flip()
            self.clock.tick(60)
 
 
    def task(self):
        #two random numbers:
        self.n1 = random.randint(2, 9)
        self.n2 = random.randint(2, 9)
 
        #correct answer:
        self.ans = self.n1*self.n2
 
        #list with 4 choices:
        self.choices = [self.ans] 
        while len(self.choices) < 4:
            n = self.ans+random.randint(-5, 5)
            if n not in self.choices:
                self.choices.append(n)
        random.shuffle(self.choices)
 
 
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False
 
 
    def load_images(self):
        self.images = {}
        for name in ["coin", "door", "monster", "robot"]:
            self.images[name] = pygame.image.load(name + ".png")
 
 
    def create_walls(self):
        self.wall_heigt = self.images['door'].get_height()
        self.wall_width = self.w_width/8 - self.images['door'].get_width()/2 - 10
        self.walls = []
        #generate horisontal walls:
        for i in range(8):
            self.walls.append(pygame.Rect((self.w_width*i//8+(i%2)*(self.images['door'].get_width()//2 + 10), self.w_height//2-self.wall_heigt//2),(self.wall_width, self.wall_heigt)))
        #generate vertical walls:
        for i in range(5):
            self.walls.append(pygame.Rect((self.w_width/4*(i)-5,0),(10,self.w_height/2)))
 
 
    def draw_window(self):
        self.window.fill((224, 224, 224))
        #show score:
        text = self.game_font.render(f'Score: {self.score}', True, (255, 0, 0))
        text_rect = text.get_rect(x = 5, y = self.w_height - 40)
        self.window.blit(text, text_rect)
        #show question:
        text = self.game_font.render(f'{self.n1} * {self.n2} = ?', True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.w_width/2, self.w_height*3/4))
        self.window.blit(text, text_rect)
        for i in range(len(self.choices)):
            #show answers:
            text = self.game_font.render(str(self.choices[i]), True, (255, 0, 0))
            text_rect = text.get_rect(center=(self.w_width*(1+2*i)/8, self.w_height/2 + self.images['door'].get_height()/2 + 10))
            self.window.blit(text, text_rect)
            #draw coin in the correct room:
            if self.choices[i] == self.ans:
                self.coin = self.images['coin'].get_rect()
                self.coin.centerx = self.w_width*(1+2*i)/8
                self.coin.centery = self.w_height / 4
                self.window.blit(self.images['coin'], (self.coin.x, self.coin.y))
            #draw monsters in other roooms:
            else:
                self.window.blit(self.images['monster'], (self.w_width*(1+2*i)/8 - self.images['monster'].get_width() / 2, self.w_height / 4 - self.images['monster'].get_height() / 2))
        #draw black over unoppened rooms:
        for i in range(len(self.doors)):
            if self.doors[i].closed:
                self.window.blit(self.doors[i].image, (self.doors[i].rect.x, self.doors[i].rect.y))
                pygame.draw.rect(self.window, (0,0,0), self.rooms[i].rect)
        #draw walls and doors:
        for wall in self.walls:
            pygame.draw.rect(self.window, (0,0,225), wall)
 
 
    def check_colisions(self):
        #check if collided with a wall (-1 if no collision, otherwise index of wall with which collided)
        collision = self.player.rect.collidelist(self.walls)
        if collision > -1:
            #determine what side of player is collided, stop and bounce back:
            if abs(self.walls[collision].bottom - self.player.rect.top) < 10:
                self.up = False
                self.player.move_down()
            if abs(self.walls[collision].top - self.player.rect.bottom) < 10:
                self.down = False
                self.player.move_up()
            if abs(self.walls[collision].left - self.player.rect.right) < 10:
                self.to_right = False
                self.player.move_left()
            if abs(self.walls[collision].right - self.player.rect.left) < 10:
                self.to_left = False
                self.player.move_right()
 
 
    def open_doors(self):
        #check if collided with a door (-1 if no collision, otherwise index of door with which collided)
        oppened = self.player.rect.collidelist(self.doors)
        if oppened > -1:
            if self.doors[oppened].closed:
                self.doors[oppened].closed = False
                #if wrong door is oppened, player looses 1 point:
                if self.choices[oppened] != self.ans:
                    self.score -=1
 
 
    def get_coin(self):
        #when player reaches coin, he gets +1 score point and new round is started
        if pygame.Rect.colliderect(self.player.rect, self.coin) == True:
            self.score += 1
            self.next_round()
 
 
    def player_move(self):
        if self.to_right and self.player.rect.x < self.w_width - self.player.image.get_width():
            self.player.move_right()
        if self.to_left and 0 < self.player.rect.x:
            self.player.move_left()
        if self.up and self.player.rect.y > 0:
            self.player.move_up()
        if self.down and self.player.rect.y < self.w_height - self.player.image.get_height():
            self.player.move_down()
 
 
class Player:
    def __init__(self, w_height, w_width):
        self.image = pygame.image.load("robot.png")
        self.rect = self.image.get_rect()
        self.rect.x = w_width/2 - self.image.get_width()/2
        self.rect.y = w_height - self.image.get_height()
        self.rect.width -= 10
 
    def move_down(self):
        self.rect.y += 2
 
    def move_up(self):
        self.rect.y += -2
 
    def move_right(self):
        self.rect.x += 2
 
    def move_left(self):
        self.rect.x += -2
 
 
class Room:
    def __init__(self, x1, y1, x2, y2):
        self.rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
 
 
class Door:
    def __init__(self, x, y):
        self.image = pygame.image.load("door.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.closed = True
 
if __name__ == "__main__":
    MultGame(640, 480)