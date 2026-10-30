# game.py
#이 파일이 각 시스템을 연결해. 플레이어 이동, 몹과의 접촉, 문제 입력, 카메라 이동, HP와 점수 관리를 여기서 처리해.

import pygame

from settings import WIDTH, HEIGHT, MAX_HP
from player import Player
from world import World
from quiz import Quiz
from renderer import Renderer


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.world = World()
        self.quiz = Quiz()
        self.renderer = Renderer(screen)

        self.camera_x = 0
        self.score = 0
        self.hp = MAX_HP
        self.message = ""
        self.message_until = 0
        self.running = True
        self.game_over = False

    def show_message(self, text, duration=2000):
        self.message = text
        self.message_until = (
            pygame.time.get_ticks() + duration
        )

    def apply_quiz_result(self, result):
        if result is None:
            return

        self.score += result["score"]
        self.hp = max(0, self.hp - result["damage"])
        self.show_message(result["message"])

        if self.hp <= 0:
            self.game_over = True

    def open_nearby_enemy(self):
        nearby = self.player.rect.inflate(60, 45)

        for enemy in self.world.enemies:
            if enemy.active and nearby.colliderect(enemy.rect):
                self.quiz.open(enemy)
                return

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return

        if self.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            return

        if self.quiz.active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quiz.enemy = None

                elif event.key in (
                    pygame.K_UP, pygame.K_w
                ):
                    self.quiz.selected = (
                        self.quiz.selected - 1
                    ) % 4

                elif event.key in (
                    pygame.K_DOWN, pygame.K_s
                ):
                    self.quiz.selected = (
                        self.quiz.selected + 1
                    ) % 4

                elif event.key in (
                    pygame.K_RETURN, pygame.K_SPACE
                ):
                    result = self.quiz.submit(
                        self.quiz.selected
                    )
                    self.apply_quiz_result(result)

                elif event.key in (
                    pygame.K_1, pygame.K_2,
                    pygame.K_3, pygame.K_4
                ):
                    result = self.quiz.submit(
                        event.key - pygame.K_1
                    )
                    self.apply_quiz_result(result)

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
            ):
                for i in range(4):
                    option = pygame.Rect(
                        205, 245 + i * 48, 590, 39
                    )

                    if option.collidepoint(event.pos):
                        result = self.quiz.submit(i)
                        self.apply_quiz_result(result)
                        break

            return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

            elif event.key == pygame.K_SPACE:
                self.player.jump()

            elif event.key == pygame.K_e:
                self.open_nearby_enemy()

    def update(self):
        if self.game_over or self.quiz.active:
            return

        keys = pygame.key.get_pressed()
        self.player.update(keys, self.world)

        # 가시 충돌
        for spike in self.world.spikes:
            spike_rect = pygame.Rect(
                spike["x"],
                spike["y"] - 14,
                spike["count"] * 13,
                14,
            )

            if self.player.rect.colliderect(spike_rect):
                self.hp = max(0, self.hp - 1)
                self.player.rect.bottom = min(
                    self.player.rect.bottom, 500
                )
                self.player.vy = -4

        # 카메라: 플레이어가 화면 중앙보다 오른쪽으로 가면 이동
        target_x = max(0, self.player.rect.x - int(WIDTH * 0.55))
        self.camera_x = max(self.camera_x, target_x)

        # 오른쪽 지형을 계속 생성
        self.world.update_generation(self.player.rect.x)

        # 몹과 접촉하면 문제 시작
        for enemy in self.world.enemies:
            if (
                enemy.active
                and self.player.rect.colliderect(enemy.rect)
            ):
                self.quiz.open(enemy)
                break

        # 추락
        if self.player.rect.top > HEIGHT:
            self.player.reset_position()
            self.hp = max(0, self.hp - 10)

        if self.hp <= 0:
            self.game_over = True

    def update_quiz(self):
        result = self.quiz.check_timeout()
        self.apply_quiz_result(result)

    def draw(self):
        self.renderer.draw_background(self.camera_x)
        self.renderer.draw_world(
            self.world, self.camera_x
        )
        self.renderer.draw_player(
            self.player, self.camera_x
        )

        message = (
            self.message
            if pygame.time.get_ticks() < self.message_until
            else ""
        )

        self.renderer.draw_hud(
            self.hp, self.score, message
        )
        self.renderer.draw_quiz(self.quiz)

        if self.game_over:
            overlay = pygame.Surface(
                (WIDTH, HEIGHT), pygame.SRCALPHA
            )
            overlay.fill((0, 0, 0, 190))
            self.screen.blit(overlay, (0, 0))

            text = self.renderer.draw_text
            text("GAME OVER", 390, 240, (255, 255, 255))
            text(
                f"최종 점수: {self.score}",
                390, 290, (255, 255, 255)
            )
            text(
                "ESC를 눌러 종료",
                390, 340, (255, 255, 255), 
            )

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                self.handle_event(event)

            self.update()
            self.update_quiz()
            self.draw()

            pygame.display.flip()