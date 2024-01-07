import pygame
from os import walk

MAIN_PATH = 'images/'

def load_image(path):
    image = pygame.transform.scale2x(pygame.image.load(path).convert())
    image.set_colorkey((0, 0, 0))
    return image

def import_folder(path):
    surface_list = []
    
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = f'{path}/{image}'
            image_surface = load_image(full_path).convert()
            surface_list.append(image_surface)
    return surface_list

def import_cut_graphicks(path, tile_number):
    surface = load_image(path)
    size_x, size_y = surface.get_size()[0] // tile_number[0], surface.get_size()[1] // tile_number[1]

    cut_tiles = []
    for row in range(tile_number[1]):
        for col in range(tile_number[0]):
            x = col * size_x
            y = row * size_y
            new_surf = pygame.Surface((size_x, size_y), flags = pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, size_x, size_y))
            cut_tiles.append(new_surf)
    return cut_tiles