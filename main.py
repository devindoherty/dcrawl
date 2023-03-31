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



state = {
    "runmode": "Start",
    "redraw": True,
    "command": "letter"
}
screen = pygame.display.set_mode((480, 270))
clock = pygame.time.Clock()
running = True

wall_types = pygame.image.load("assets/monochrome_wall.png").convert_alpha()

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

    pygame.display.flip()

def main():

    pygame.init()
    print("Pygame Init")
    

    while running:
        input(state, screen)
        update(state, screen)
        render(screen)

main()
>>>>>>> a0bff23ef3ccd5a0abaf6fea1e72524ac05ba157
