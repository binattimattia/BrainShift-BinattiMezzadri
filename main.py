import pygame
import random
from config import *
from ui import draw_card, draw_timer, draw_results
from generator import generate_trial
from scoring import apply_answer
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    running = True
    trial = generate_trial(random.Random())
    start_time = time.time()
    score = 0
    correct_answers = 0
    wrong_answers = 0
    state = "PLAYING"
    feedback_until = 0
    need_new_trial = False
    last_answer_correct = None

    while running:
        # Aggiornamento logica di gioco e tempo
        if state == "PLAYING":
            elapsed = time.time() - start_time
            if elapsed >= 60:
                state = "RESULTS"
            
            # Genera la nuova carta solo quando scade il timer del feedback
            if time.time() >= feedback_until and need_new_trial:
                trial = generate_trial(random.Random())
                need_new_trial = False

        # Gestione degli Eventi
        for event in pygame.event.get():
            # Chiusura finestra con la X
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                # Uscita con ESC 
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                if state == "PLAYING" and time.time() >= feedback_until:
                    # Se premo FRECCIA DESTRA
                    if event.key == pygame.K_RIGHT:
                        user_answer = True
                        is_correct = (user_answer == trial.expected_answer)
                        score = apply_answer(score, is_correct)
                        if is_correct:
                            correct_answers += 1
                        else:
                            wrong_answers += 1
                        last_answer_correct = is_correct
                        need_new_trial = True
                        feedback_until = time.time() + 0.15

                    # Se premo FRECCIA SINISTRA
                    elif event.key == pygame.K_LEFT:
                        user_answer = False
                        is_correct = (user_answer == trial.expected_answer)
                        score = apply_answer(score, is_correct)
                        if is_correct:
                            correct_answers += 1
                        else:
                            wrong_answers += 1
                        last_answer_correct = is_correct
                        need_new_trial = True
                        feedback_until = time.time() + 0.15
                
                if state == "RESULTS":
                    # Se premo R, resetto il gioco
                    if event.key == pygame.K_r:
                        state = "PLAYING"
                        # Resetto tutti i valori del gioco
                        start_time = time.time()
                        score = 0
                        correct_answers = 0
                        wrong_answers = 0
                        trial = generate_trial(random.Random())

        screen.fill((0, 0, 0)) # Colore nero
        
        if state == "PLAYING":
            if time.time() < feedback_until:
                draw_card(screen, trial, last_answer_correct)
            else:
                draw_card(screen, trial, None)
            
            draw_timer(screen, elapsed)
        elif state == "RESULTS":
            draw_results(screen, score, correct_answers, wrong_answers)
            
        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()

if __name__ == "__main__":
    main()
