import pygame
import config
from bullets import Bullets


class Player:
    def __init__(self, x, y, width, height, color, speed) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.shots = []
        self.timer = 0

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

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
                config.BULLETS_WIDTH,
                config.BULLETS_HEIGHT,
                config.RED,
                config.BULLETS_SPEED,
            )
            self.shots.append(bullet)
