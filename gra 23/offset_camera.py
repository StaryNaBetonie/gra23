import pygame

class CustomCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_heigth = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x += (player.rect.centerx - self.half_width - self.offset.x) / 30
        self.offset.y += (player.rect.centery - self.half_heigth - self.offset.y) / 30

        for sprite in sorted(self.sprites(), key = lambda sprite: (sprite.z)):
            offset_pos = sprite.rect.topleft - self.offset * sprite.depth
            self.display_surface.blit(sprite.image, offset_pos)
        
class CloudsCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_heigth = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x += (player.rect.centerx - self.half_width - self.offset.x) / 30
        self.offset.y += (player.rect.centery - self.half_heigth - self.offset.y) / 30

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.depth)[:-1]:
            offset_pos = sprite.rect.topleft - self.offset * sprite.depth
            x = offset_pos[0] % (self.display_surface.get_width() + sprite.image.get_width()) - sprite.image.get_width()
            y = offset_pos[1] % (self.display_surface.get_height() + sprite.image.get_height()) - sprite.image.get_height()
            self.display_surface.blit(sprite.image, (x, y))
        
