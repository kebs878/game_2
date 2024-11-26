from game_object import GameObject
from bullets import Bullets
import random
import config

class Enemy(GameObject):
    def __init__(self, x, y, width, height, color) -> None:
        super().__init__(x, y, width, height, color)
        self.shots = []
        self.timer = 0
        self.speed = config.ENEMY_SPEED
        self.direction = "left"

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

    def move(self) -> None:
        if self.direction == 'left':
            self.x -= self.speed
            if self.x < 0:
                self.direction = 'right'
        
        if self.direction == "right":
            self.x += self.speed
            if self.x > config.SCREEN_WIDTH - config.ENEMY_WIDTH:
                self.direction = 'left'

        

