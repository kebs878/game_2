import config
from game_object import GameObject


class Bullets(GameObject):
    def __init__(
        self,
        x: int,
        y: int,
        width: int = config.BULLETS_WIDTH,
        height: int = config.BULLETS_HEIGHT,
        color: tuple[int, int, int] = config.RED,
        speed: int = config.BULLETS_SPEED,
    ) -> None:
        super().__init__(x, y, width, height, color)
        self.speed = speed

    def move(self, type: int = 1) -> None:
        if type == 1:
            self.y -= self.speed
        if type == 2:
            self.y += self.speed
