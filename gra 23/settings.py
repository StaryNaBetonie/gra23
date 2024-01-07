from enum import Enum

SCREEN_W = 1920
SCREEN_H = 1080
FRAMERATE = 60
GRAVITY = 1
PLAYER_SPEED = 7
TILE_SIZE = 64
NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone', 'metal'}
PLAYER_IMG_SIZE = (100, 60)
ECONSTANT = 1

class EType(Enum):
    Player = 1
    cloud = 2