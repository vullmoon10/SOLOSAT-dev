import pygame


class FormulaEnemy:
    def __init__(self, x, question, speed=1.2):
        self.x = float(x)
        self.y = 550
        self.width = 150
        self.height = 70
        self.speed = speed
        self.question = question
        self.active = True

    @property
    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def update(self, player_x):
        if not self.active:
            return
        distance = player_x - self.x
        if abs(distance) > 80:
            self.x += self.speed if distance > 0 else -self.speed
