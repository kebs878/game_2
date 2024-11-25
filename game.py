import pygame
import config
from player import Player
from enemy import Enemy


class Game:
    def __init__(self) -> None:
        self.screen_width = config.SCREEN_WIDTH
        self.screen_height = config.SCREEN_HEIGHT
        self.font = pygame.font.Font(None, config.FONT_SIZE)

        self.reset_game()

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

    def reset_game(self):
        self.game_over = False
        self.enemy_1 = Enemy(200, 100, 30, 30, config.RED)
        self.enemy_2 = Enemy(600, 50, 30, 30, config.YELLOW)
        self.enemy_3 = Enemy(350, 75, 30, 30, config.BLACK)
        self.enemies = [self.enemy_1 , self.enemy_2, self.enemy_3]

    def event_loop(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset_game()

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
                    print(self.enemy_1)
                    self.player.shots.remove(bullet)
                if self.enemies == []:
                    self.game_over = True


    def run(self) -> None:
        clock = pygame.time.Clock()
        while self.running:
            self.event_loop()
            self.screen.fill(config.WHITE)
            if self.game_over == False:
                self.player.draw(self.screen)
                self.player.move()
                self.player.bullets_clock()
                self.move_bullets()
                for enemy in self.enemies:
                    enemy.draw(self.screen)
                self.handle_collision()
            else:
                game_over_text = self.font.render("THE GAME IS OVER ", True, config.RED)
                self.screen.blit(game_over_text, (300, 225))
            pygame.display.flip()
            clock.tick(30)
