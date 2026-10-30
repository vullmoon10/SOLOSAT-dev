import pygame

from config import GROUND_Y, GRAVITY, INITIAL_HP, INITIAL_LEVEL, INITIAL_EXP, INITIAL_MAX_EXP, JUMP_POWER, PLAYER_SPEED, WORLD_WIDTH


# 클래스 기능
class Player:  # ???? ??? ?? ??
    # 함수 기능
    def __init__(self, nickname="PLAYER"):  # ?? ?? ?? ??
        self.nickname = nickname  # 변수 기능
        self.width = 45  # 변수 기능
        self.height = 65  # 변수 기능
        self.x = 300.0  # 변수 기능
        self.y = GROUND_Y - self.height  # 변수 기능
        self.speed = PLAYER_SPEED  # 변수 기능
        self.velocity_y = 0.0  # 변수 기능
        self.on_ground = True  # 변수 기능
        self.hp = INITIAL_HP  # 변수 기능
        self.max_hp = INITIAL_HP  # 변수 기능
        self.level = INITIAL_LEVEL  # 변수 기능
        self.exp = INITIAL_EXP  # 변수 기능
        self.max_exp = INITIAL_MAX_EXP  # 변수 기능
        self.score = 0  # 변수 기능
        self.correct = 0  # 변수 기능
        self.wrong = 0  # 변수 기능
        self.solved = 0  # 변수 기능

    @property
    # 함수 기능
    def rect(self):  # ?? ??? ??? ??
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    # 함수 기능
    def update(self):  # ????? ? ?? ??
        keys = pygame.key.get_pressed()  # 변수 기능
        # 조건 분기
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # ?? ?? ?? ??
            self.x -= self.speed
        # 조건 분기
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # ??? ?? ?? ??
            self.x += self.speed  # ?? ??

        self.x = max(0, min(WORLD_WIDTH - self.width, self.x))  # 변수 기능
        self.velocity_y += GRAVITY  # ?? ??
        self.y += self.velocity_y  # ?? ??

        # 조건 분기
        if self.y + self.height >= GROUND_Y:  # ?? ?? ?? ??
            self.y = GROUND_Y - self.height  # 변수 기능
            self.velocity_y = 0  # 변수 기능
            self.on_ground = True  # 변수 기능
        else:  # ? ??? ??? ? ??
            self.on_ground = False  # 변수 기능

    # 함수 기능
    def jump(self):  # ???? ?? ??
        # 조건 분기
        if self.on_ground:  # ?? ?? ? ?? ??
            self.velocity_y = JUMP_POWER  # 변수 기능
            self.on_ground = False  # 변수 기능

    # 함수 기능
    def add_exp(self, amount):  # ??? ??? ??? ??
        self.exp += amount  # ?? ???
        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.level += 1  # ?? ??
            self.max_exp = int(self.max_exp * 1.25)  # 변수 기능

    # 함수 기능
    def apply_penalty(self, amount):  # ?? ?? ??
        self.score = max(0, self.score - amount)  # 변수 기능
