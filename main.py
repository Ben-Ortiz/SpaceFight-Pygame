import pygame
import math
import random
from pygame import mixer

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

WHITE = (255,255,255)

FPS = 60

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()



def main():
    clock = pygame.time.clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window()



    pygame.quit()

if __name__ == "__main__":
    main()