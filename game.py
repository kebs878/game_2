import pygame
import config
from player import Player

class Game:
    def __init__(self) -> None:
        self.screen_width = config.SCREEN_WIDTH
        self.screen_height = config.SCREEN_HEIGHT
        self.running = True

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("GAME 1")

        self.player = Player(0, self.screen_height // 2, config.PLAYER_WIDTH, config.PLAYER_HEIGHT, config.YELLOW)
    
    def event_loop(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self) -> None:
        while self.running == True:
            self.screen.fill(config.WHITE)
            self.player.draw(self.screen)
            self.event_loop()
            pygame.display.flip()

