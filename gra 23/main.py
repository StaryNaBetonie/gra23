import pygame
from settings import *
from gameplay import Gameplay
from support import load_image

class Main:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.running = True
        self.display = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.FULLSCREEN|pygame.SCALED)
        self.game = Gameplay()
        self.inputs = {'w': False, 'a': False, 's': False, 'd': False, 'space': False, 'shift': False}
        self.pressed = {'w': False, 'a': False, 's': False, 'd': False, 'space': False, 'shift': False}
        self.background = load_image('images/background.png')
    
    def update(self):
        self.game.update(self.inputs, self.pressed)  
    
    def render(self):
        self.display.blit(self.background, (0, 0))
        self.game.render(self.display)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.stop()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.inputs['w'] = True
                    self.pressed['w'] = True
                if event.key == pygame.K_a:
                    self.inputs['a'] = True
                    self.pressed['a'] = True
                if event.key == pygame.K_s:
                    self.inputs['s'] = True
                    self.pressed['s'] = True
                if event.key == pygame.K_d:
                    self.inputs['d'] = True
                    self.pressed['d'] = True
                if event.key == pygame.K_SPACE:
                    self.inputs['space'] = True
                    self.pressed['space'] = True
                if event.key == pygame.K_LSHIFT:
                    self.inputs['shift'] = True
                    self.pressed['shift'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.inputs['w'] = False
                if event.key == pygame.K_a:
                    self.inputs['a'] = False
                if event.key == pygame.K_s:
                    self.inputs['s'] = False
                if event.key == pygame.K_d:
                    self.inputs['d'] = False
                if event.key == pygame.K_SPACE:
                    self.inputs['space'] = False
                if event.key == pygame.K_LSHIFT:
                    self.inputs['shift'] = False
                    
    def start(self):
        while self.running:
            self.clock.tick(FRAMERATE)
            self.events()
            self.render()
            self.update()
            self.pressed = {'w': False, 'a': False, 's': False, 'd': False, 'space': False, 'shift': False}
        
    def stop(self):
        self.running = False

if __name__ == '__main__':
    g = Main()
    g.start()
