"""
teemu was alone
===============
 
Pygame made for Mooc Programming 2022 part 14.
<https://programming-22.mooc.fi/part-14>
 
Copyright (c) 2022 Teemu Autto <mooc.fi@teemu.rautakuu.org>
 
How to play
===========
 
Find your way out of series of dark tiled mazes using the arrow keys. It's
an allegory for life.
 
You are not alone.
 
Assigment requirements:
=======================
 
 * The game has a sprite the player can move in some way
 
 -> Player has as square as as sprite, which can be moved around
    with the arrow keys or wasd.
 
 * The game has some collectable items and/or enemies
 
 -> In darkness lurks voids, that start to move when player approaches
    them. They can be regarded as enemies. But the real enemy is the
    darkness inside you!
 
    Also player "collects" exits, which triggers the next level.
 
 * The player needs to be set a clear task in the game
 
 -> Premise is simple; Player needs to find enough exits to reach the end of the maze.
 
 * The game contains a counter which tells the player how they are doing in the game
 
 -> After finding the exit, the icon is added into hud (bottom right).
    After finding all exits, the game enters the outro sequence. Direct numerical
    counter doesn't exist, so the player has to count icons themselves. Enabling debug
    mode (F11) displays numerical info.
 
 * The source code for the game is divided into functions like in the Sokoban example.
 
    Very good, very professional like sokoban. Much source, excessive amount of
    functions and classes.
 
 
Additional notes:
=================
 
Game is inspired by Pac-Man and Thomas was alone.
From packman specially the "enemy" behaviour is copied, and from thomas was
alone the obvious blocky style with shadows.
 
Detecting visible walls is done using DDA raycasting
(https://lodev.org/cgtutor/raycasting.html). Naive raycasting is left as
and obsolete artifact. Some trickery going on as plain python is lacking
on matrix operations.
 
To keep movement constant, movement is calculated using the time between
frame updates.
 
Mazes are not guaranteed to be solvable, but due to the sparse nature of them,
it's highly unlikely to happen.
 
Some places should use Vector2, but it was discovered too late in development
process.
 
Location and position terms are used quite a wildly, and in hindsights location
should be used when talking on tiles, and position about pixels.
"""
 
from enum import Enum
import math
import random
import sys
from typing import List, Tuple
import pygame
from pygame import Vector2
 
 
class GameState(Enum):
    """
    Game states, which are used on main loop.
    """
    QUIT = 0x00  # Not used.
    INTRO = 0x01
    INIT = 0x02
    PLAYING = 0x03
    CREDITS = 0x04
    DEFEAT = 0x04  # Separate state not implemented
    COMPLETED = 0x05
    OUTRO = 0x06
 
 
class IntroState(pygame.sprite.Sprite):
    """
    Initial screen.
    """
 
    def __init__(self) -> None:
 
        self.image = pygame.Surface(pygame.display.get_window_size())
        self.rect = self.image.get_rect()
 
        self.time = 0
        super().__init__()
 
    def update(self, updated) -> None:
        """
        Function that updates the sprite on every cycle.
        """
 
        self.time += updated
 
        game_font = pygame.font.SysFont("Arial", 48)
 
        # Lots' of artistic things follows.
        offset_x = 30
        offset_y = self.image.get_height() * 0.60
 
        scale = max(0, (self.time / 3000) - 0.5)
        scale = 1 + scale * scale
 
        tint = min(1, (scale - 1) / 3)
        color = [c - c * tint for c in (255, 255, 255)]
 
        text_teemu = game_font.render("teemu was ", True, (255, 255, 255))
        text_alone = game_font.render("alone", True, color)
 
        text_teemu = pygame.transform.rotate(text_teemu, 2)
        text_alone = pygame.transform.rotate(text_alone, 2)
        text_alone = pygame.transform.scale(text_alone, (text_alone.get_width(),
                                                         text_alone.get_height() * scale))
 
        self.image.fill((0, 0, 0))
        self.image.blit(text_teemu, (offset_x, offset_y))
        self.image.blit(text_alone, (text_teemu.get_width() + offset_x,
                                     offset_y + scale * 3))
 
        # Draw player character and cursor pointing to it
        # to help player discover who is he.
        player_character = PlayerObject(Game.TILE_SIZE)
        pos = Game.player_default_location()
        self.image.blit(player_character.image, pos)
        offset = Vector2(player_character.width / 2, -1)
        triangle = [v + pos + offset for v in (Vector2(-4, -4),
                                               Vector2(4, -4),
                                               Vector2(0, 0))]
        pygame.draw.polygon(self.image, color=color, points=triangle)
 
        return super().update()
 
 
class GameObject(pygame.sprite.Sprite):
    """
    Base class for interactive objects.
 
    Usage is not constant and probably violates Liskov substitution principle.
 
 
    The x and y is properties are not used directly from rect, as it only supports integers,
    ergo own accessors.
    """
 
    SYMBOL: str
    "Indicates symbol used to represent object on map"
 
    def __init__(self, size=None) -> None:
        """
        GameObject constructor.
 
        :param size: Size of the object in pixels.
        """
        super().__init__()
 
        self._position = Vector2()
        self._move_direction = Vector2(0, 0)
 
        # speed the object can move when direction is 1.
        self.speed = 50
 
        self.time = 0.
 
        if size is None:
            self.size = (Game.TILE_SIZE, Game.TILE_SIZE)
        elif isinstance(size, (int, float)):
            self.size = (size, size)
        else:
            self.size = size
 
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
 
    @property
    def width(self) -> int:
        return self.rect.width
 
    @property
    def height(self) -> int:
        return self.rect.height
 
    @property
    def x(self) -> float:
        return self._position[0]
 
    @property
    def y(self) -> float:
        return self._position[1]
 
    @x.setter
    def x(self, value: float) -> None:
        self._position[0] = value
        self.rect.x = value
 
    @y.setter
    def y(self, value: float) -> None:
        self._position[1] = value
        self.rect.y = value
 
    def move_direction(self, towards) -> None:
        """
        Set movement direction, and clamp it to [-1, 1]
        """
        self._move_direction[0] = max(-1, min(1, towards[0]))
        self._move_direction[1] = max(-1, min(1, towards[1]))
        return
 
    def target_position(self):
        """
        Get relative target position for object.
        """
 
        pos = self._move_direction.copy()
 
        try:
            pos.scale_to_length(self.speed)
        except ValueError:
            # scaling zero value, ignore.
            pass
 
        return pos
 
    def get_location(self, frame_ms=0) -> Vector2:
        """
        Get location a [x, y] vector
 
        :param frame_ms: time is ms to use as speed factor.
        """
        if frame_ms == 0:
            return self._position
        else:
            timeslice = frame_ms / 1000
            return self._position + self.target_position() * timeslice
 
    def update(self, updated) -> None:
 
        # Use time slice to indicate how far move object, as fps might not be constant
        self.x, self.y = self.get_location(updated)
 
        super().update()
 
 
class VoidObject(GameObject):
    """
    Thing that lurks in the dark.
    """
    SYMBOL = "O"
 
    def __init__(self, size=None) -> None:
 
        # Void objects are a bit smaller than standard tile,
        # so I can bypass implementing sub-stepping.
        if size is None:
            size = Game.TILE_SIZE * 0.9
 
        super().__init__(size)
 
        self.speed = self.speed * 0.6
 
        self.image.fill((0, 0, 0))
        self.active = False
 
    def update(self, updated, mask: List[List[float]]) -> None:
        """
        Update method for VoidObject.
 
        :param updated: time since last update in ms.
        :param mask: ray-tracing mask. Used to determine if object seen.
        """
 
        x, y = self.get_location(updated)
        x = int(x // Game.TILE_SIZE)
        y = int(y // Game.TILE_SIZE)
 
        if mask[y][x] > 0:
            self.active = True
            # If seen, stay put and hope player doesn't notice.
            self.move_direction((0, 0))
 
        return super().update(updated)
 
 
class PlayerObject(GameObject):
    """
    Player character representation.
    """
 
    SYMBOL = "@"
    FOV: float = math.pi / 3
    "Field of view of the player character"
 
    def __init__(self, size=None) -> None:
 
        if size is None:
            size = Game.TILE_SIZE
 
        # Make player character a bit less square.
        size = (size * 0.5, size * 0.8)
        super().__init__(size)
 
        self.view_angle: float = 0.
 
        self.color = (232, 84, 41)
        self.image.fill(self.color)
 
        self.rect = pygame.Rect(0, 0, *self.size)
 
    def move_direction(self, towards) -> None:
        # When moving, rotate player character to face direction.
        if any(towards):
            self.view_angle = math.atan2(*towards[::-1])
 
        return super().move_direction(towards)
 
 
class MazeTile(pygame.sprite.Sprite):
    """
    Base class for tiles.
    """
 
    SYMBOL: str
    grid_pos: Tuple[int, int]
    "Tile position on the maze grid"
 
    def __init__(self, position: Tuple[int, int], size=None):
        super().__init__()
        if size is None:
            size = Game.TILE_SIZE
 
        self.grid_pos = (-1, -1)
        self.size = (size, size)
 
        # Indicates how bright the tile is.
        self.intensity = 0.
 
        self.image = pygame.Surface(self.size)
        self.rect = pygame.Rect(*position, *self.size)
 
    def update(self, updated=0, view_mask=None) -> None:
        """
        Updates tile brightness based on view mask.
        """
 
        x, y = self.grid_pos
 
        if view_mask and float("inf") > view_mask[y][x] > 0:
            i = view_mask[y][x]
            self.intensity = 1 - math.sin(math.pi / 2 * i)
        else:
            # If not in view, dim it slowly (1s)
            self.intensity = max(0, self.intensity - updated / 1000)
 
        # Dim color. Better way would be to use colorsys and hsl, but good
        # enough for the girls I go out with. Or boys.
        color = [min(255, int(c * self.intensity)) for c in self.color]
        self.image.fill(color)
 
        return super().update(updated)
 
 
class WallTile(MazeTile):
    SYMBOL = "#"
 
    def __init__(self, *args, **kwargs):
        # Better colour might be in need.
        self.color = (200, 200, 200)
        super().__init__(*args, **kwargs)
 
 
class FloorTile(MazeTile):
    SYMBOL = " "
 
    def __init__(self, *args, **kwargs):
        # Add some randomness to the color.
 
        self.color = [c + random.randint(0, 4) for c in (52, 62, 64)]
        super().__init__(*args, **kwargs)
 
 
class InvisibleWall(FloorTile):
    """
    Like wall, but used as a placeholder for walls that are not visible.
 
    Used to make final 1d sequence without needing to change the movement code.
    """
    SYMBOL = "X"
 
 
class DoorTile(MazeTile):
    SYMBOL = ">"
 
    def __init__(self, position, size, color):
        self.color = color
        size = size - 2
        position = (position[0] + 1, position[1] + 1)
        super().__init__(position, size)
 
    def update(self, *args, **kwargs) -> None:
        # After founding, doors are always visible
        if self.intensity > 0:
            self.intensity = 1
 
        super().update(*args, **kwargs)
 
 
class TileTypes:
    """
    List of tile behaviours and their corresponding symbols.
 
    Notice that they are sets, so common set operations can be used, ie.
    intersection two sets to see if there is a common element.
    """
 
    OPAQUE = {WallTile.SYMBOL, VoidObject.SYMBOL}
    "Tiles that block ray-tracing"
 
    TRANSPARENT = {FloorTile.SYMBOL, DoorTile.SYMBOL, InvisibleWall.SYMBOL}
 
    BLOCKING = {WallTile.SYMBOL, InvisibleWall.SYMBOL}
    "Prevents moving into tile"
 
 
class TextSprite(pygame.sprite.Sprite):
    """
    Text message generator.
    """
 
    FADE_SPEED = 700
 
    font: pygame.font.Font
 
    def __init__(self, text) -> None:
        self.font = pygame.font.SysFont("sans-serif", 20)
        self.image = self.font.render(text, True, (240, 240, 240))
        self.rect = self.image.get_rect()
 
        self.rect.x = Game.TILE_SIZE
        self.rect.y = Game.TILE_SIZE * Game.MAZE_SIZE[1] * 0.75
 
        self.time = 0
 
        # Approximate how long the text should be visible.
        self.ttl = len(text) * 55 + (self.FADE_SPEED * 2)
 
        super().__init__()
 
    def update(self, updated, *args) -> None:
        """
        Fade text in and out.
        """
        self.time += updated
 
        if self.time < self.FADE_SPEED:
            alpha = min(255, self.time * 255 / self.FADE_SPEED)
        elif self.time > self.ttl:
            alpha = 0
            self.kill()
        elif self.time > (self.ttl - self.FADE_SPEED):
            alpha = min(255, 255 - (self.time - (self.ttl - self.FADE_SPEED)) / self.FADE_SPEED * 255)
        else:
            alpha = 255
 
        self.image.set_alpha(alpha)
        super().update(updated, *args)
 
 
class LevelText(TextSprite):
    """
    Class for story element texts.
    """
 
    LEVEL_TEXTS = [
        "From the darkness he tried to find something.",
        "And in the darkness he found void.",
        "More he observer the darkness, the more void filled it.",
        "Void could not be argued with. Void could not be reasoned with. And Void doesn't feel pity.",
        "At least he had become good at finding something.",
        "Maybe he was just looking in the wrong place."
    ]
 
    def __init__(self, level) -> None:
        text = self.LEVEL_TEXTS[level - 1]
        super().__init__(text)
 
 
class Game:
    """
    Main game class.
    """
 
    state: GameState
    "Current game state"
    maze: List[List[str]]
    "Maze matrix"
 
    TILE_SIZE = 20
    "Tile size in pixels"
 
    MAZE_SIZE = (40, 20)
    "Maze size in tiles"
 
    RAYS = 50
    "Number of rays for ray-tracing"
 
    DOORS = [
        (247, 137, 47),
        (253, 206, 46),
        (85, 140, 55),
        (145, 212, 224),
        (47, 128, 199),
        (118, 44, 178)
    ]
    "Door colors"
 
    def __init__(self):
        """
        Initialize common constants
        """
        # vector for size in pixels
        size = Vector2(self.MAZE_SIZE[0] * self.TILE_SIZE,
                       self.MAZE_SIZE[1] * self.TILE_SIZE)
    
        # Maximum length for ray-tracing, from corner to corner.
        self.MAX_RAY_LENGTH = math.sqrt(size[0] ** 2 + size[1] ** 2)
 
        # Debug toggle and layer
        self.debug = False
        self.debug_surface = pygame.Surface(size)
        self.debug_surface.set_colorkey((0, 0, 0))
 
        # Initialize pygame stuff
        self.window = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Programming-22 - Game project - teemu was alone")
 
        # SysFonts needs pygame.init(), so done in main loop
        self.font: pygame.font.Font  # = pygame.font.Font("monospace", 12)
 
        # Initialize game layers
        self.player_layer = pygame.sprite.GroupSingle()
        self.void_layer = pygame.sprite.Group()
        self.exit_layer = pygame.sprite.Group()
        self.maze_layer = pygame.sprite.Group()
        self.hud_layer = pygame.sprite.Group()
 
        # Should be in main loop, and without own layer. But this is easier.
        self.intro = pygame.sprite.GroupSingle()
        self.intro.add(IntroState())
 
        # Game state
        self.state = GameState.INTRO
        self.maze = []
        self.level = 1
        self.level_timer = 0
 
    @staticmethod
    def player_default_location():
        """
        Default player location in pixels.
 
        Defaults to the center of the maze.
        """
        return Vector2(Game.MAZE_SIZE[0] // 2 * Game.TILE_SIZE,
                       Game.MAZE_SIZE[1] // 2 * Game.TILE_SIZE)
 
    def render_maze(self):
        """
        Generate maze sprites and add them to the maze_layer.
        """
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                tile = self.render_tile(x, y, self.maze[y][x])
 
                self.maze_layer.add(tile)
 
                if tile.SYMBOL == DoorTile.SYMBOL:
                    # Doors are on different layer, so they can be easily collided with.
                    self.exit_layer.add(tile)
 
    def render_tile(self, x, y, tile_symbol):
        tile: MazeTile
        position = (x * self.TILE_SIZE, y * self.TILE_SIZE)
 
        # not handled: player character; voids. They are added dynamically.
        if tile_symbol in [FloorTile.SYMBOL, VoidObject.SYMBOL]:
            tile = FloorTile(position, self.TILE_SIZE)
        elif tile_symbol == WallTile.SYMBOL:
            tile = WallTile(position, self.TILE_SIZE)
        elif tile_symbol == InvisibleWall.SYMBOL:
            tile = InvisibleWall(position, self.TILE_SIZE)
        elif tile_symbol == DoorTile.SYMBOL:
            tile = DoorTile(position, self.TILE_SIZE, self.DOORS[self.level - 1])
        else:
            raise RuntimeError(f"Unknown tile symbol: {tile_symbol}")
 
        tile.grid_pos = (x, y)
 
        return tile
 
    def move_player(self) -> None:
        """
        Move player according player input events.
        """
 
        keys = pygame.key.get_pressed()
 
        # Vector [x, y] for movement direction.
        direction = Vector2(0, 0)
 
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction[0] = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            direction[0] = 1
 
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            direction[1] = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            direction[1] = 1
 
        self.player_object.move_direction(direction)
        self.movement_collision(self.player_object)
 
    def move_voids(self) -> None:
        """
        Moves voids.
 
        Copies behaviour from Pac-man ghosts.
        Depending on their placement on the sprite layer, every other
        is moved towards the player, and every other is moved towards
        the opposite side of player.
 
        """
        voids = self.void_layer.sprites()
        player_x, player_y = self.player_object.rect.center
 
        for i, void in enumerate(voids):
            if not void.active:
                continue
 
            if i % 2 == 0:
                # Basic void, track player
                void_x, void_y = void.rect.center
 
                x = player_x - void_x
                y = player_y - void_y
            else:
                # Track opposite side of player
                opposite_void_x, opposite_void_y = voids[i - 1].rect.center
 
                opposite_x = player_x + (player_x - opposite_void_x)
                opposite_y = player_y + (player_y - opposite_void_y)
                
                void_x, void_y = void.rect.center
                x = opposite_x - void_x
                y = opposite_y - void_y
 
            try:
                direction = Vector2(x, y).normalize()
                void.move_direction(direction)
            except ValueError:
                # Ignore ValueError, vector is zero / if everything is on line
                pass
            self.movement_collision(void)
 
    def movement_collision(self, object: GameObject) -> bool:
        """
        Prevent object from moving towards blocked direction.
 
        Sub-stepping is not implemented.
        """
 
        # Test for different movement directions stoppages.
        move_x, move_y = object._move_direction
 
        # Exit early, if no collision
        if not self.future_collision(object):
            return False
        # else: Collisions, try handling it.
 
        # Try resetting individual movement directions.
        if move_x != 0:
            object._move_direction[0] = 0.
            r = self.future_collision(object)
            if not r: return r
            else: object._move_direction[0] = move_x
 
        if move_y != 0:
            object._move_direction[1] = 0.
            r = self.future_collision(object)
            if not r: return r
            else: object._move_direction[1] = move_y
 
        # Try resetting both movement directions
        object._move_direction[0] = 0.
        object._move_direction[1] = 0.
 
        return self.future_collision(object)
 
    def future_collision(self, object: GameObject):
        """
        Check if object will collide with something in the future.
 
        Uses game clock to check how far the object will move.
 
        TODO add level bounds
        """
 
        # Get future position of object
        frame_ms = self.clock.get_time()
        target_x, target_y = object.get_location(frame_ms)
        rect = pygame.Rect(target_x, target_y, object.width, object.height)
        return self.rect_collision(rect)
 
    def rect_collision(self, rect: pygame.Rect):
        """
        Check if :param:`rect` collides with any blocking tiles.
 
        :param rect: pygame rectangular. Can be only two tiles wide
                     and tall at maximum so I don't need to calculate
                     the full rectangle in pixels.
        """
 
        left = int(rect.left // self.TILE_SIZE)
        top = int(rect.top // self.TILE_SIZE)
        right = int(rect.right // self.TILE_SIZE)
        bottom = int(rect.bottom // self.TILE_SIZE)
 
        tiles = {self.maze[top][left], self.maze[top][right], self.maze[bottom][left], self.maze[bottom][right]}
        return bool(tiles & TileTypes.BLOCKING)
 
    def get_random_tile(self):
        """
        Get a random, accessible position on the maze.
 
        Notice: accessability not guaranteed.
        """
        player_location = self.player_object.get_location() // self.TILE_SIZE
 
        while True:
            # Dont place next to borders, and next to player
            exit_location = Vector2(random.randint(2, self.MAZE_SIZE[0] - 4),
                                    random.randint(2, self.MAZE_SIZE[1] - 4))
 
            # Make sure it's not next to player
            if exit_location.distance_to(player_location) <= 2:
                continue
 
            x, y = map(int, exit_location)
            # Dont place on blocking tiles
            # Check that there is entryway to the exit
            surrounding_tiles = {self.maze[y][x], self.maze[y - 1][x], self.maze[y + 1][x], self.maze[y][x - 1], self.maze[y][x + 1]}
            if not surrounding_tiles & TileTypes.BLOCKING:
                return (x, y)
 
    def set_state(self, state: GameState):
        """
        Set game state.
        """
        self.state = state
        self.level_timer = 0
        #self.reset_level()
 
    def init_level(self, level: int):
        """
        Setup new maze based on :param:`level`.
 
        :param level: level number
        """
        self.maze = maze(*self.MAZE_SIZE)
 
        self.init_player()
        self.init_exit()
 
        # no voids on first level
        if self.level > 1:
            self.init_voids()
 
        self.init_hud()
 
        self.render_maze()
 
        print("Maze:")
        for r in self.maze:
            print("".join(r))
 
    def reset_level(self):
        """
        Reset level to empty state.
        """
        self.level_timer = 0
 
        self.maze_layer.empty()
        self.player_layer.empty()
        self.void_layer.empty()
        self.exit_layer.empty()
        self.hud_layer.empty()
 
    def level_completed(self):
        """
        Mark current level as completed and move into next level or game state.
        """
        print("Level completed", self.level)
        self.level += 1
 
        # Collect all the doors!
        if self.level <= len(self.DOORS):
            self.reset_level()
            self.init_level(self.level)
 
        else:
            self.set_state(GameState.COMPLETED)
 
    def init_player(self, location=None):
        """
        Setup player character in to the maze.
 
        No guarantees of player not being placed in unaccessible position.
        """
 
        self.player_object = PlayerObject(size=self.TILE_SIZE)
        self.player_layer.add(self.player_object)
 
        if location is None:
            location = self.player_default_location() // self.TILE_SIZE
 
        x, y = map(int, location)
        self.maze[y][x] = FloorTile.SYMBOL
        self.player_object.x = x * self.TILE_SIZE
        self.player_object.y = y * self.TILE_SIZE
 
    def init_voids(self):
        """
        Place voids in the maze.
 
        Number of voids is based on level.
        """
 
        for i in range(self.level):
            # Place enemy
            x, y = self.get_random_tile()
            self.maze[y][x] = VoidObject.SYMBOL
 
            void_object = VoidObject()
            void_object.x = x * self.TILE_SIZE
            void_object.y = y * self.TILE_SIZE
 
            self.void_layer.add(void_object)
 
    def init_exit(self):
        """
        Place exit in the maze.
        """
        x, y = self.get_random_tile()
        self.maze[y][x] = DoorTile.SYMBOL
 
    def init_hud(self):
        # Add collected door symbols to HUD
        for i in range(self.level - 1):
            # Could be cleaner...
            door_symbol_size = self.TILE_SIZE * 1.2
            door_symbol_position = (self.window.get_width() - (i + 1) * door_symbol_size, self.window.get_height() - door_symbol_size)
            door_symbol = DoorTile(door_symbol_position, door_symbol_size, self.DOORS[i])
            door_symbol.intensity = 1
            self.hud_layer.add(door_symbol)
 
        self.hud_layer.add(LevelText(self.level))
 
    def init_outro(self):
        """
        Setup outro screen.
 
        Outro is special maze with pseudo 1d gameplay to indicate game coming to completion.
        """
        width, height = self.MAZE_SIZE
        player_level = int((height / 5) * 3)
 
        row = [InvisibleWall.SYMBOL] + [FloorTile.SYMBOL] * (width - 2) + [InvisibleWall.SYMBOL]
        maze = [row.copy() for _ in range(height)]
        maze[player_level - 1] = [InvisibleWall.SYMBOL] * width
        # Fill out the bottom
        maze[player_level + 1:] = [[WallTile.SYMBOL] * width] * (height - player_level - 2)
 
        self.maze = maze
 
        player_position = Vector2(10, player_level)
        self.init_player(player_position)
        # Fix player position to bottom of the tile.
        self.player_object.y += (self.TILE_SIZE - self.player_object.height - 1)
 
        door_symbol_size = self.TILE_SIZE * 1.2
        # Place all door opposite side of player
        for i, door_color in enumerate(self.DOORS):
            x = (self.MAZE_SIZE[0] - 10) * self.TILE_SIZE + i * door_symbol_size
            y = player_level * self.TILE_SIZE - (door_symbol_size - self.TILE_SIZE)
 
            door_symbol = DoorTile((x, y), door_symbol_size, door_color)
            door_symbol.intensity = 1
 
            self.exit_layer.add(door_symbol)
 
        self.render_maze()
 
    def raytrace(self):
        """
        Raytraces the player's field of view.
 
        Returns a matrix tiles that are in the field of view.
 
        Negative numbers indicate tiles that are not in the field of view, and positive
        numbers are distance normalized to the maze cross distance.
        """
 
        max_ray_length = math.sqrt(self.MAZE_SIZE[0]**2 + self.MAZE_SIZE[1]**2) * self.TILE_SIZE
 
        def norm_distance(d: float) -> float:
            """Helper function to normalize values"""
            if 0 < d < float("inf"):
                # Rational
                return min(1, d / max_ray_length)
            else:
                return -1.
 
        # Direction where to send rays.
        half_fov = self.player_object.FOV / 2
        angle = self.player_object.view_angle - half_fov
        x, y = self.player_object.rect.center
 
        # vector to store the distance to the closest opaque tile.
        # Not using matrix here because it's easier to combine list
        # without numpy.
        distances = [float("inf")] * self.MAZE_SIZE[0] * self.MAZE_SIZE[1]
 
        for ray in range(self.RAYS):
            distances = map(min, zip(distances, raycast_dda(x, y, angle, self.maze)))
            angle += self.player_object.FOV / self.RAYS
 
        # Normalize values
        normalized = map(norm_distance, distances)
        # Convert list to a matrix
        viewable = list(zip(*[iter(normalized)] * self.MAZE_SIZE[0]))
 
        return viewable
 
    def shading(self):
        """
        Create a radial shading map from player position.
        Similar effect to ray tracing, but without the tracing and fov.
 
        TODO - make this more efficient.
        """
 
        max_ray_length = math.sqrt(self.MAZE_SIZE[0]**2 + self.MAZE_SIZE[1]**2)
 
        # Get player position
        player = Vector2(self.player_object.rect.center) // self.TILE_SIZE
 
        # Create a radial shading map
        shading = [[0] * self.MAZE_SIZE[0] for _ in range(self.MAZE_SIZE[1])]
        for i in range(self.MAZE_SIZE[0]):
            for j in range(self.MAZE_SIZE[1]):
                distance = (Vector2(i, j) - player).length()
                shading[j][i] = distance / max_ray_length
        shading[int(player.y)][int(player.x)] = 0.01
        return shading
 
    def draw(self, frame: pygame.Surface):
        """
        Draw layers to surface.
        """
        self.maze_layer.draw(frame)
        self.exit_layer.draw(frame)
        self.player_layer.draw(frame)
        self.void_layer.draw(frame)
        self.hud_layer.draw(frame)
 
    def run(self):
        """
        Main game loop.
 
        Loops until game is over.
 
        Behaviour is selected from the game state.
        """
 
        self.state = GameState.COMPLETED
 
        # Init pygame and stuff.
        pygame.init()
        self.font = pygame.font.SysFont("monospace", 14)
 
        fill_color = (255, 255, 255)
 
        # Render target - window is not directly drawn to.
        # Plan was to add some camera effects, but it was not implemented.
        frame: pygame.Surface = pygame.Surface(self.window.get_size())
 
        while self.state != GameState.QUIT:
 
            updated = self.clock.get_time()
 
            # Reset frames
            frame.fill(fill_color)
            if self.debug: self.debug_surface.fill((0, 0, 0))
 
            keys = pygame.key.get_pressed()
            # Check common events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = GameState.QUIT
                    break
                if event.type == pygame.KEYUP and event.key == pygame.K_F11:
                    self.debug = not self.debug
                    print("Toggling debug", self.debug)
                if event.type == pygame.KEYUP and event.key == pygame.K_PERIOD:
                    if self.debug and self.state == GameState.PLAYING:
                        self.level_completed()
                    break
 
            if self.state == GameState.INTRO:
                fill_color = (0, 0, 0)
                # Force to watch some intro
                # but skip to game after a while.
                if (any(keys) and self.level_timer > 200) or self.level_timer / 1000 > 7:
                    self.set_state(GameState.INIT)
                    continue
 
                self.intro.update(updated)
                self.intro.draw(frame)
 
            elif self.state == GameState.INIT:
                # Setup game defaults.
                self.level = 1
                self.reset_level()
                self.init_level(self.level)
                self.set_state(GameState.PLAYING)
                continue
 
            elif self.state == GameState.PLAYING:
                # Main loop
                # =========
 
                # Move player and voids according to player input.
                self.move_player()
                self.move_voids()
 
                # Update sprite layers
                self.player_layer.update(updated)
                self.exit_layer.update(updated)
 
                # Check for game collision events
                if pygame.sprite.groupcollide(self.void_layer, self.player_layer, False, False):
                    # todo: resetting here might not be needed.
                    self.reset_level()
                    self.level = 1
                    self.hud_layer.add(TextSprite("Darkness was a jerk..."))
                    self.set_state(GameState.DEFEAT)
 
                elif pygame.sprite.groupcollide(self.exit_layer, self.player_layer, False, False):
                    self.level_completed()
                    continue
 
                # Raytrace tiles in field of view
                tile_mask = self.raytrace()
 
                # If starting a level, fade the viewable area.
                if self.level_timer < 1000:
                    fade = 1 - self.level_timer / 1000
                    tile_mask = fadein_mask(tile_mask, fade)
 
                # Update sprites with the view mask
                self.maze_layer.update(updated, tile_mask)
                self.void_layer.update(updated, tile_mask)
                self.hud_layer.update(updated, tile_mask)
 
                self.draw(frame)
 
            elif self.state == GameState.COMPLETED:
                # Setup special 1d level.
                self.set_state(GameState.OUTRO)
                self.reset_level()
                self.init_outro()
 
            elif self.state == GameState.OUTRO:
                # Special 1d level.
                self.move_player()
                self.player_layer.update(updated)
                self.exit_layer.update(updated)
 
                if pygame.sprite.groupcollide(self.exit_layer, self.player_layer, False, False):
                    fill_color = (255, 255, 255)
                    self.set_state(GameState.CREDITS)
 
                    # HACK
                    # Copy sprite properties for player sprite,
                    # and add it to the lineup.
                    _sprite = self.exit_layer.sprites()[0]
                    pos = (_sprite.rect.x - _sprite.rect.width - 3, _sprite.rect.y - 1)
                    player_sprite = DoorTile(pos, _sprite.size[0] + 2, self.player_object.color)
                    player_sprite.intensity = 1
                    player_sprite.update(0)
                    self.exit_layer.add(player_sprite)
                    continue
 
                # Use radial shading instead of ray-tracing.
                mask = self.shading()
                self.maze_layer.update(updated, mask)
                self.draw(frame)
 
                # Moving towards other fades screen white to symbolize the end
                # of the game.
                # Expects exits to be located 10 tiles from right
                max_distance = (self.MAZE_SIZE[0] - 20) * self.TILE_SIZE
                # Not completely opaque to reduce confusion.
                brightness = 240 * (self.player_object.x / max_distance - 0.5)
                overlay = pygame.Surface(self.window.get_size())
                overlay.fill((255, 255, 255))
                overlay.set_alpha(brightness)
                frame.blit(overlay, (0, 0))
                self.exit_layer.draw(frame)
 
            elif self.state == GameState.CREDITS:
                if self.level_timer > 700 and any(keys):
                    # Allow skipping after small delay to allow key press release.
                    self.set_state(GameState.INTRO)
 
                # Scroll credits, which is the docstring from this file.
                credits = sys.modules[__name__].__doc__.split("\n")
                font_height = self.font.get_height()
 
                # Opposite color of the background fill.
                text_color = (255, 255, 255) if sum(fill_color) / 3 <= 127 else (0, 0, 0)
 
                # Draw credits into surface, and move surface upwards until out of view.
                credits_surface = pygame.Surface((self.window.get_width(), self.font.get_height() * len(credits)))
                credits_surface.fill(fill_color)
                width = 0
                for i, line in enumerate(credits):
                    text = self.font.render(line, True, text_color)
                    credits_surface.blit(text, (0, i * font_height))
                    width = max(width, text.get_width())
 
                y = self.window.get_height() - (self.level_timer / 50) - 20
                frame.blit(credits_surface, ((self.window.get_width() - width) / 2, y))
 
                if y + credits_surface.get_height() < 0:
                    self.state = GameState.INTRO
                    self.level_timer = 0
                    continue
 
                # Draw exit icons
                self.exit_layer.update(updated)
                self.exit_layer.draw(frame)
 
            # Draw rendered frame into window
            self.window.blit(frame, (0, 0))
 
            # Draw debug info
            if self.debug:
                self.draw_debug()
                self.window.blit(self.debug_surface, (0, 0))
 
            # flop
            pygame.display.flip()
 
            self.level_timer += updated
            self.clock.tick(60)
 
        pygame.quit()
 
    def draw_debug(self):
        """
        Draw some debug info onto the debug surface.
        """
        for door in self.exit_layer.sprites():
            pygame.draw.rect(self.debug_surface, door.color, door.rect)
        
        voids_active = sum(1 for v in self.void_layer.sprites() if v.active)
        voids_num = len(self.void_layer.sprites())
        self.debug_surface.blit(self.font.render("FPS: %d" % self.clock.get_fps(), True, (255, 255, 255)), (0, 0))
        self.debug_surface.blit(self.font.render(f"Voids: {voids_active} / {voids_num}", True, (255, 255, 255)), (0, self.font.get_height()))
 
 
def fadein_mask(mask: list, fade: float) -> list:
    """
    Create a fading mask from time :param:`fade`.
 
    Keeps the minimum value of the mask if value > 0
    """
    return [[min(1, col + fade) if col > 0 else -1 for col in row] for row in mask]
 
 
def raycast_naive(x, y, angle, maze: List[List], tile_size=Game.TILE_SIZE) -> List[float]:
    """
    Cast ray from a point in the maze.
    Finds the shortest distance to the opaque tile.
 
    Uses a naive raycasting algorithm.
    """
 
    def distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
 
    tile_size = Game.TILE_SIZE
    maze_width = len(maze[0])
    maze_height = len(maze)
    max_depth = int(math.sqrt(maze_height ** 2 + maze_width ** 2) * tile_size)
 
    max_x = maze_width * tile_size
    max_y = maze_height * tile_size
 
    cos = math.cos(angle)
    sin = math.sin(angle)
 
    distances = [float("inf")] * maze_width * maze_height
 
    # Using bigger steps could speed up the raytracing,
    # but it makes it a less accurate.
    for depth in range(0, max_depth, int(tile_size // 3)):
        target_x = x + cos * depth
        target_y = y + sin * depth
 
        # Check for bounds
        if not (0 < target_x < max_x) or not (0 < target_y < max_y):
            #raise OverflowError("Raycast went out of bounds")
            break
 
        col = int(target_x // tile_size)
        row = int(target_y // tile_size)
        idx = row * maze_width + col
 
        if maze[row][col] in TileTypes.OPAQUE:
            # Blocking object, stop raytrace
            distances[idx] = min(distances[idx], distance(x, y, target_x, target_y))
            break
        elif maze[row][col] in TileTypes.TRANSPARENT:
            # Transparent (open) title
            distances[idx] = min(distances[idx], distance(x, y, target_x, target_y))
 
    return distances
 
 
def raycast_dda(start_x, start_y, angle, maze: List[List], tile_size=Game.TILE_SIZE) -> List[float]:
    """
    Cast rays from a point in the maze.
    Finds the shortest distance to the opaque tile.
 
    Uses a Digital Differential Analysis (DDA) algorithm.
    https://lodev.org/cgtutor/raycasting.html
    """
 
    maze_height = len(maze)
    maze_width = len(maze[0])
    max_depth = int(math.sqrt(maze_height ** 2 + maze_width ** 2) * tile_size)
 
    dx = math.cos(angle)
    dy = math.sin(angle)
 
    step_size_x = math.sqrt(1 - dx ** 2) * tile_size
    step_size_y = math.sqrt(1 - dy ** 2) * tile_size
 
    distances = [float("inf")] * maze_width * maze_height
 
    ray_length_x, ray_length_y = (0, 0)
 
    # Offset from tile top-left corner
    col = int(start_x // tile_size)
    row = int(start_y // tile_size)
 
    # Setup ray starting length relative to tile
    if dx < 0:
        ray_length_x = (start_x - (col * tile_size))
    else:
        ray_length_x = ((col + 1) * tile_size - start_x)
 
    if dy < 0:
        ray_length_y = (start_y - (row * tile_size))
    else:
        ray_length_y = ((row + 1) * tile_size - start_y)
 
    distance = 0
    while distance < max_depth:
 
        # Follow the shorter ray
        if (ray_length_x < ray_length_y and step_size_x) or step_size_y == 0:
            distance = ray_length_x
            ray_length_x += step_size_x
        else:
            distance = ray_length_y
            ray_length_y += step_size_y
 
        # tile intersection position
        _xy = [
            start_x + distance * dx,
            start_y + distance * dy,
        ]
 
        col = int(_xy[0] // tile_size)
        row = int(_xy[1] // tile_size)
 
        if not (0 < col < maze_width) or not (0 < row < maze_height):
            #raise OverflowError("Raycast went out of bounds")
            break
 
        # Store current distance.
        idx = row * maze_width + col
        distances[idx] = min(distances[idx], distance)
 
        if maze[row][col] in TileTypes.OPAQUE:
            # Blocking object, stop raytrace
            break
 
    return distances
 
 
def maze(width, height, density=0.2):
    """
    Generate random "maze". Might not be solvable.
    """
    maze = []
    for y in range(height):
        row = []
        if y == 0 or y == height - 1:
            # First and last rows are full walls
            row = [WallTile.SYMBOL] * width
        else:
            for x in range(width):
                if x == 0 or x == width - 1:
                    # First and last columns are full walls
                    row.append(WallTile.SYMBOL)
                else:
                    row.append(WallTile.SYMBOL if random.random() <= density else FloorTile.SYMBOL)
        maze.append(row)
 
    return maze
 
 
if __name__ == "__main__":
    game = Game()
    game.run()