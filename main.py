import pygame
import random
from config import *
from ui import draw_card
from generator import generate_trial
from scoring import apply_answer

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    running = True
    trial = generate_trial(random.Random())
    score = 0
    correct_answers = 0
    wrong_answers = 0

    while running:
        for event in pygame.event.get():
            # Se premo la X della finestra si chiude
            if event.type == pygame.QUIT:
                running = False
            
            # Input da tastiera
            if event.type == pygame.KEYDOWN:
                # Se premo ESC si chiude
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Se premo FRECCIA DESTRA
                elif event.key == pygame.K_RIGHT:
                    user_answer = True
                    is_correct = (user_answer == trial.expected_answer)
                    score = apply_answer(score, is_correct)
                    if is_correct:
                        correct_answers += 1
                    else:
                        wrong_answers += 1
                    trial = generate_trial(random.Random())
                # Se premo FRECCIA SINISTRA
                elif event.key == pygame.K_LEFT:
                    user_answer = False
                    is_correct = (user_answer == trial.expected_answer)
                    score = apply_answer(score, is_correct)
                    if is_correct:
                        correct_answers += 1
                    else:
                        wrong_answers += 1
                    trial = generate_trial(random.Random())

        screen.fill((0, 0, 0)) # Colore nero
        draw_card(screen, trial)
        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()

if __name__ == "__main__":
    main()
