import config
from game_object import GameObject

class Bullets(GameObject):
    def __init__(
        self,
        x,
        y,
        width=config.BULLETS_WIDTH,
        height=config.BULLETS_HEIGHT,
        color=config.RED,
        speed=config.BULLETS_SPEED,
    ) -> None:
        super().__init__(x, y, width, height, color)
        self.speed = speed

    def move(self, type=1) -> None:
        if type == 1:
            self.y -= self.speed
        if type == 2:
            self.y += self.speed

