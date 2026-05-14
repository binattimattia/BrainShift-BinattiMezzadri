import pygame
from config import *
from models import Trial

def draw_card(surface: pygame.Surface, trial: Trial):
    x = (surface.get_width() - CARD_W) // 2
    if trial.position.upper() == "TOP":
        y = 50
    else:
        y = surface.get_height() - CARD_H - 50
    card_rect = pygame.Rect(x, y, CARD_W, CARD_H)

    pygame.draw.rect(surface, (255, 255, 255), card_rect)
    pygame.draw.rect(surface, (0, 0, 0), card_rect, 3)

    font = pygame.font.SysFont("Arial", 48, bold=True)
    text_str = f"{trial.letter}{trial.number}"
    text_surf = font.render(text_str, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=card_rect.center)
    surface.blit(text_surf, text_rect)

def draw_timer(surface: pygame.Surface, elapsed: float):
    # Calcolo i secondi rimanenti
    time_left = max(0, 60 - int(elapsed))
    
    font = pygame.font.SysFont("Arial", 36, bold=True)
    text_str = f"Tempo: {time_left}s"
    
    # Se mancano meno di 10 secondi, lo coloro di rosso per attirare l'attenzione
    color = (255, 50, 50) if time_left <= 10 else (255, 255, 255)
    
    text_surf = font.render(text_str, True, color)
    # Lo posiziono in alto al centro
    text_rect = text_surf.get_rect(center=(surface.get_width() // 2, 20))
    surface.blit(text_surf, text_rect)

def draw_results(surface: pygame.Surface, score: int, correct: int, wrong: int):
    total = correct + wrong
    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0.0

    # Font
    font_title = pygame.font.SysFont("Arial", 48, bold=True)
    font_text = pygame.font.SysFont("Arial", 32)
    font_small = pygame.font.SysFont("Arial", 24, italic=True)

    # Scritte
    title_surf = font_title.render("TEMPO SCADUTO!", True, (255, 200, 50)) # Giallo/Arancio
    score_surf = font_text.render(f"Punteggio Finale: {score}", True, (255, 255, 255))
    correct_surf = font_text.render(f"Corrette: {correct}", True, (255, 255, 255))
    wrong_surf = font_text.render(f"Errate: {wrong}", True, (255, 255, 255))
    acc_surf = font_text.render(f"Accuratezza: {accuracy:.1f}%", True, (255, 255, 255))
    restart_surf = font_small.render("Premi R per rigiocare", True, (150, 150, 150)) # Grigio

    # Posizionamento e rendering sullo schermo
    # Posizioniamo tutto al centro, con diverse altezze (Y)
    center_x = surface.get_width() // 2
    surface.blit(title_surf, title_surf.get_rect(center=(center_x, 100)))
    surface.blit(score_surf, score_surf.get_rect(center=(center_x, 200)))
    surface.blit(correct_surf, correct_surf.get_rect(center=(center_x, 260)))
    surface.blit(wrong_surf, wrong_surf.get_rect(center=(center_x, 300)))
    surface.blit(acc_surf, acc_surf.get_rect(center=(center_x, 340)))
    surface.blit(restart_surf, restart_surf.get_rect(center=(center_x, 450)))
