import pygame

MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0 # 0 = North, 1 = East, 2 = South, 3 = West
        self.map_x = 1
        self.map_y = 1
        self.position = MAP[self.map_x][self.map_y]

class Spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error:
            print('Unable to load spritesheet image')
            raise SystemExit
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface((rect.size), pygame.SRCALPHA)
        # image.fill( (0,0,0,0) )
        image.blit(self.sheet, (0, 0), rect)
        return image

class GameState:

    def __init__(self):
        self.running = True
        self.run_mode = "start"
        self.player = Player(6, 6)

pygame.init()
pygame.display.set_caption("Dungeon Crawl")
screen = pygame.display.set_mode((480, 270))

clock = pygame.time.Clock()    

gs = GameState()
wall_sprites = Spritesheet("assets/monochrome_wall.png")
wall_side_close = wall_sprites.image_at((320, 120, 160, 120))
wall_side_far = wall_sprites.image_at((0, 120, 160, 120))
wall_facing_close = wall_sprites.image_at((160, 120, 160, 120))
wall_facing_far = wall_sprites.image_at((320, 0, 160, 120))

floor_sprites = Spritesheet("assets/monochrome_ceiling.png")
floor_ceiling_close = floor_sprites.image_at((480, 120, 140, 120))
floor_ceiling_far = floor_sprites.image_at((160, 120, 140, 120))

def draw_map():
    x = 0
    y = 0
    for row in MAP:
        for column in row:
            if column == 1:
                pygame.draw.rect(screen, "red", (x, y, 5, 5))
                x += 6
                # print(f"Red tile drawn at ({x}, {y})")
            if column == 0:
                pygame.draw.rect(screen, "blue", (x, y, 5, 5))
                x += 6
                # print(f"Blue tile drawn at ({x}, {y})")
        x = 0
        y += 6

def draw_player_map():
    pygame.draw.rect(screen, "green", (gs.player.x, gs.player.y, 5, 5))
    pygame.draw.line(screen, "green", (gs.player.x + 2.5, gs.player.y), (gs.player.x + 2.5, gs.player.y - 3))

def draw_player_pov():
    left_sector = (160, 100)
    right_sector = (320, 100)
    top_sector = ()
    bottom_sector = ()
    
    



    # Facing North
    # 
    # [x - 1][y - 2] - [x][y - 2] - [x + 1][y + 2]
    #                     |
    # [x -1][y - 1] - [x][y - 1] - [x + 1][y + 1]
    #                    |
    # [x - 1][y]   -  [x][y] - [x + 1][y]
    #
    #
    x = gs.player.map_x - 1
    y = gs.player.map_y - 1
    if gs.player.direction == 0:
        for x in range(gs.player.map_x + 1):
            for y in range(gs.player.map_y + 1):
                if MAP[x][y] == 1:
                    screen.blit(floor_ceiling_far, (160, 100))
                    screen.blit(floor_ceiling_close, (160, 100))
                    screen.blit(wall_facing_far, (160, 100))
                    screen.blit(wall_side_far,(160, 100))
                    screen.blit(wall_side_close, (160, 100))        


    # Facing East
    if gs.player.direction == 1:
        pass
    
    # Facing South
    if gs.player.direction == 2:
        pass
    
    # Facing West
    if gs.player.direction == 3:
        pass

def input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gs.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                gs.player.y -= 6
                gs.player.position -= 1
            if event.key == pygame.K_a:
                gs.player.x -= 6
            if event.key == pygame.K_s:
                gs.player.y += 6
            if event.key == pygame.K_d:
                gs.player.x += 6
                gs.player.map_y += 1
            if event.key == pygame.K_e:
                if gs.player.direction == 3:
                    gs.player.direction = 0
                else:
                    gs.player.direction += 1
            if event.key == pygame.K_q:
                if gs.player.direction == 0:
                    gs.player.direction = 3
                else:
                    gs.player.direction -= 1
    
def update():
    pass

def render():
    screen.fill("black")
    draw_map()
    draw_player_map()
    draw_player_pov()
    pygame.display.flip()

def main():
    
    while gs.running:
        input()
        update()
        render()
    
    pygame.quit()

main()