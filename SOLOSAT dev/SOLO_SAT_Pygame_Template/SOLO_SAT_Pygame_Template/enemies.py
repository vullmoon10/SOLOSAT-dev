# enemies.py
# 몹의 데이터와 외형을 담당해. 현재 영상에서 모든 종류의 몹을 확정할 수 없으므로, 아래 유형은 구조를 시험하기 위한 예시야.
import pygame
from questions import get_random_question


# [수정 가능] 몬스터 유형별 설정
ENEMY_TYPES = {
    "basic": {
        "color": (210, 65, 65),
        "size": (30, 30),
        "difficulty": "easy",
        "hp": 1,
        "score": 100,
    },
    "advanced": {
        "color": (130, 90, 65),
        "size": (36, 36),
        "difficulty": "medium",
        "hp": 1,
        "score": 200,
    },
}


class Enemy:
    def __init__(self, x, ground_y, enemy_type="basic"):
        self.enemy_type = enemy_type
        self.data = ENEMY_TYPES[enemy_type]

        width, height = self.data["size"]
        self.rect = pygame.Rect(
            x, ground_y - height,
            width, height
        )

        self.hp = self.data["hp"]
        self.active = True
        self.question = get_random_question(
            self.data["difficulty"]
        )

    def defeat(self):
        self.hp -= 1

        if self.hp <= 0:
            self.active = False
            return True

        # 다단계 전투를 위해 다음 문제를 부여
        self.question = get_random_question(
            self.data["difficulty"]
        )
        return False
    
#현재 world.py는 Enemy를 생성할 때 기본 유형을 사용해. 유형별 생성 확률이나 위치를 다르게 하려면 이 부분을 확장하면 돼.

# 중요: ENEMY_TYPES의 색상과 능력치는 실제 원본 기획에 확정된 값이 아니라 임시값이야. 몹의 외형을 확정하면 이 파일만 수정해 실제 디자인에 맞출 수 있어.