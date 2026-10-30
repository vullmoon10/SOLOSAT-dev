import pygame

from config import GROUND_Y, GRAVITY, INITIAL_HP, INITIAL_LEVEL, INITIAL_EXP, INITIAL_MAX_EXP, JUMP_POWER, PLAYER_SPEED, WORLD_WIDTH


class Player:
    def __init__(self, nickname="PLAYER"):
        self.nickname = nickname
        self.width = 45
        self.height = 65
        self.x = 300.0
        self.y = GROUND_Y - self.height
        self.speed = PLAYER_SPEED
        self.velocity_y = 0.0
        self.on_ground = True
        self.hp = INITIAL_HP
        self.max_hp = INITIAL_HP
        self.level = INITIAL_LEVEL
        self.exp = INITIAL_EXP
        self.max_exp = INITIAL_MAX_EXP
        self.score = 0
        self.correct = 0
        self.wrong = 0
        self.solved = 0

    @property
    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed

        self.x = max(0, min(WORLD_WIDTH - self.width, self.x))
        self.velocity_y += GRAVITY
        self.y += self.velocity_y

        if self.y + self.height >= GROUND_Y:
            self.y = GROUND_Y - self.height
            self.velocity_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_POWER
            self.on_ground = False

    def add_exp(self, amount):
        self.exp += amount
        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.level += 1
            self.max_exp = int(self.max_exp * 1.25)

    def apply_penalty(self, amount):
        self.score = max(0, self.score - amount)
