from os.path import join
import pygame

pygame.init

width, height = 800, 600
FPS = 60

pygame.display.set_caption("The Amazing Incredible Fausible Legend of the Ninjiest Ninja Frog")
window = pygame.display.set_mode((width, height))

def get_backround(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width_of_tile, height_of_tile = image.get_rect()

    tiles = []

    for i in range(width // width_of_tile + 1):
        for j in range(height // height_of_tile + 1):
            top_left_corner = (i * width_of_tile, j * height_of_tile)
            tiles.append(top_left_corner)

    return tiles, image

def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_backround("Blue.png")
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        draw(window, background, bg_image)
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)