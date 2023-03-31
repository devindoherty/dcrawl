import pygame

MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

class Player:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0

def draw_map(window):
    x = 0
    y = 0
    for row in MAP:
        for column in row:
            if column == 1:
                pygame.draw.rect(window, "red", (x, y, 5, 5))
                x += 6
                # print(f"Red tile drawn at ({x}, {y})")
            if column == 0:
                pygame.draw.rect(window, "blue", (x, y, 5, 5))
                x += 6
                # print(f"Blue tile drawn at ({x}, {y})")
        x = 0
        y += 6

def draw_player(window, player):
    pygame.draw.rect(window, "green", (player.x, player.y, 5, 5))
    pygame.draw.line(window, "green", (player.x, player.y), (player.x, player.y - 3))

def main():
    pygame.init()

    window = pygame.display.set_mode((480, 270))
    player = Player(6, 6)
    draw_map(window)
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.y -= 6
                if event.key == pygame.K_a:
                    player.x -= 6
                if event.key == pygame.K_s:
                    player.y += 6
                if event.key == pygame.K_d:
                    player.x += 6
                draw_map(window)

        draw_player(window, player)
        pygame.display.flip()

    pygame.quit()

main()