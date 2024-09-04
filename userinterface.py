import pygame
from constants import *


class UserInterface:
    def __init__(self, screen, font_size=36):
        self.screen = screen
        self.font = pygame.font.SysFont(None, font_size)

    def render_text(self, text, position):
        text_surface = self.font.render(text, True, (255, 255, 255))  # White color
        self.screen.blit(text_surface, position)

    def render(self, player, kill_count):
        self.render_text(f"Health: {player.health}", (SCREEN_WIDTH - 150, 10))
        self.render_text(f"Armour: {player.armour}", (SCREEN_WIDTH - 150, 40))
        self.render_text(f"Score: {kill_count}", (SCREEN_WIDTH // 2 - 50, 10))