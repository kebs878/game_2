import pygame
import config


class Bullets:
    def __init__(
        self,
        x,
        y,
        width=config.BULLETS_WIDTH,
        height=config.BULLETS_HEIGHT,
        color=config.RED,
        speed=config.BULLETS_SPEED,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, type = 1) -> None:
        if type == 1:
            self.y -= self.speed
        if type == 2:
            self.y += self.speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
