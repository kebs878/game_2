import pygame
from bullets import Bullets
import random


class Enemy:
    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.shots = []
        self.timer = 0

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def bullets_clock(self):
        self.timer += random.randint(1, 10)
        if self.timer > 120:
            self.shot()

    def shot(self) -> None:
        self.timer = 0
        bullet = Bullets(
            self.x,
            self.y,
        )
        self.shots.append(bullet)
