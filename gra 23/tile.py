from typing import Any
import pygame
from pygame.surface import Surface as Surface
from settings import TILE_SIZE, SCREEN_W, SCREEN_H, ECONSTANT
from random import randint

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, type, pos, image = pygame.Surface((1, 1)), z=1, depth=1) -> None:
        super().__init__(groups)
        self.type = type
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.copy()
        self.depth = depth
        self.z = z
    
    def set_hitbox(self, size):
        self.hitbox = pygame.Rect(self.rect.topleft, size)
        self.rect.center = self.hitbox.center

class MovingTile(Tile):
    def __init__(self, groups, type, pos, image=pygame.Surface((0, 0)), z=1, depth=1, velocity=pygame.Vector2(0, 0)) -> None:
        super().__init__(groups, type, pos, image, z, depth)
        self.velocity = velocity
        self.pos = pygame.Vector2(self.hitbox.center)
    
    def update(self) -> None:
        self.pos += self.velocity
        self.hitbox.center = self.pos
        self.rect.center = self.hitbox.center

class Metal(Tile):
    def __init__(self, groups, type, pos, charge, image=pygame.Surface((1, 1)), z=1, depth=1) -> None:
        super().__init__(groups, type, pos, image, z, depth)
        self.charge = charge

    def get_force(self, pos, charge):
        x2, y2 = pos
        relative = pygame.Vector2(x2 - self.hitbox.centerx, y2 - self.hitbox.centery)
        distance = relative.magnitude()
        force = ECONSTANT * charge * self.charge / distance**2
        sin = relative.y / distance
        cos = relative.x / distance
        return pygame.Vector2(force * cos, force * sin)

    
