# quiz.py
#문제 출제와 정답 판정, 제한 시간, 점수·체력 변화를 담당해.

import pygame

from settings import (
    MAX_HP, CORRECT_SCORE, WRONG_DAMAGE,
    QUESTION_TIME
)


class Quiz:
    def __init__(self):
        self.enemy = None
        self.started = 0
        self.duration = QUESTION_TIME
        self.selected = 0
        self.feedback = ""
        self.feedback_until = 0

    @property
    def active(self):
        return self.enemy is not None

    def open(self, enemy):
        if not enemy.active:
            return

        self.enemy = enemy
        self.started = pygame.time.get_ticks()
        self.duration = enemy.question.get(
            "time", QUESTION_TIME
        )
        self.selected = 0

    def remaining(self):
        elapsed = (
            pygame.time.get_ticks() - self.started
        ) / 1000
        return max(0, self.duration - elapsed)

    def submit(self, index):
        if not self.active:
            return None

        question = self.enemy.question

        if not 0 <= index < len(question["choices"]):
            return None

        enemy = self.enemy

        if index == question["answer"]:
            defeated = enemy.defeat()
            score = enemy.data["score"]
            result = {
                "correct": True,
                "damage": 0,
                "score": score,
                "defeated": defeated,
                "message": f"정답! +{score}점",
            }
        else:
            result = {
                "correct": False,
                "damage": WRONG_DAMAGE,
                "score": 0,
                "defeated": False,
                "message": f"오답! 체력 -{WRONG_DAMAGE}",
            }

        self.feedback = result["message"]
        self.feedback_until = (
            pygame.time.get_ticks() + 1000
        )
        self.enemy = None
        return result

    def check_timeout(self):
        if self.active and self.remaining() <= 0:
            self.feedback = "시간 초과!"
            self.feedback_until = (
                pygame.time.get_ticks() + 1000
            )
            self.enemy = None

            return {
                "correct": False,
                "damage": WRONG_DAMAGE,
                "score": 0,
                "defeated": False,
                "message": "시간 초과!",
            }

        return None