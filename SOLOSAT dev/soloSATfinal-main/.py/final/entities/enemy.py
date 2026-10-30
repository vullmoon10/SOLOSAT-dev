import pygame


# 클래스 기능
class FormulaEnemy:  # ??? ?? ? ??
    # 함수 기능
    def __init__(self, x, question, speed=1.2):  # ?? ?? ?? ??
        self.x = float(x)  # 변수 기능
        self.y = 550  # 변수 기능
        self.width = 150  # 변수 기능
        self.height = 70  # 변수 기능
        self.speed = speed  # 변수 기능
        self.question = question  # 변수 기능
        self.active = True  # 변수 기능

    @property
    # 함수 기능
    def rect(self):  # ?? ??? ??? ??
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    # 함수 기능
    def update(self, player_x):  # ????? ? ?? ??
        # 조건 분기
        if not self.active:  # ??? ? ?? ??
            return
        distance = player_x - self.x  # 변수 기능
        # 조건 분기
        if abs(distance) > 80:  # ?? ?? ?? ? ??
            self.x += self.speed if distance > 0 else -self.speed  # ?? ??
