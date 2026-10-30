# settings.py 
# 게임의 공통 설정을 모아 두는 파일이야.
import pygame

# [수정 가능] 화면 설정
WIDTH = 1000
HEIGHT = 600
FPS = 60
TITLE = "SOLO SAT"

# [수정 가능] 플레이어 물리 설정
MOVE_SPEED = 4
GRAVITY = 0.55
JUMP_POWER = -11.5
MAX_FALL_SPEED = 12

# [수정 가능] 게임 규칙
MAX_HP = 100
CORRECT_SCORE = 100
WRONG_DAMAGE = 10
QUESTION_TIME = 30

# 색상
SKY = (126, 196, 235)
MOUNTAIN = (150, 176, 196)
GRASS = (81, 170, 89)
PLATFORM_COLOR = (112, 133, 92)
DIRT = (132, 86, 53)
BLUE = (65, 75, 225)
RED = (210, 65, 65)
WHITE = (255, 255, 255)
DARK = (39, 54, 67)
CREAM = (250, 249, 239)
GRAY = (232, 232, 240)
YELLOW = (255, 220, 70)

GROUND_Y = 520

pygame.font.init()
FONT = pygame.font.SysFont("malgungothic", 22)
SMALL = pygame.font.SysFont("malgungothic", 16)
TITLE_FONT = pygame.font.SysFont("malgungothic", 27)
BIG = pygame.font.SysFont("malgungothic", 34)


