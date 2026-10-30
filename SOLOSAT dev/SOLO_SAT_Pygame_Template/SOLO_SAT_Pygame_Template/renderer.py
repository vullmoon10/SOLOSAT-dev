# renderer.py
# 배경과 지형, 몹, 플레이어, HUD, 문제 창을 그려.

import pygame

from settings import *


class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_text(self, text, x, y, color=DARK, font=FONT):
        image = font.render(str(text), True, color)
        self.screen.blit(image, (x, y))

    def draw_background(self, camera_x):
        self.screen.fill(SKY)

        # 산
        for i in range(-1, 7):
            x = i * 260 - int(camera_x * 0.18) % 260
            pygame.draw.polygon(
                self.screen,
                MOUNTAIN,
                [
                    (x, 520),
                    (x + 125, 360 + (i % 3) * 30),
                    (x + 260, 520),
                ],
            )

        # 구름
        for i in range(6):
            x = (
                i * 210 - int(camera_x * 0.3)
            ) % (WIDTH + 180) - 80
            y = 90 + (i % 3) * 55

            pygame.draw.circle(self.screen, WHITE, (x, y), 17)
            pygame.draw.circle(
                self.screen, WHITE, (x + 20, y - 8), 20
            )
            pygame.draw.circle(
                self.screen, WHITE, (x + 40, y), 15
            )

    def draw_world(self, world, camera_x):
        # 지면
        for segment in world.ground_segments:
            rect = segment.move(-camera_x, 0)

            if rect.right < 0 or rect.left > WIDTH:
                continue

            pygame.draw.rect(self.screen, DIRT, rect)
            pygame.draw.rect(
                self.screen, GRASS,
                (rect.x, rect.y, rect.width, 7),
            )

        # 발판
        for platform in world.platforms:
            rect = platform.move(-camera_x, 0)

            if rect.right < 0 or rect.left > WIDTH:
                continue

            pygame.draw.rect(
                self.screen, PLATFORM_COLOR, rect
            )
            pygame.draw.rect(
                self.screen, GRASS,
                (rect.x, rect.y, rect.width, 4),
            )

        # 사다리
        for ladder in world.ladders:
            rect = ladder.move(-camera_x, 0)

            if rect.right < 0 or rect.left > WIDTH:
                continue

            pygame.draw.line(
                self.screen, (180, 100, 55),
                rect.topleft, (rect.left, rect.bottom), 3
            )
            pygame.draw.line(
                self.screen, (180, 100, 55),
                (rect.right, rect.top),
                (rect.right, rect.bottom), 3
            )

            for y in range(rect.top + 8, rect.bottom, 13):
                pygame.draw.line(
                    self.screen, (180, 100, 55),
                    (rect.left, y), (rect.right, y), 3
                )

        # 장식 상자
        for item in world.decorations:
            rect = item.move(-camera_x, 0)

            if rect.right < 0 or rect.left > WIDTH:
                continue

            pygame.draw.rect(self.screen, DIRT, rect)
            pygame.draw.rect(
                self.screen, (91, 57, 36), rect, 2
            )

        # 가시
        for spike in world.spikes:
            x = spike["x"] - camera_x
            y = spike["y"]

            for i in range(spike["count"]):
                sx = x + i * 13
                pygame.draw.polygon(
                    self.screen, (220, 45, 65),
                    [
                        (sx, y),
                        (sx + 7, y - 15),
                        (sx + 13, y),
                    ],
                )

        # 몹
        for enemy in world.enemies:
            if not enemy.active:
                continue

            rect = enemy.rect.move(-camera_x, 0)

            if rect.right < 0 or rect.left > WIDTH:
                continue

            pygame.draw.rect(
                self.screen,
                enemy.data["color"],
                rect,
                border_radius=4,
            )

            # 눈
            eye_y = rect.y + rect.height // 3
            pygame.draw.circle(
                self.screen, WHITE,
                (rect.x + rect.width // 3, eye_y), 4
            )
            pygame.draw.circle(
                self.screen, WHITE,
                (rect.x + 2 * rect.width // 3, eye_y), 4
            )

    def draw_player(self, player, camera_x):
        rect = player.rect.move(-camera_x, 0)

        pygame.draw.rect(
            self.screen, BLUE, rect, border_radius=3
        )
        pygame.draw.rect(
            self.screen, (40, 45, 150),
            rect, 2, border_radius=3
        )

    def draw_hud(self, hp, score, message):
        pygame.draw.rect(
            self.screen, (75, 65, 65),
            (15, 14, 170, 14)
        )
        pygame.draw.rect(
            self.screen, RED,
            (15, 14, int(170 * max(0, hp) / MAX_HP), 14)
        )

        self.draw_text(f"HP {hp}", 15, 32, DARK, SMALL)
        self.draw_text(f"SCORE {score}", 15, 52, DARK, SMALL)
        self.draw_text(
            "A/D 이동  SPACE 점프  W/S 사다리",
            15, HEIGHT - 25, DARK, SMALL
        )

        if message:
            self.draw_text(message, 250, 25, DARK, SMALL)

    def draw_quiz(self, quiz):
        if not quiz.active:
            return

        question = quiz.enemy.question
        remaining = quiz.remaining()

        overlay = pygame.Surface(
            (WIDTH, HEIGHT), pygame.SRCALPHA
        )
        overlay.fill((20, 30, 45, 145))
        self.screen.blit(overlay, (0, 0))

        panel = pygame.Rect(190, 125, 620, 365)
        pygame.draw.rect(
            self.screen, CREAM, panel, border_radius=8
        )

        self.draw_text(
            question["subject"], 210, 142, GRASS, SMALL
        )
        self.draw_text(
            "문제 풀이", 285, 142, DARK, SMALL
        )
        self.draw_text(
            f"{remaining:.1f}s", 740, 142,
            RED if remaining < 10 else DARK, SMALL
        )

        bar = pygame.Rect(205, 175, 590, 7)
        pygame.draw.rect(self.screen, GRAY, bar)

        ratio = remaining / max(1, quiz.duration)
        pygame.draw.rect(
            self.screen,
            GRASS if ratio > 0.3 else (220, 130, 50),
            (bar.x, bar.y, int(bar.width * ratio), bar.height)
        )

        self.draw_text(question["q"], 210, 205, DARK, SMALL)

        for i, choice in enumerate(question["choices"]):
            option = pygame.Rect(205, 245 + i * 48, 590, 39)
            selected = i == quiz.selected

            color = (190, 220, 255) if selected else GRAY
            pygame.draw.rect(
                self.screen, color, option, border_radius=5
            )

            if selected:
                pygame.draw.rect(
                    self.screen, (55, 110, 220),
                    option, 2, border_radius=5
                )

            self.draw_text(
                f"{i + 1}. {choice}",
                220, option.y + 8, DARK, SMALL
            )

        self.draw_text(
            "↑/↓ 선택 · Enter 제출 · 마우스 클릭",
            210, 450, DARK, SMALL
        )