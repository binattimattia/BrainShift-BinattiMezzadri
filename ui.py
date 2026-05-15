import pygame
from config import *
from models import Trial

def draw_card(surface: pygame.Surface, trial: Trial, is_correct: bool):
    """
    Disegna la carta sullo schermo
    
    Args:
        surface: La superficie di disegno
        trial: La carta da disegnare
        is_correct: Se la risposta è corretta
    """
    x = (surface.get_width() - CARD_W) // 2
    if trial.position.upper() == "TOP":
        y = surface.get_height() - CARD_H - 400
    else:
        y = surface.get_height() - CARD_H - 110
    card_rect = pygame.Rect(x, y, CARD_W, CARD_H)

    color = COLOR_WHITE

    if is_correct:
        color = COLOR_GREEN
    if is_correct is False:
        color = COLOR_RED

    pygame.draw.rect(surface, color, card_rect, border_radius=15)
    pygame.draw.rect(surface, COLOR_BLACK, card_rect, 3, border_radius=15)

    font = pygame.font.Font("fonts/Ubuntu-Bold.ttf", 80)
    text_str = f"{trial.letter}{trial.number}"
    text_surf = font.render(text_str, True, COLOR_YELLOW)
    text_rect = text_surf.get_rect(center=card_rect.center)
    surface.blit(text_surf, text_rect)

def draw_timer(surface: pygame.Surface, elapsed: float):
    """
    Disegna il timer sullo schermo
    
    Args:
        surface: La superficie di disegno
        elapsed: Il tempo trascorso
    """
    # Calcolo il tempo rimanente e la percentuale per la barra
    time_left = max(0, 60 - elapsed)
    ratio = time_left / 60.0
    
    # Dimensioni della barra
    max_width = 600
    height = 40
    current_width = int(max_width * ratio)
    
    # Posizione (centrata in alto)
    x = (surface.get_width() - max_width) // 2
    y = 20
    
    # Scelta del colore: verde normalmente, rosso negli ultimi 10 secondi
    color = COLOR_RED if time_left <= 10 else COLOR_GREEN
    
    # Disegno sfondo bianco
    bg_rect = pygame.Rect(x, y, max_width, height)
    pygame.draw.rect(surface, COLOR_WHITE, bg_rect, border_radius=15)
    
    # Disegno barra del tempo rimasto
    if current_width > 0:
        fill_rect = pygame.Rect(x, y, current_width, height)
        # Se la barra è molto corta, potremmo avere problemi con il raggio se è maggiore della larghezza
        # ma pygame lo gestisce internamente.
        pygame.draw.rect(surface, color, fill_rect, border_radius=15)
        
    # Disegno bordo nero
    pygame.draw.rect(surface, COLOR_BLACK, bg_rect, 2, border_radius=15)
    
    # Testo dei secondi rimanenti al centro
    font = pygame.font.Font("fonts/Ubuntu-Italic.ttf", 20)
    text_surf = font.render(f"Tempo: {int(time_left)}s", True, COLOR_BLACK)
    text_rect = text_surf.get_rect(center=bg_rect.center)
    surface.blit(text_surf, text_rect)

def draw_results(surface: pygame.Surface, score: int, correct: int, wrong: int):
    """
    Disegna i risultati finali sullo schermo
    
    Args:
        surface: La superficie di disegno
        score: Il punteggio finale
        correct: Il numero di risposte corrette
        wrong: Il numero di risposte errate
    """
    total = correct + wrong
    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0.0

    # Font
    font_title = pygame.font.Font("fonts/Ubuntu-Bold.ttf", 48)
    font_text = pygame.font.Font("fonts/Ubuntu-Regular.ttf", 32)
    font_small = pygame.font.Font("fonts/Ubuntu-Italic.ttf", 24)

    # Scritte
    title_surf = font_title.render("TEMPO SCADUTO!", True, COLOR_RED) # Rosso
    score_surf = font_text.render(f"Punteggio Finale: {score}", True, COLOR_WHITE)
    correct_surf = font_text.render(f"Corrette: {correct}", True, COLOR_WHITE)
    wrong_surf = font_text.render(f"Errate: {wrong}", True, COLOR_WHITE)
    acc_surf = font_text.render(f"Accuratezza: {accuracy:.1f}%", True, COLOR_WHITE)
    restart_surf = font_small.render("Premi R per rigiocare", True, COLOR_GREY) # Grigio

    # Posizionamento e rendering sullo schermo
    # Posizioniamo tutto al centro, con diverse altezze (Y)
    center_x = surface.get_width() // 2
    surface.blit(title_surf, title_surf.get_rect(center=(center_x, 100)))
    surface.blit(score_surf, score_surf.get_rect(center=(center_x, 200)))
    surface.blit(correct_surf, correct_surf.get_rect(center=(center_x, 260)))
    surface.blit(wrong_surf, wrong_surf.get_rect(center=(center_x, 300)))
    surface.blit(acc_surf, acc_surf.get_rect(center=(center_x, 340)))
    surface.blit(restart_surf, restart_surf.get_rect(center=(center_x, 450)))

def draw_rules(surface: pygame.Surface, trial: Trial):
    """
    Disegna la regola del gioco sullo schermo

    Args:
        surface: La superficie di disegno
        trial: La carta da disegnare
    """
    # avrà la stessa y delle card 
    # se è sopra, sarà a destra della card, altrimenti a sinistra
    if trial.position.upper() == "TOP":
        x = 900
        y = surface.get_height() - RULES_H - 450
    else:
        x = 50
        y = surface.get_height() - RULES_H - 160
    card_rect = pygame.Rect(x, y, RULES_W, RULES_H)

    color = COLOR_WHITE

    pygame.draw.rect(surface, color, card_rect, border_radius=15)
    pygame.draw.rect(surface, COLOR_BLACK, card_rect, 3, border_radius=15)

    font = pygame.font.Font("fonts/Ubuntu-Italic.ttf", 25)
    text_str = f"Il numero è pari?" if trial.position.upper() == "TOP" else f"La lettera è una vocale?"
    text_surf = font.render(text_str, True, COLOR_BLACK)
    text_rect = text_surf.get_rect(center=card_rect.center)
    surface.blit(text_surf, text_rect)
