import pygame
import config
from bullets import Bullets
from game_object import GameObject


class Player(GameObject):
    def __init__(
        self,
        x,
        y,
        width=config.PLAYER_WIDTH,
        height=config.PLAYER_HEIGHT,
        color=config.LIME,
        speed=config.PLAYER_SPEED,
    ) -> None:
        super().__init__(x, y, width, height, color)
        self.speed = speed
        self.shots = []
        self.timer = 0
        self.lives = 6

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < config.SCREEN_WIDTH - self.width:
            self.x += self.speed

    def bullets_clock(self) -> None:
        self.timer += 1
        if self.timer > 10:
            self.shot()

    def shot(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.timer = 0
            bullet = Bullets(
                self.x,
                self.y,
            )
            self.shots.append(bullet)

