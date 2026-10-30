# player.py
# 플레이어의 이동과 물리를 담당해. 카메라가 움직여도 플레이어의 월드 좌표는 유지하도록 구성했어.

import pygame
from settings import (
    MOVE_SPEED, GRAVITY, JUMP_POWER,
    MAX_FALL_SPEED, HEIGHT
)


class Player:
    def __init__(self, x=60, y=450):
        self.rect = pygame.Rect(x, y, 22, 30)
        self.vy = 0.0
        self.on_ground = False
        self.climbing = False

    def update(self, keys, world):
        dx = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= MOVE_SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += MOVE_SPEED

        self.rect.x += dx

        # 사다리 이동
        self.climbing = False

        for ladder in world.ladders:
            if self.rect.colliderect(ladder):
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    self.rect.y -= MOVE_SPEED
                    self.climbing = True
                elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    self.rect.y += MOVE_SPEED
                    self.climbing = True

                if self.climbing:
                    self.vy = 0
                    break

        previous_bottom = self.rect.bottom

        if not self.climbing:
            self.vy = min(
                self.vy + GRAVITY,
                MAX_FALL_SPEED
            )
            self.rect.y += int(self.vy)

        self.on_ground = False

        # 지면 및 발판 착지
        if not self.climbing and self.vy >= 0:
            surfaces = (
                world.ground_segments
                + world.platforms
            )

            for surface in surfaces:
                horizontal_overlap = (
                    self.rect.right > surface.left
                    and self.rect.left < surface.right
                )

                crossed_top = (
                    previous_bottom <= surface.top
                    and self.rect.bottom >= surface.top
                )

                if horizontal_overlap and crossed_top:
                    self.rect.bottom = surface.top
                    self.vy = 0
                    self.on_ground = True
                    break

    def jump(self):
        if self.on_ground:
            self.vy = JUMP_POWER
            self.on_ground = False

    def reset_position(self):
        self.rect.x = 60
        self.rect.y = 400
        self.vy = 0
        
#[수정 가능] 이동 속도와 점프 높이는 우선 settings.py에서 조절해. 이 파일의 충돌 로직은 지형 구조를 바꿀 때 함께 검토해야 해.