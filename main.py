import pygame
import random
from config import *
from ui import draw_card, draw_timer, draw_results, draw_rules
from generator import generate_trial
from scoring import apply_answer
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    running = True
    rng = random.Random(SEED)
    trial = generate_trial(rng)
    start_time = time.time()
    score = correct_answers = wrong_answers = feedback_until = 0
    state = "PLAYING"
    need_new_trial = False
    last_answer_correct = None

    while running:
        # Aggiornamento logica di gioco e tempo
        if state == "PLAYING":
            elapsed = time.time() - start_time
            if elapsed >= GAME_DURATION:
                state = "RESULTS"
            
            # Genera la nuova carta solo quando scade il timer del feedback
            if time.time() >= feedback_until and need_new_trial:
                trial = generate_trial(rng)
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
                    if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                        # Se è FRECCIA DESTRA, user_answer è True, altrimenti è False
                        user_answer = (event.key == pygame.K_RIGHT)
                        
                        is_correct = (user_answer == trial.expected_answer)
                        score = apply_answer(score, is_correct)
                        
                        if is_correct:
                            correct_answers += 1
                        else:
                            wrong_answers += 1
                            
                        # Setup per il feedback e nuova carta
                        last_answer_correct = is_correct
                        need_new_trial = True
                        feedback_until = time.time() + FEEDBACK_DURATION
                
                if state == "RESULTS":
                    # Se premo R, resetto il gioco
                    if event.key == pygame.K_r:
                        state = "PLAYING"
                        # Resetto tutti i valori del gioco
                        start_time = time.time()
                        score = 0
                        correct_answers = 0
                        wrong_answers = 0
                        trial = generate_trial(rng)

        screen.fill((0, 0, 0)) # Colore nero
        
        if state == "PLAYING":
            if time.time() < feedback_until:
                draw_card(screen, trial, last_answer_correct)
            else:
                draw_card(screen, trial, None)
            
            if correct_answers < 10:
                draw_rules(screen)
            
            draw_timer(screen, elapsed)
        elif state == "RESULTS":
            draw_results(screen, score, correct_answers, wrong_answers)
            
        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()

if __name__ == "__main__":
    main()
