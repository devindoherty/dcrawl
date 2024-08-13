import pygame
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1,'D',1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


INTRO = [
"Brave adventurer, you have foolishly chosen to enter the fiendish",
"DUNGEON GATE, a portal to a subterranean realm most foul. Should",
"you wish to emerge alive, you must SLAY all the monsters that prowl",
"these fetid depths.",
"",
"WASD to move forward, backward, and side to side. E and Q rotate your",
"view. Mouse click to attack.",
"",
"Press SPACEBAR to continue..."
]

DEFEAT = ["You have died."]

VICTORY = ["You SLEW all your foes and escaped! Huzzah!"]

#Compass
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

#Sprite Blitting
LEFT_SIDE = (0, 0, 80, 120)
RIGHT_SIDE =  (80, 0, 160, 120)
LEFT_ALIGNMENT = (0, 0)
RIGHT_ALIGNMENT = (80, 0)
CENTER_ALIGNMENT = (0, 0)
MONSTER_FAR_CENTER_ALIGNMENT = (37.5, 25)
MONSTER_FAR_LEFT_ALIGNMENT = (15, 25)
MONSTER_FAR_RIGHT_ALIGNMENT = (60, 25)
MONSTER_MEDIUM_RIGHT_ALIGNMENT = (50, 0)
MONSTER_MEDIUM_LEFT_ALIGNMENT = (-55, 0)

class GameState:
    def __init__(self, screen, pov_screen, map_screen, log_screen, info_screen, sprites):
        self.screen = screen
        self.pov_screen = pov_screen
        self.map_screen = map_screen
        self.log_screen = log_screen
        self.info_screen = info_screen
        self.sprites = sprites
        self.start_dialog = Dialog(INTRO)
        self.win_dialog = Dialog(VICTORY)
        self.lose_dialog = Dialog(DEFEAT)
        self.running = True
        # self.run_modes = ["start", "player_turn", "monster_turn", "dialog", "menu", "win", "lose"]
        self.run_mode = "start"
        self.player = Player(36, 7)
        self.monsters = []
        self.redraw = True
        self.debug = False
        self.map = Map(MAP)
        self.clock = pygame.time.Clock()
        self.log = [pygame.font.SysFont(None, 35).render("", True, "white"),
                    pygame.font.SysFont(None, 35).render("", True, "white")
                    ]    

class Spritesheet():
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename) #.convert_alpha()
    
    # Load a specific image from a rect
    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface((rect.size), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        return image

class MapTile():
    def __init__(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile
        self.explored = False

class Map():
    def __init__(self, raw_map):
        self.map = [[0 for _ in range(len(MAP[0]))] for _ in range(len(MAP))]
        for x, row in enumerate(raw_map):
            for y, tile in enumerate(row):
                self.map[x][y] = MapTile(x, y, tile)

    def reveal_map(self, playerx, playery):
        for x in range(playerx - 1, playerx + 2):
            for y in range(playery - 1, playery + 2):
                self.map[x][y].explored = True
        
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0 # 0 = North, 1 = East, 2 = South, 3 = West
        self.position = [x, y]
        self.health = 30
        self.defense = 12
        self.inventory = []
        self.attacking = False
        self.moved = False
        self.attacking_idx = 0

    def player_move(self, key, monsters):
        self.moved = True
        x = self.x
        y = self.y

        # Directionals
        if key == pygame.K_w:
            if self.direction == NORTH:
                x = x - 1
            if self.direction == EAST:
                y = y + 1
            if self.direction == SOUTH:
                x = x + 1
            if self.direction == WEST:
                y = y - 1
        if key == pygame.K_a:
            if self.direction == NORTH:
                y = y - 1
            if self.direction == EAST:
                x = x - 1
            if self.direction == SOUTH:
                y = y + 1
            if self.direction == WEST:
                x = x + 1
        if key == pygame.K_s:
            if self.direction == NORTH:
                x = x + 1
            if self.direction == EAST:
                y = y - 1
            if self.direction == SOUTH:
                x = x - 1
            if self.direction == WEST:
                y = y + 1
        if key == pygame.K_d:
            if self.direction == NORTH:
                y = y + 1
            if self.direction == EAST:
                x = x + 1
            if self.direction == SOUTH:
                y = y - 1
            if self.direction == WEST:
                x = x - 1
        if position_is_empty(x, y, monsters):
            self.x = x
            self.y = y

            self.position[0] = self.x
            self.position[1] = self.y


        # Rotationals
        if key == pygame.K_e:
            if self.direction == WEST:
                self.direction = NORTH
            else:
                self.direction += 1
        if key == pygame.K_q:
            if self.direction == NORTH:
                self.direction = WEST
            else:
                self.direction -= 1

    def player_attack(self, monsters):
        pass

    def inflict_damage(self, damage):
        self.health -= damage

class Monster:
    def __init__(self, name, x, y, sprite):
        self.name = name
        self.x = x
        self.y = y
        self.position = [self.x, self.y]
        self.sprite = sprite
        self.health = 20
        self.defense = 8
        self.dead = False

    def inflict_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead = True

class Dialog:
    def __init__(self, message):
        self.message = message

    def display(self, gs):
        gs.screen.blit(pygame.transform.scale_by(gs.sprites["gateway"], .75), (SCREEN_HEIGHT / 3.9, 150))
        y = 0
        i = 0
        for msg in self.message:
            msg = pygame.font.SysFont(None, 35).render(self.message[i], True, "white")
            gs.screen.blit(msg, (0, y))
            y += 20
            i += 1

def load_sprites(gs):
    # Wall Sprites
    wall_sprites = Spritesheet("assets/monochrome_wall.png")
    gs.sprites["wall_side_close"] = wall_sprites.image_at((320, 120, 160, 120))
    gs.sprites["wall_side_medium"] = wall_sprites.image_at((0, 120, 160, 120))
    gs.sprites["wall_side_far"] = wall_sprites.image_at((160, 0, 160, 120))
    gs.sprites["wall_wideside_far"] = wall_sprites.image_at((0, 0, 160, 120))
    gs.sprites["wall_wideside_medium"] = wall_sprites.image_at((480, 0, 160, 120))
    gs.sprites["wall_facing_medium"] = wall_sprites.image_at((160, 120, 160, 120))
    gs.sprites["wall_facing_far"] = wall_sprites.image_at((320, 0, 160, 120))

    # Door Sprites (Only door facing medium/far implemented)
    door_sprites = Spritesheet("assets/monochrome_locked.png")
    gs.sprites["door_side_close"] = door_sprites.image_at((320, 120, 160, 120))
    gs.sprites["door_side_medium"] = door_sprites.image_at((0, 120, 160, 120))
    gs.sprites["door_side_far"] = door_sprites.image_at((160, 0, 160, 120))
    gs.sprites["door_wideside_far"] = door_sprites.image_at((0, 0, 160, 120))
    gs.sprites["door_wideside_medium"] = door_sprites.image_at((480, 0, 160, 120))
    gs.sprites["door_facing_medium"] = door_sprites.image_at((160, 120, 160, 120))
    gs.sprites["door_facing_far"] = door_sprites.image_at((320, 0, 160, 120))
    
    # Floor Sprites
    floor_sprites = Spritesheet("assets/monochrome_ceiling.png")
    gs.sprites["floor_ceiling_close"] = floor_sprites.image_at((480, 120, 140, 120))
    gs.sprites["floor_ceiling_medium"] = floor_sprites.image_at((160, 120, 140, 120))
    gs.sprites["floor_ceiling_far"] = floor_sprites.image_at((320, 0, 160, 120))
    gs.sprites["floor_ceiling_side_close"] = floor_sprites.image_at((320 , 120, 160, 120))
    gs.sprites["floor_ceiling_side_medium"] = floor_sprites.image_at((0, 120, 160, 120))
    gs.sprites["floor_ceiling_side_far"] = floor_sprites.image_at((160, 0, 160, 120))
    gs.sprites["floor_ceiling_wideside_far"] = floor_sprites.image_at((0, 0, 160, 120))
    gs.sprites["floor_ceiling_doublewideside_far"] = floor_sprites.image_at((480, 0, 160, 120))

    # Monster Sprites
    monster_sprites = Spritesheet("assets/monsters.png")
    gs.sprites["goblin"] = monster_sprites.image_at((0, 0, 150, 128))
    gs.sprites["cultist"] = monster_sprites.image_at((150, 0, 150, 128))
    gs.sprites["zombie"] = monster_sprites.image_at((300, 0, 150, 128))
    gs.sprites["imp"] = monster_sprites.image_at((450, 0, 150, 128))
    gs.sprites["skeleton"] = monster_sprites.image_at((600, 0, 150, 128))

    # Sword Sprites
    sword_sprites = Spritesheet("assets/sword_alt.png")
    gs.sprites["sword1"] = pygame.transform.scale_by(sword_sprites.image_at((0, 0, 275, 61)), .60)
    gs.sprites["sword2"] = pygame.transform.scale_by(sword_sprites.image_at((0, 61, 275, 61)), .60)
    gs.sprites["sword3"] = pygame.transform.scale_by(sword_sprites.image_at((0, 122, 275, 70)), .60)
    gs.sprites["sword4"] = pygame.transform.scale_by(sword_sprites.image_at((0, 192, 275, 86)), .60)
    gs.sprites["sword5"] = pygame.transform.scale_by(sword_sprites.image_at((0, 278, 275, 119)), .60)
    
    # Icons
    gs.sprites["gateway"] = pygame.image.load("assets/dungeon_gate.png")
    gs.sprites["health"] = pygame.image.load("assets/heart.png")
    gs.sprites["defense"] = pygame.image.load("assets/shield.png")

def draw_map(gs):
    gs.map_screen.fill("black")
    x = 0
    y = 0
    for row in gs.map.map:
        for column in row:
            if column.explored:
                if column.tile == 1:
                    pygame.draw.rect(gs.map_screen, "grey", (x, y, 10, 10))
                    # print(f"Red tile drawn at ({x}, {y})")
                elif column.tile == 0:
                    pygame.draw.rect(gs.map_screen, "blue", (x, y, 10, 10))
                    # print(f"Blue tile drawn at ({x}, {y})")
                elif column.tile == 'D':
                    pygame.draw.rect(gs.map_screen, "orange", (x, y, 10, 10))
                x += 11
            else:
                x += 11

        x = 0
        y += 11
    # pygame.draw.rect(screen, "green", (gs.player.y * 11, gs.player.x * 11, 10, 10))
    
    if gs.player.direction == NORTH:
        pygame.draw.polygon(gs.map_screen, "green", [[gs.player.y * 11 + 5, gs.player.x * 11], [gs.player.y * 11, gs.player.x * 11 + 10], [gs.player.y * 11 + 10, gs.player.x * 11 +10]], 0)
    elif gs.player.direction == EAST:
        pygame.draw.polygon(gs.map_screen, "green", [[gs.player.y * 11, gs.player.x * 11], [gs.player.y * 11, gs.player.x * 11 + 10], [gs.player.y * 11 + 10, gs.player.x * 11 + 5]], 0)
    elif gs.player.direction == SOUTH:
        pygame.draw.polygon(gs.map_screen, "green", [[gs.player.y * 11, gs.player.x * 11], [gs.player.y * 11 + 5, gs.player.x * 11 + 10], [gs.player.y * 11 + 10, gs.player.x * 11]], 0)
    elif gs.player.direction == WEST:
        pygame.draw.polygon(gs.map_screen, "green", [[gs.player.y * 11, gs.player.x * 11 + 5], [gs.player.y * 11 + 10, gs.player.x * 11 + 10], [gs.player.y * 11 + 10, gs.player.x * 11]], 0)

    for monster in gs.monsters:
        if gs.map.map[monster.x][monster.y].explored:
            pygame.draw.polygon(gs.map_screen, "red", [[monster.y * 11 + 5, monster.x * 11], [monster.y * 11, monster.x * 11 + 10], [monster.y * 11 + 10, monster.x * 11 +10]], 0)

    gs.screen.blit(gs.map_screen, (0,0))



def draw_pov(gs):
    # Every sprite associated with direction.
    #                                                           Facing 
    # [x - 2][y - 1] - [x - 2][y] - [x - 2][y + 1] = far north     N
    #                     |                                        o
    # [x - 1][y - 1] - [x -1][y] - [x - 1][y + 1] = medium north   r
    #                    |                                         t
    #  [x][y-1]    -  [x][y]    - [x][y + 1] = close               h
    #
    #  [x +1][y-1]  [x + 1][y]   [x + 1][y+1] = medium south       S   
    #                                                              o
    # [x + 2][y-1] [x + 2][y]  [x + 2][y+1] = far south            u
    #                                                              t
    #                                                              h
    #
    #           Facing West                          Facing East 
    # [x -1][y - 2]   [x -1][y - 1] [x - 1][y]   [x -1][y + 1]     [x - 1][y + 2]
    #                            
    #   [x][y -2]      [x][y -1]      [x][y]       [x][y + 1]       [x][y + 2]
    #                           
    # [x + 1][y - 2] [x + 1][y - 1]   [x + 1][y]   [x + 1][y + 1]    [x + 1][y + 2]

    map = gs.map.map
    pov_screen = gs.pov_screen
    sprites = gs.sprites
    x = gs.player.x
    y = gs.player.y

    wall_wideside_far = sprites["wall_wideside_far"]
    wall_side_far = sprites["wall_side_far"]
    wall_facing_far = sprites["wall_facing_far"]

    wall_wideside_medium = sprites["wall_wideside_medium"]
    wall_side_medium = sprites["wall_side_medium"]
    
    wall_facing_medium = sprites["wall_facing_medium"]
    wall_side_close = sprites["wall_side_close"]

    door_wideside_far = sprites["door_wideside_far"]
    door_side_far = sprites["door_side_far"]
    door_facing_far = sprites["door_facing_far"]

    door_wideside_medium = sprites["door_wideside_medium"]
    door_side_medium = sprites["door_side_medium"]
    
    door_facing_medium = sprites["door_facing_medium"]
    door_side_close = sprites["door_side_close"]

    # Floors and Ceilings
    pov_screen.blit(sprites["floor_ceiling_wideside_far"], CENTER_ALIGNMENT)
    pov_screen.blit(sprites["floor_ceiling_doublewideside_far"], CENTER_ALIGNMENT)
    pov_screen.blit(sprites["floor_ceiling_side_far"], CENTER_ALIGNMENT)
    pov_screen.blit(sprites["floor_ceiling_far"], CENTER_ALIGNMENT)
    
    pov_screen.blit(sprites["floor_ceiling_side_medium"], CENTER_ALIGNMENT)
    pov_screen.blit(sprites["floor_ceiling_medium"], CENTER_ALIGNMENT)
    
    pov_screen.blit(sprites["floor_ceiling_side_close"], CENTER_ALIGNMENT)
    pov_screen.blit(sprites["floor_ceiling_close"], CENTER_ALIGNMENT)
 
    # Walls
    if gs.player.direction == NORTH:
        if MAP[x - 2][y - 2] == 1:
            pov_screen.blit(wall_wideside_far, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 2][y + 2] == 1:
            pov_screen.blit(wall_wideside_far, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x - 2][y - 1] == 1:
            pov_screen.blit(wall_side_far, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 2][y + 1] == 1:
            pov_screen.blit(wall_side_far, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x - 2][y] == 1:
            pov_screen.blit(wall_facing_far, CENTER_ALIGNMENT)
        
        if MAP[x - 1][y - 2] == 1:
            pov_screen.blit(wall_wideside_medium, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 1][y + 2] == 1:
            pov_screen.blit(wall_wideside_medium, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x - 1][y - 1] == 1:
            pov_screen.blit(wall_side_medium, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 1][y + 1] == 1:
            pov_screen.blit(wall_side_medium, RIGHT_ALIGNMENT, RIGHT_SIDE)       
        if MAP[x - 1][y] == 1:
            pov_screen.blit(wall_facing_medium, CENTER_ALIGNMENT)
        
        if MAP[x][y - 1] == 1:
            pov_screen.blit(wall_side_close, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x][y + 1] == 1:
            pov_screen.blit(wall_side_close, RIGHT_ALIGNMENT, RIGHT_SIDE)

        for i in range(x - 2, x, 1):
            for j in range(y - 1, y + 2):
                for monster in gs.monsters:
                    if monster.x == i and monster.y == j:
                        # if monster.x >= gs.player.x:
                        #     break
                        if abs(i - x) > 1 or abs(j - y) > 1:
                                if monster.y > gs.player.y:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_RIGHT_ALIGNMENT)
                                if monster.y == gs.player.y:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_CENTER_ALIGNMENT)
                                if monster.y < gs.player.y:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_LEFT_ALIGNMENT)
                        else:
                            if monster.y > gs.player.y:
                                pov_screen.blit(monster.sprite, MONSTER_MEDIUM_RIGHT_ALIGNMENT)
                            if monster.y == gs.player.y:
                                pov_screen.blit(monster.sprite, CENTER_ALIGNMENT)
                            if monster.y < gs.player.y:
                                pov_screen.blit(monster.sprite, MONSTER_MEDIUM_LEFT_ALIGNMENT)

    # Facing East
    if gs.player.direction == EAST:
        if MAP[x - 2][y + 2] == 1:
            pov_screen.blit(wall_wideside_far, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 2][y + 2] == 1:
            pov_screen.blit(wall_wideside_far, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x - 1][y + 2] == 1:
            pov_screen.blit(wall_side_far, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 1][y + 2] == 1:
            pov_screen.blit(wall_side_far, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x][y + 2] == 1:
            pov_screen.blit(wall_facing_far, CENTER_ALIGNMENT)

        if MAP[x - 2][y + 1] == 1:
            pov_screen.blit(wall_wideside_medium, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 2][y + 1] == 1:
            pov_screen.blit(wall_wideside_medium, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x - 1][y + 1] == 1:
            pov_screen.blit(wall_side_medium, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 1][y + 1] == 1:
            pov_screen.blit(wall_side_medium, RIGHT_ALIGNMENT, RIGHT_SIDE)       
        if MAP[x][y + 1] == 1:
            pov_screen.blit(wall_facing_medium, CENTER_ALIGNMENT)
        
        if MAP[x - 1][y] == 1:
            pov_screen.blit(wall_side_close, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 1][y] == 1:
            pov_screen.blit(wall_side_close, RIGHT_ALIGNMENT, RIGHT_SIDE)
        
        for i in range(y + 2, y, -1):
            for j in range(x - 1, x + 2):
                for monster in gs.monsters:
                    if monster.y == i and monster.x == j:
                        # if monster.x >= gs.player.x:
                        #     break
                        if abs(i - y) > 1 or abs(j - x) > 1:
                                if monster.x > gs.player.x:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_RIGHT_ALIGNMENT)
                                if monster.x == gs.player.x:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_CENTER_ALIGNMENT)
                                if monster.x < gs.player.x:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_LEFT_ALIGNMENT)
                        else:
                            if monster.x > gs.player.x:
                                pov_screen.blit(monster.sprite, MONSTER_MEDIUM_RIGHT_ALIGNMENT)
                            if monster.x == gs.player.x:
                                pov_screen.blit(monster.sprite, CENTER_ALIGNMENT)
                            if monster.x < gs.player.x:
                                pov_screen.blit(monster.sprite, MONSTER_MEDIUM_LEFT_ALIGNMENT)

        
    # Facing South
    if gs.player.direction == SOUTH:
        if MAP[x + 2][y + 2] == 1:
            pov_screen.blit(wall_wideside_far, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 2][y - 2] == 1:
            pov_screen.blit(wall_wideside_far, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x + 2][y + 1] == 1:
            pov_screen.blit(wall_side_far, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 2][y - 1] == 1:
            pov_screen.blit(wall_side_far, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x + 2][y] == 1:
            pov_screen.blit(wall_facing_far, CENTER_ALIGNMENT)
        if MAP[x + 2][y] == 'D':
            pov_screen.blit(door_facing_far, CENTER_ALIGNMENT)
        
        if MAP[x + 1][y + 2] == 1:
            pov_screen.blit(wall_wideside_medium, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 1][y - 2] == 1:
            pov_screen.blit(wall_wideside_medium, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x + 1][y + 1] == 1:
            pov_screen.blit(wall_side_medium, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x + 1][y - 1] == 1:
            pov_screen.blit(wall_side_medium, RIGHT_ALIGNMENT, RIGHT_SIDE)       
        if MAP[x + 1][y] == 1:
            pov_screen.blit(wall_facing_medium, CENTER_ALIGNMENT)
        if MAP[x + 1][y] == 'D':
            pov_screen.blit(door_facing_medium, CENTER_ALIGNMENT)
        
        if MAP[x][y + 1] == 1:
            pov_screen.blit(wall_side_close, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x][y - 1] == 1:
            pov_screen.blit(wall_side_close, RIGHT_ALIGNMENT, RIGHT_SIDE)

        for i in range(x + 2, x, -1):
            for j in range(y - 1, y + 2):
                for monster in gs.monsters:
                    if monster.x == i and monster.y == j:
                        # if monster.x <= gs.player.x:
                        #     break
                        if abs(i - x) > 1 or abs(j - y) > 1:
                                if monster.y < gs.player.y:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_RIGHT_ALIGNMENT)
                                if monster.y == gs.player.y:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_CENTER_ALIGNMENT)
                                if monster.y > gs.player.y:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_LEFT_ALIGNMENT)
                        else:
                            if monster.y < gs.player.y:
                                pov_screen.blit(monster.sprite, MONSTER_MEDIUM_RIGHT_ALIGNMENT)
                            if monster.y == gs.player.y:
                                pov_screen.blit(monster.sprite, CENTER_ALIGNMENT)
                            if monster.y > gs.player.y:
                                pov_screen.blit(monster.sprite, MONSTER_MEDIUM_LEFT_ALIGNMENT)


    
    # Facing West
    if gs.player.direction == WEST:
        if MAP[x + 2][y - 2] == 1:
            pov_screen.blit(wall_wideside_far, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 2][y - 2] == 1:
            pov_screen.blit(wall_wideside_far, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x + 1][y - 2] == 1:
            pov_screen.blit(wall_side_far, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 1][y - 2] == 1:
            pov_screen.blit(wall_side_far, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x][y - 2] == 1:
            pov_screen.blit(wall_facing_far, CENTER_ALIGNMENT)

        if MAP[x + 2][y - 1] == 1:
            pov_screen.blit(wall_wideside_medium, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 2][y - 1] == 1:
            pov_screen.blit(wall_wideside_medium, RIGHT_ALIGNMENT, RIGHT_SIDE)
        if MAP[x + 1][y - 1] == 1:
            pov_screen.blit(wall_side_medium, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 1][y - 1] == 1:
            pov_screen.blit(wall_side_medium, RIGHT_ALIGNMENT, RIGHT_SIDE)       
        if MAP[x][y - 1] == 1:
            pov_screen.blit(wall_facing_medium, CENTER_ALIGNMENT)
        
        if MAP[x + 1][y] == 1:
            pov_screen.blit(wall_side_close, LEFT_ALIGNMENT, LEFT_SIDE)
        if MAP[x - 1][y] == 1:
            pov_screen.blit(wall_side_close, RIGHT_ALIGNMENT, RIGHT_SIDE)

        for i in range(y - 2, y, 1):
            for j in range(x - 1, x + 2):
                for monster in gs.monsters:
                    if monster.y == i and monster.x == j:
                        # if monster.x >= gs.player.x:
                        #     break
                        if abs(i - y) > 1 or abs(j - x) > 1:
                                if monster.x < gs.player.x:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_RIGHT_ALIGNMENT)
                                if monster.x == gs.player.x:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_CENTER_ALIGNMENT)
                                if monster.x > gs.player.x:
                                    pov_screen.blit(pygame.transform.scale_by(monster.sprite, .5), MONSTER_FAR_LEFT_ALIGNMENT)
                        else:
                            if monster.x < gs.player.x:
                                pov_screen.blit(monster.sprite, MONSTER_MEDIUM_RIGHT_ALIGNMENT)
                            if monster.x == gs.player.x:
                                pov_screen.blit(monster.sprite, CENTER_ALIGNMENT)
                            if monster.x > gs.player.x:
                                pov_screen.blit(monster.sprite, MONSTER_MEDIUM_LEFT_ALIGNMENT)
    
    draw_sword(gs)
    gs.screen.blit(pygame.transform.scale_by(gs.pov_screen, 3.5), (180, 7))


def draw_sword(gs):
    pov_screen = gs.pov_screen
    sprites = gs.sprites

    animations = [
            sprites["sword1"],
            sprites["sword2"],
            sprites["sword3"],
            sprites["sword4"],
            sprites["sword5"],
            sprites["sword5"],
            sprites["sword5"],
            sprites["sword5"],
            sprites["sword4"],
            # sprites["sword3"],
            sprites["sword2"],
            sprites["sword1"],
    ]

    animation_alignments = [
        (0, 84),
        (0, 86),
        (0, 78),
        (0, 70),
        (0, 49),
        (0, 49),
        (0, 49),
        (0, 49),
        (0, 70),
        # (0, 78),
        (0, 86),
        (0, 84),
    ]

    if gs.player.attacking:
        pov_screen.blit(animations[gs.player.attacking_idx], animation_alignments[gs.player.attacking_idx])
        gs.player.attacking_idx += 1
        if gs.player.attacking_idx >= len(animations):
            gs.player.attacking_idx = 0
            gs.player.attacking = False
    else:
        pov_screen.blit(sprites["sword1"], (0, 84))


def draw_log(gs):
    log_screen = gs.log_screen
    log_screen.fill("black")
    log_screen.blit(gs.log[0], (0, 0))
    log_screen.blit(gs.log[1], (0, 25))
    gs.screen.blit(log_screen, (0, 435))

def draw_info(gs):
    info_screen = gs.info_screen
    info_screen.fill("black")
    
    info_screen.blit(gs.sprites["health"], (0,0))
    msg1 = pygame.font.SysFont(None, 100).render(f"{gs.player.health}", True, "red")
    info_screen.blit(msg1, (60, 60))

    info_screen.blit(gs.sprites["defense"], (0,225))
    msg2 = pygame.font.SysFont(None, 100).render(f"{gs.player.defense}", True, "cyan")
    info_screen.blit(msg2, (60, 300))
    gs.screen.blit(info_screen, (750, 0))

def monster_adjacent(x, y, monsters):
    for monster in monsters:
        if (x, y) == (monster.x, monster.y):
            return True

def get_monster_by_position(x, y, monsters):
    for monster in monsters:
        if (x, y) == (monster.x, monster.y):
            return monster

def position_is_empty(x, y, monsters):
    return not monster_adjacent(x, y, monsters) and MAP[x][y] == 0

def spawn_monsters(gs):
    goblin = Monster("Hob", 32, 2, gs.sprites["goblin"])
    zombie = Monster("Mort", 26, 3, gs.sprites["zombie"])
    cultist = Monster("Edgar", 17, 6, gs.sprites["cultist"])
    skeleton = Monster("Bones", 17, 11, gs.sprites["skeleton"])
    imp = Monster("Mephisto", 2, 5, gs.sprites["imp"])
    
    gs.monsters.append(goblin)
    gs.monsters.append(zombie)
    gs.monsters.append(cultist)
    gs.monsters.append(skeleton)
    gs.monsters.append(imp)

def debug(gs):
    print("####### DEBUG #######")
    print(f"Run Mode: {gs.run_mode}")
    print(f"Player Location: {gs.player.position}")
    print(f"Player Health: {gs.player.health}")
    print(f"Player Attacking: {gs.player.attacking}")
    for monster in gs.monsters:
        print(f"{monster.name} Location: {monster.position}")
    print("####### DEBUG #######")


def input(gs):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gs.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gs.running = False
            if event.key == pygame.K_TAB:
                gs.debug = True
            if gs.run_mode == "start":
                if event.key == pygame.K_SPACE:
                    gs.run_mode = "player_turn"
            if gs.run_mode == "player_turn":
                gs.player.player_move(event.key, gs.monsters)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 3:
                gs.player.attacking = True
                if gs.player.direction == NORTH:
                    x = gs.player.x - 1 
                    y = gs.player.y
                elif gs.player.direction == EAST:
                    x = gs.player.x
                    y = gs.player.y + 1
                elif gs.player.direction == SOUTH:
                    x = gs.player.x + 1
                    y = gs.player.y
                elif gs.player.direction == WEST:
                    x = gs.player.x
                    y = gs.player.y - 1
                
                if monster_adjacent(x, y, gs.monsters):
                    monster = get_monster_by_position(x, y, gs.monsters)
                    player_damage = random.randint(1, 12)
                    monster.inflict_damage(player_damage)
                    msg = f"You attacked {monster.name} for {player_damage} damage. {monster.name} now has {monster.health} health. {monster.name + ' is dead.' if monster.health <= 0 else ""}"
                    gs.log[0] = pygame.font.SysFont(None, 30).render(msg, True, "green")
                    monster_attack = random.randint(1, 20)
                    if monster_attack >= gs.player.defense and monster.dead == False:
                        monster_damage = random.randint(1, 10)
                        msg2 = f"{monster.name} attacked you for {monster_damage} damage. (Rolled {monster_attack})"
                        gs.log[1] = pygame.font.SysFont(None, 30).render(msg2, True, "red")
                        gs.player.inflict_damage(monster_damage)
                    else:
                        msg2 = f"{monster.name} attacked you and missed. (Rolled {monster_attack}{' but died)' if monster.dead == True else ')'}"
                        gs.log[1] = pygame.font.SysFont(None, 30).render(msg2, True, "cyan")
                    
def update(gs):
    gs.clock.tick(16)
    
    if gs.debug:
        debug(gs)
        gs.debug = False

    for i, monster in enumerate(gs.monsters):
        if monster.dead == True:
            gs.monsters.pop(i)
    
    if len(gs.monsters) == 0:
        gs.run_mode = "win"

    if gs.player.health <= 0:
        gs.run_mode = "lose"
    if gs.player.moved == True:
        gs.map.reveal_map(gs.player.x, gs.player.y)
        gs.player.moved = False
    
    gs.redraw = True

def render(gs):
    gs.pov_screen.fill("black")
    if gs.redraw == True:
        if gs.run_mode == "start":
            gs.start_dialog.display(gs)
        elif gs.run_mode == "win":
            gs.screen.fill("black")
            gs.win_dialog.display(gs)
        elif gs.run_mode == "lose":
            gs.screen.fill("black")
            gs.lose_dialog.display(gs)
        else:
            gs.screen.fill("black")
            draw_map(gs)
            draw_pov(gs)
            draw_info(gs)
            draw_log(gs)
            gs.redraw = False
        pygame.display.flip()

def main():
    pygame.init()
    pygame.font.init()
    
    icon_image = pygame.image.load("assets/dungeon_gate_icon.png")
    icon = pygame.surface.Surface((32, 32))
    icon.blit(icon_image, (0, 0), (0, 0, 32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Dungeon Gate")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH /2 , SCREEN_HEIGHT /2))
    pov_screen = pygame.surface.Surface((160, 120))
    map_screen = pygame.surface.Surface((165, 430))
    log_screen = pygame.surface.Surface((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 12))
    info_screen = pygame.surface.Surface((200, 430))
    sprites = {}
    gs = GameState(screen, pov_screen, map_screen, log_screen, info_screen, sprites)
    load_sprites(gs)
    spawn_monsters(gs)

    while gs.running:
        input(gs)
        update(gs)
        render(gs)
    
    pygame.quit()

if __name__ == "__main__":
    main()