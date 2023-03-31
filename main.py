import pygame

MAP = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y



state = {
    "runmode": "Start",
    "redraw": True,
    "command": "letter"
}
screen = pygame.display.set_mode((480, 270))
clock = pygame.time.Clock()
running = True

wall_types = pygame.image.load("assets/monochrome_wall.png").convert_alpha()

player = Player(6, 6)

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

def draw_player():
    pygame.draw.rect(screen, "green", (player.x, player.y, 5, 5))
    pygame.draw.line(screen, "green", (player.x, player.y), (player.x, player.y - 3))


def input(state, screen):
    print("Input")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
def update(state, screen):
    print("Update")

def render(screen):
    print("Render")
    screen.fill("purple")
    screen.blit(wall_types,(0, 0))
    draw_map()
    draw_player()

    pygame.display.flip()

def main():

    pygame.init()
    print("Pygame Init")
    

    while running:
        input(state, screen)
        update(state, screen)
        render(screen)

main()
