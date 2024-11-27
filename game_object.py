import pygame
from pygame import Surface


class GameObject:
    def __init__(
        self, x: int, y: int, width: int, height: int, color: tuple[int, int, int]
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
