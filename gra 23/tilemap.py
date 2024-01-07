import pygame
from tile import Tile, Metal
from settings import TILE_SIZE, NEIGHBOUR_OFFSETS, PHYSICS_TILES
from support import load_image

class Tilemap:
    def __init__(self) -> None:
        self.tile_map = {}
        self.offgrid_tiles = []
        self.magnets = pygame.sprite.Group()
        assets = {
            'grass': load_image('images/tiles/grass.png'),
            'stone': load_image('images/tiles/stone.png'),
            'metal': load_image('images/tiles/metal.png')
        }

        for i in range(20):
            self.tile_map[str(-3 + i) + ';10'] = Tile([], 'grass', ((-3 + i) * TILE_SIZE, 10 * TILE_SIZE), assets['grass'])
            self.tile_map[str(-3 + i) + ';15'] = Tile([], 'grass', ((-3 + i) * TILE_SIZE, 15 * TILE_SIZE), assets['grass'])
            self.tile_map['10;' + str(5 + i)] = Tile([], 'stone', (10 * TILE_SIZE, (5 + i) * TILE_SIZE), assets['stone'])
        self.tile_map['-2;6'] = Metal(self.magnets, 'metal', (-2 * TILE_SIZE, 6 * TILE_SIZE), -1,  assets['metal'])
        self.tile_map['10;1'] = Metal(self.magnets, 'metal', (10 * TILE_SIZE, 1 * TILE_SIZE), -1,  assets['metal'])
        self.tile_map['-3;15'] = Metal(self.magnets, 'metal', (-3 * TILE_SIZE, 15 * TILE_SIZE), -1,  assets['metal'])
        self.tile_map['-7;14'] = Metal(self.magnets, 'metal', (-7 * TILE_SIZE, 14 * TILE_SIZE), 3,  assets['metal'])
        self.tile_map['9;2'] = Tile([], 'stone', (9 * TILE_SIZE, 2 * TILE_SIZE), assets['stone'])
        self.tile_map['10;2'] = Tile([], 'stone', (10 * TILE_SIZE, 2 * TILE_SIZE), assets['stone'])
        self.tile_map['11;2'] = Tile([], 'stone', (11 * TILE_SIZE, 2 * TILE_SIZE), assets['stone'])
    
    def tiles_around(self, pos):
        x, y = pos
        tiles = []
        tile_location_x = int(x // TILE_SIZE)
        tile_location_y = int(y // TILE_SIZE)

        for offset_x in range(-3, 3):
            for offset_y in range(-3, 3):
                check_loc = str(tile_location_x + offset_x) + ';' + str(tile_location_y + offset_y)
                if check_loc in self.tile_map:
                    tile = self.tile_map[check_loc]
                    if tile.type in PHYSICS_TILES:
                        tiles.append(self.tile_map[check_loc].hitbox)
        return tiles

    def get_magnetic_force(self, pos, charge):
        force = pygame.Vector2(0, 0)
        for magnet in self.magnets.sprites():
            force += magnet.get_force(pos, charge)
        return force

    def render(self, display: pygame.Surface, offset):
        for x in range(int(offset[0] // TILE_SIZE), (int(offset[0] + display.get_width()) // TILE_SIZE) + 1):
            for y in range(int(offset[1] // TILE_SIZE), (int(offset[1] + display.get_height()) // TILE_SIZE) + 1):
                location = f'{str(x)};{str(y)}'
                if location in self.tile_map:
                    tile = self.tile_map[location]
                    offset_pos = tile.rect.topleft - offset * tile.depth
                    display.blit(tile.image, offset_pos)




