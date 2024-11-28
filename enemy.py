from game_object import GameObject
from bullets import Bullets
import random
import config


class Enemy(GameObject):
    def __init__(
        self,
        x: int,
        y: int,
        color: tuple[int, int, int],
        speed: int = config.ENEMY_SPEED,
        width: int = config.ENEMY_WIDTH,
        height: int = config.ENEMY_HEIGHT,
    ) -> None:
        super().__init__(x, y, width, height, color)
        self.shots: list[Bullets] = []
        self.timer = 0
        self.speed = speed
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
        self.change_direction()
        if self.direction == "left":
            self.x -= self.speed
            if self.x < 0:
                self.direction = "right"

        if self.direction == "right":
            self.x += self.speed
            if self.x > config.SCREEN_WIDTH - config.ENEMY_WIDTH:
                self.direction = "left"

    def change_direction(self) -> None:
        random_number = random.randint(0, 100)
        if random_number > 95:
            if self.direction == "right":
                self.direction = "left"
            else:
                self.direction = "right"
