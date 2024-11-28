from enum import Enum

class GameState(Enum):
    MENU = 1
    GAME_OVER = 2
    ACTIV_GAME = 3

class GameDifficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

