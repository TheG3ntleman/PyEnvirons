import pygame
from . import Transform2D

class GameObject:

    def __init__(self, sprite):
        self.sprite = sprite
        self.transform = Transform2D.Transform2D()

    def object_update(self):
        pass

    def set_pos(self, pos):
        self.transform.pos = pos

    def set_rot(self, rot):
        self.transform.rot = rot

    def get_sprite(self):
        sprite = pygame.transform.rotate(self.sprite.surface, self.transform.rot)
        sprite = pygame.transform.scale(sprite, [self.sprite.surface.get_width() * self.transform.scale[0],
                                                 self.sprite.surface.get_height() * self.transform.scale[1]])
        return sprite