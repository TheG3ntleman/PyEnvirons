import pygame

class Sprite:
    def __init__(self, source):
        self.surface = pygame.image.load(source)