# world.py
 #지형, 발판, 사다리, 가시와 장식용 상자를 생성해. 월드 좌표를 유지하므로 카메라가 움직일 때 지형 좌표를 일일이 이동시키지 않아도 돼.
 

import random
import pygame

from settings import WIDTH, HEIGHT, GROUND_Y


class World:
    def __init__(self):
        self.platforms = []
        self.ground_segments = []
        self.spikes = []
        self.ladders = []
        self.decorations = []
        self.enemies = []

        self.world_end = 0
        self.generate_chunk(0, 12)

    def generate_chunk(self, start_x, count=5):
        x = start_x

        for _ in range(count):
            width = random.randint(190, 290)

            self.ground_segments.append(
                pygame.Rect(
                    x, GROUND_Y,
                    width, HEIGHT - GROUND_Y
                )
            )

            # 장식용 상자
            if random.random() < 0.45:
                box_w = random.choice([28, 36, 48])
                box_h = random.choice([35, 50, 65])
                box_x = x + random.randint(
                    40, max(41, width - box_w)
                )

                self.decorations.append(
                    pygame.Rect(
                        box_x,
                        GROUND_Y - box_h,
                        box_w,
                        box_h
                    )
                )

            # 가시
            if random.random() < 0.35:
                self.spikes.append({
                    "x": x + random.randint(
                        40, max(41, width - 70)
                    ),
                    "y": GROUND_Y,
                    "count": random.randint(3, 5),
                })

            # 공중 발판
            if random.random() < 0.9:
                px = x + random.randint(
                    20, max(21, width - 130)
                )
                py = random.randint(350, 455)
                pw = random.randint(100, 170)

                self.platforms.append(
                    pygame.Rect(px, py, pw, 12)
                )

                # 사다리
                if random.random() < 0.7:
                    self.ladders.append(
                        pygame.Rect(
                            px + pw // 2,
                            py,
                            22,
                            GROUND_Y - py
                        )
                    )

                # 발판 위 몬스터
                if random.random() < 0.6:
                    self.add_enemy(
                        px + random.randint(
                            15, max(16, pw - 35)
                        ),
                        py
                    )

            # 지상 몬스터
            if random.random() < 0.4:
                self.add_enemy(
                    x + random.randint(
                        40, max(41, width - 35)
                    ),
                    GROUND_Y
                )

            x += width

        self.world_end = x

    def add_enemy(self, x, ground_y):
        # 실제 몬스터 생성은 enemies.py에서 담당
        from enemies import Enemy
        self.enemies.append(Enemy(x, ground_y))

    def update_generation(self, player_x):
        # 월드 끝이 플레이어보다 충분히 앞에 있도록 유지
        if self.world_end < player_x + WIDTH + 700:
            self.generate_chunk(
                self.world_end + random.randint(20, 60),
                5
            )

        # 플레이어 뒤의 오래된 오브젝트 정리
        cutoff = player_x - WIDTH - 300

        self.platforms = [
            obj for obj in self.platforms
            if obj.right > cutoff
        ]
        self.ground_segments = [
            obj for obj in self.ground_segments
            if obj.right > cutoff
        ]
        self.ladders = [
            obj for obj in self.ladders
            if obj.right > cutoff
        ]
        self.spikes = [
            obj for obj in self.spikes
            if obj["x"] + obj["count"] * 13 > cutoff
        ]
        self.decorations = [
            obj for obj in self.decorations
            if obj.right > cutoff
        ]
        self.enemies = [
            obj for obj in self.enemies
            if obj.rect.right > cutoff
        ]
        
#[수정 가능] random.random() < 0.9 같은 값은 발판 생성 확률이야. 0.9를 0.6으로 바꾸면 발판이 덜 생성돼.

#주의할 점은 현재 발판과 지면이 서로 떨어질 수 있다는 거야. 실제 플레이 테스트 후 지형 사이의 간격과 착지 가능성을 조정해야 해.