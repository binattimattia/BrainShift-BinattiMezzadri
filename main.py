import pygame
import random
from config import *
from ui import draw_card
from generator import generate_trial

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    running = True
    current_trial = generate_trial(random.Random())

    while running:
        for event in pygame.event.get():
            # Se premo la X della finestra si chiude
            if event.type == pygame.QUIT:
                running = False
            # Se intercetta un evento sulla tastiera ed è ESC
            # Chiude la finestra
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0)) # Colore nero
        draw_card(screen, current_trial)
        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()

if __name__ == "__main__":
    main()
