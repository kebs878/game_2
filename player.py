import pygame
import config

class Player:
    def __init__(self, x, y, width, height, color, speed) -> None:
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.color = color
      self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
          self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < config.SCREEN_WIDTH - self.width:
          self.x += self.speed 