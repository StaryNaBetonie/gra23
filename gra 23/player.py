import pygame
from entities import PhysicsEntity
from settings import PLAYER_SPEED

class Player(PhysicsEntity):
    def __init__(self, groups, pos) -> None:
        super().__init__(groups, 'player', pos)
        self.movement_speed = PLAYER_SPEED
        self.set_hitbox((32, 120))
        self.movement_x = 0
        self.can_change_direction = True

        self.charge = 0
        self.delta_charge = 1000
        self.max_charge = 50000
    
    def move(self, tiles, movement, magnetic_force: pygame.Vector2):
        self.velocity += magnetic_force
        return super().move(tiles, movement)

    def jump(self):
        self.velocity.y = -20
    
    def gest_status(self, movement_x):
        self.air_time += 1
        if self.collisions['down']: self.air_time = 0

        if self.air_time > 4:
            self.can_change_direction = False
            if self.collisions['left'] or self.collisions['right']: self.movement_x = 0
            if self.velocity.y < -1: self.set_action('jump')
            else: self.set_action('fall')
        elif movement_x != 0:
            self.can_change_direction = True
            self.set_action('run')
        else:
            self.can_change_direction = True
            self.set_action('idle')
    
    def get_direction(self, inputs):
        if not self.can_change_direction: return
        self.movement_x = self.movement_speed * (inputs['d'] - inputs['a'])
    
    def charging(self, inputs):
        delta = self.delta_charge
        if not inputs['shift']: delta *= -1
        self.charge = max(min(self.max_charge, self.charge + delta), 0)
    
    def update(self, inputs, pressed, tiles, magnetic_force):
        self.get_direction(inputs)
        self.charging(inputs)
        self.move(tiles, pygame.Vector2(self.movement_x, 0), magnetic_force)
        self.gest_status(self.movement_x)
        self.animate()
        self.animation.update()
        if pressed['space']: self.jump()


