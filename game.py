import pygame
import config
from player import Player
from enemy import Enemy
import random
from enums import GameState, GameDifficulty


class Game:
    def __init__(self) -> None:
        self.screen_width = config.SCREEN_WIDTH
        self.screen_height = config.SCREEN_HEIGHT
        self.font = pygame.font.Font(None, config.FONT_SIZE)
        self.running = True
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("GAME 1")
        self.state = GameState.MENU

    def reset_game(self, difficulty: GameDifficulty):
        self.state = GameState.ACTIV_GAME
        self.player = Player(
            config.SCREEN_WIDTH // 2,
            config.SCREEN_HEIGHT - config.PLAYER_HEIGHT,
        )
        if difficulty == GameDifficulty.EASY:
            lives = 6
            enemy_speed = config.ENEMY_SPEED
        elif difficulty == GameDifficulty.MEDIUM:
            lives = 4
            enemy_speed = config.ENEMY_SPEED * 2
        elif difficulty == GameDifficulty.HARD:
            lives = 2
            enemy_speed = config.ENEMY_SPEED * 4

        self.player.lives = lives
        enemy_1 = Enemy(200, 100, config.RED, enemy_speed)
        enemy_2 = Enemy(600, 50, config.YELLOW, enemy_speed)
        enemy_3 = Enemy(350, 75, config.BLACK, enemy_speed)
        self.enemies = [enemy_1, enemy_2, enemy_3]
        self.timer_enemy = 0
        self.killed_enemies = 0

    def spawn_enemy(self) -> None:
        self.timer_enemy += 1
        if self.timer_enemy > 150:
            self.timer_enemy = 0
            x = random.randint(0, config.SCREEN_WIDTH - config.ENEMY_WIDTH)
            y = random.randint(0, config.SCREEN_HEIGHT - 5 * config.ENEMY_HEIGHT)
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            enemy = Enemy(x, y, color)
            self.enemies.append(enemy)

    def event_loop(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.state == GameState.GAME_OVER and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.state = GameState.MENU

    def move_bullets(self) -> None:
        for bullet in self.player.shots:
            bullet.draw(self.screen)
            bullet.move()
            if bullet.y < 0:
                self.player.shots.remove(bullet)
        for enemy in self.enemies:
            for bullet in enemy.shots:
                bullet.draw(self.screen)
                bullet.move(2)

    def handle_collision(self) -> None:
        for enemy in self.enemies:
            for bullet in self.player.shots:
                if enemy.get_rect().colliderect(bullet.get_rect()):
                    self.enemies.remove(enemy)
                    self.player.shots.remove(bullet)
                    self.killed_enemies += 1
                    if self.enemies == []:
                        self.state = GameState.GAME_OVER

        for enemy in self.enemies:
            for bullet in enemy.shots:
                if self.player.get_rect().colliderect(bullet.get_rect()):
                    enemy.shots.remove(bullet)
                    self.player.lives -= 1
                    if self.player.lives == 0:
                        self.state = GameState.GAME_OVER

    def draw_lost(self):
        lost_text = self.font.render(
            f"YOU LOST-> KILLED {self.killed_enemies} ENEMIES", True, config.RED
        )
        self.screen.blit(lost_text, (200, 225))

    def draw_won(self):
        won_text = self.font.render("YOU WON", True, config.RED)
        self.screen.blit(won_text, (300, 225))

    def draw_lives(self):
        live_text = self.font.render(
            f"LIVES: {str(self.player.lives)}", True, config.BLUE
        )
        self.screen.blit(live_text, (10, 10))

    def draw_game_over(self):
        if self.enemies == []:
            self.draw_won()
        if self.player.lives == 0:
            self.draw_lost()

    def play_game(self):
        self.player.draw(self.screen)
        self.player.move()
        self.player.bullets_clock()
        self.move_bullets()
        for enemy in self.enemies:
            enemy.draw(self.screen)
            enemy.move()
            enemy.bullets_clock()
        self.handle_collision()
        self.spawn_enemy()
        self.draw_lives()

    def menu(self):
        menu_text = self.font.render("Select difficulty. 1.Easy 2.Medium 3.Hard", True, config.RED)
        self.screen.blit(menu_text, (100, 225))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.reset_game(GameDifficulty.EASY)
        if keys[pygame.K_2]:
            self.reset_game(GameDifficulty.MEDIUM)
        if keys[pygame.K_3]:
            self.reset_game(GameDifficulty.HARD)

    def run(self) -> None:
        clock = pygame.time.Clock()
        while self.running:
            self.event_loop()
            self.screen.fill(config.WHITE)
            if self.state == GameState.MENU:
                self.menu()
            elif self.state == GameState.GAME_OVER:
                self.draw_game_over()
            elif self.state == GameState.ACTIV_GAME:
                self.play_game()
    
            pygame.display.flip()
            clock.tick(30)
