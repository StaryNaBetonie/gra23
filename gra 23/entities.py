import pygame
from settings import GRAVITY
from tile import Tile
from support import import_cut_graphicks
from animation import Animation

class PhysicsEntity(Tile):
    def __init__(self, groups, type, pos, z=1) -> None:
        super().__init__(groups, type, pos, z=z)
        self.velocity = pygame.Vector2(0, 0)
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.assets = {
            'idle': Animation(import_cut_graphicks(f'images/{type}/idle.png', (4, 1)), duration=8),
            'run': Animation(import_cut_graphicks(f'images/{type}/run.png', (6, 1)), duration=4),
            'jump': Animation(import_cut_graphicks(f'images/{type}/jump.png', (1, 1))),
            'fall': Animation(import_cut_graphicks(f'images/{type}/fall.png', (1, 1))),
        }

        self.air_time = 0
        self.action = ''
        self.flip = False
        self.set_action('idle')
    
    def set_action(self, action):
        if self.action == action: return
        self.action = action
        self.animation = self.assets[action].copy()
    
    def move(self, tiles, movement):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.velocity.y += GRAVITY
        self.velocity.x = max(min(20, self.velocity.x), -20)
        self.velocity.y = max(min(20, self.velocity.y), -20)
        frame_movement_x = self.velocity.x + movement.x
        frame_movement_y = self.velocity.y + movement.y

        self.hitbox.x += frame_movement_x
        for tile_hitbox in tiles:
            if self.hitbox.colliderect(tile_hitbox):
                if frame_movement_x > 0:
                    self.hitbox.right = tile_hitbox.left
                    self.collisions['right'] = True
                elif frame_movement_x < 0:
                    self.hitbox.left = tile_hitbox.right
                    self.collisions['left'] = True

        self.hitbox.y += frame_movement_y
        for tile_hitbox in tiles:
            if self.hitbox.colliderect(tile_hitbox):
                if frame_movement_y > 0:
                    self.hitbox.bottom = tile_hitbox.top
                    self.collisions['down'] = True
                elif frame_movement_y < 0:
                    self.hitbox.top = tile_hitbox.bottom
                    self.collisions['up'] = True
        
        if self.collisions['up'] or self.collisions['down']: self.velocity.y = 0
        if self.collisions['down']: self.velocity.x = 0
        self.rect.center = self.hitbox.center

        self.set_flip(movement)

    def animate(self):
        image = pygame.transform.flip(self.animation.image(), self.flip, False)
        self.rect = image.get_rect(topleft = self.rect.topleft)
        self.image = image
    
    def set_flip(self, movement):
        if movement.x > 0: self.flip = False
        if movement.x < 0: self.flip = True

    def update(self, tiles: list[pygame.Rect], movement = pygame.Vector2(0, 0)):
        self.move(tiles, movement)
        self.animate()
        self.animation.update()


