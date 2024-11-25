import pygame
import config
from player import Player
from enemy import Enemy


class Game:
    def __init__(self) -> None:
        self.screen_width = config.SCREEN_WIDTH
        self.screen_height = config.SCREEN_HEIGHT
        self.running = True

        self.enemy_1 = Enemy(200, 100, 30, 30, config.RED)
        self.enemy_2 = Enemy(600, 50, 30, 30, config.YELLOW)
        self.enemy_3 = Enemy(350, 75, 30, 30, config.BLACK)
        self.enemies = [self.enemy_1 , self.enemy_2, self.enemy_3]

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("GAME 1")

        self.player = Player(
            config.SCREEN_WIDTH // 2,
            config.SCREEN_HEIGHT - config.PLAYER_HEIGHT,
            config.PLAYER_WIDTH,
            config.PLAYER_HEIGHT,
            config.LIME,
            config.PLAYER_SPEED,
        )

    def event_loop(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def move_bullets(self) -> None:
        for bullet in self.player.shots:
            bullet.draw(self.screen)
            bullet.move()
            if bullet.y < 0:
                self.player.shots.remove(bullet)

    def handle_collision(self) -> None:
        for enemy in self.enemies:
            for bullet in self.player.shots:
                if enemy.get_rect().colliderect(bullet.get_rect()):
                    self.enemies.remove(enemy)
                    self.player.shots.remove(bullet)


    def run(self) -> None:
        clock = pygame.time.Clock()
        while self.running:
            self.screen.fill(config.WHITE)
            self.player.draw(self.screen)
            self.player.move()
            self.player.bullets_clock()
            self.move_bullets()
            self.enemy_1.draw(self.screen)
            self.enemy_2.draw(self.screen)
            self.enemy_3.draw(self.screen)
            self.handle_collision()
            self.event_loop()
            pygame.display.flip()
            clock.tick(30)
