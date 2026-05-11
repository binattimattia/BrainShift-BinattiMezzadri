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
    