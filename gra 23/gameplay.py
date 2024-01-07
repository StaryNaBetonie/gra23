import pygame
from player import Player
from settings import *
from tilemap import Tilemap
from offset_camera import CustomCamera, CloudsCamera
from support import import_folder
from random import choice, randint
from tile import MovingTile

class Gameplay():
    def __init__(self) -> None:
        self.visible_group = CustomCamera()
        self.clouds_group = CloudsCamera()
        self.player = Player(self.visible_group, (500, 300))
        self.map = Tilemap()
        self.camera_offset = pygame.math.Vector2()
        self.add_clouds(10)
    
    def get_offset(self):
        self.camera_offset.x += (self.player.rect.centerx - SCREEN_W / 2 - self.camera_offset.x) / 30
        self.camera_offset.y += (self.player.rect.centery - SCREEN_H / 2 - self.camera_offset.y) / 30
    
    def add_clouds(self, count):
        cloud_sprites = import_folder('images/clouds')
        for i in range(count):
            groups = (self.clouds_group)
            x = randint(0, 9999)
            y = randint(0, 9999)
            image = choice(cloud_sprites)
            depth = randint(20, 70)/100
            velocity = pygame.Vector2(randint(1, 3)/4, 0)
            MovingTile(groups, EType.cloud, (x, y), image, 2, depth, velocity)

    def render(self, display):
        self.clouds_group.custom_draw(self.player)
        self.map.render(display, self.camera_offset)
        self.visible_group.custom_draw(self.player)
        pygame.draw.rect(display, '#000875', pygame.Rect(100, SCREEN_H - 100, 300 * self.player.charge / self.player.max_charge, 20))
    
    def update(self,  inputs, pressed):
        self.player.update(inputs, pressed, self.map.tiles_around(self.player.hitbox.center), self.map.get_magnetic_force(self.player.hitbox.center, self.player.charge))
        self.get_offset()
        self.clouds_group.update()