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
