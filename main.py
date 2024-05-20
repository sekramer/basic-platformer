import pygame

pygame.init

width, heigt = 800, 600
FPS = 60

pygame.display.set_caption("The Amazing Incredible Fausible Legend of the Ninjiest Ninja Frog")
window = pygame.display.set_mode((width, height))

def main(window):
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for events in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)