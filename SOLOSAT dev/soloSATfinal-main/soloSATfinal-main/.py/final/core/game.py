import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH
from core.game_state import TITLE, NEW_GAME, PLAY, QUESTION, RESULT, CREDITS
from data.questions import QUESTIONS
from entities.player import Player
from entities.enemy import FormulaEnemy
from systems.question_manager import QuestionManager
from systems.battle_manager import BattleManager
from systems.save_manager import SaveManager
from ui.renderer import Renderer


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.renderer = Renderer(screen)
        self.state = TITLE
        self.question_manager = QuestionManager(QUESTIONS)
        self.save_manager = SaveManager()
        self.player = Player()
        self.battle_manager = BattleManager(self.player)
        self.enemies = []
        self.current_enemy = None
        self.current_question = None
        self.camera_x = 0
        self.difficulty = "중"
        self.speedrun = False
        self.create_stage()

    def create_stage(self):
        self.enemies.clear()
        positions = [900, 1600, 2400, 3200, 4100]
        for x, question in zip(positions, self.question_manager.questions):
            self.enemies.append(FormulaEnemy(x, question))

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if self.state == TITLE:
            if event.key == pygame.K_1:
                self.state = NEW_GAME
            elif event.key == pygame.K_2:
                self.load_game()
            elif event.key == pygame.K_3:
                self.state = CREDITS
        elif self.state == NEW_GAME:
            if event.key == pygame.K_RETURN:
                self.start_game()
            elif event.key == pygame.K_LEFT:
                self.change_difficulty(-1)
            elif event.key == pygame.K_RIGHT:
                self.change_difficulty(1)
            elif event.key == pygame.K_s:
                self.speedrun = not self.speedrun
            elif event.key == pygame.K_ESCAPE:
                self.state = TITLE
        elif self.state == PLAY:
            if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                self.player.jump()
            elif event.key == pygame.K_ESCAPE:
                self.save_game()
                self.state = TITLE
        elif self.state == QUESTION:
            key_map = {
                pygame.K_1: 1,
                pygame.K_2: 2,
                pygame.K_3: 3,
                pygame.K_4: 4,
                pygame.K_5: 5,
            }
            if event.key in key_map:
                self.submit_answer(key_map[event.key])
        elif self.state == RESULT:
            if event.key == pygame.K_RETURN:
                self.state = TITLE
        elif self.state == CREDITS:
            if event.key == pygame.K_ESCAPE:
                self.state = TITLE

    def change_difficulty(self, direction):
        difficulties = ["하", "중", "상", "최상"]
        index = (difficulties.index(self.difficulty) + direction) % len(difficulties)
        self.difficulty = difficulties[index]

    def start_game(self):
        self.player = Player("SOLO")
        self.battle_manager = BattleManager(self.player)
        self.camera_x = 0
        self.current_enemy = None
        self.current_question = None
        self.create_stage()
        self.state = PLAY

    def save_game(self):
        self.save_manager.save(self.player, self.difficulty, self.speedrun)

    def load_game(self):
        self.player = Player()
        result = self.save_manager.load(self.player)
        if result is None:
            self.state = NEW_GAME
            return
        self.difficulty = result["difficulty"]
        self.speedrun = result["speedrun"]
        self.battle_manager = BattleManager(self.player)
        self.create_stage()
        self.state = PLAY

    def update(self, dt):
        if self.state != PLAY:
            return

        self.player.update()
        for enemy in self.enemies:
            if not enemy.active:
                continue
            enemy.update(self.player.x)
            if self.player.rect.colliderect(enemy.rect):
                self.current_enemy = enemy
                self.current_question = enemy.question
                self.state = QUESTION
                break

        self.camera_x = self.player.x - SCREEN_WIDTH // 2
        self.camera_x = max(0, min(WORLD_WIDTH - SCREEN_WIDTH, self.camera_x))

    def submit_answer(self, selected_answer):
        result = self.battle_manager.answer(self.current_question, selected_answer)
        if result["correct"]:
            self.current_enemy.active = False

        self.current_enemy = None
        self.current_question = None

        if not any(enemy.active for enemy in self.enemies):
            self.state = RESULT
        else:
            self.state = PLAY

    def draw(self):
        if self.state == TITLE:
            self.renderer.draw_title()
        elif self.state == NEW_GAME:
            self.renderer.draw_new_game(self.difficulty, self.speedrun)
        elif self.state == PLAY:
            self.draw_game()
        elif self.state == QUESTION:
            self.draw_game()
            self.renderer.draw_question(self.current_question)
        elif self.state == RESULT:
            self.renderer.draw_result(self.player, self.battle_manager.get_accuracy())
        elif self.state == CREDITS:
            self.renderer.draw_credits()

    def draw_game(self):
        self.screen.fill((25, 25, 35))
        self.renderer.draw_ground(self.camera_x)
        self.renderer.draw_player(self.player, self.camera_x)
        for enemy in self.enemies:
            if enemy.active:
                self.renderer.draw_enemy(enemy, self.camera_x)
        self.renderer.draw_hud(self.player)
        self.renderer.text(
            "← → 이동 / SPACE 점프 / ESC 저장",
            20,
            SCREEN_HEIGHT - 35,
            self.renderer.small_font,
        )
