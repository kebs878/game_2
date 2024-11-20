import pygame
import config

pygame.init()

class Game:
    def __init__(self):
        self.screen_width = config.SCREEN_WIDTH
        self.screen_height = config.SCREEN_HEIGHT
        self.running = True

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("GAME 1")
    
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running == True:
            self.screen.fill(config.WHITE)
            self.event_loop()
            pygame.display.flip()
