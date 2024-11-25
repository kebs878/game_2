import pygame


class Bullets:
    def __init__(self, x, y, width, height, color, speed) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self) -> None:
        self.y -= self.speed

    def get_rect(self):
      return pygame.Rect(self.x, self.y, self.width, self.height)