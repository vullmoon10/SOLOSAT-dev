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


# 클래스 기능
class Game:  # ?? ??? ?? ??
    # 함수 기능
    def __init__(self, screen):  # ?? ?? ?? ??
        self.screen = screen  # 변수 기능
        self.renderer = Renderer(screen)  # 변수 기능
        self.state = TITLE  # 변수 기능
        self.question_manager = QuestionManager(QUESTIONS)  # 변수 기능
        self.save_manager = SaveManager()  # 변수 기능
        self.player = Player()  # 변수 기능
        self.battle_manager = BattleManager(self.player)  # 변수 기능
        self.enemies = []  # 변수 기능
        self.current_enemy = None  # 변수 기능
        self.current_question = None  # 변수 기능
        self.camera_x = 0  # 변수 기능
        self.difficulty = "以?  # ?? ???
        self.speedrun = False  # 변수 기능
        self.create_stage()

    # 함수 기능
    def create_stage(self):  # ?? ??? ?? ? ??
        self.enemies.clear()
        positions = [900, 1600, 2400, 3200, 4100]  # 변수 기능
        for x, question in zip(positions, self.question_manager.questions):
            self.enemies.append(FormulaEnemy(x, question))

    # 함수 기능
    def handle_event(self, event):  # ?? ??? ?? ?? ??
        # 조건 분기
        if event.type != pygame.KEYDOWN:  # ? ?? ???? ??
            return

        # 조건 분기
        if self.state == TITLE:  # ??? ?? ?? ??
            # 조건 분기
            if event.key == pygame.K_1:  # ? ?? ?? ??
                self.state = NEW_GAME  # 변수 기능
            # 조건 분기
            elif event.key == pygame.K_2:  # ?? ?? ???? ??
                self.load_game()
            # 조건 분기
            elif event.key == pygame.K_3:  # ??? ?? ??
                self.state = CREDITS  # 변수 기능
        # 조건 분기
        elif self.state == NEW_GAME:  # ? ?? ?? ?? ??
            # 조건 분기
            if event.key == pygame.K_RETURN:  # Enter ? ?? ??
                self.start_game()
            # 조건 분기
            elif event.key == pygame.K_LEFT:  # ??? ?? ?? ??
                self.change_difficulty(-1)
            # 조건 분기
            elif event.key == pygame.K_RIGHT:  # ??? ?? ?? ??
                self.change_difficulty(1)
            # 조건 분기
            elif event.key == pygame.K_s:  # ???? ?? ??
                self.speedrun = not self.speedrun  # 변수 기능
            # 조건 분기
            elif event.key == pygame.K_ESCAPE:  # Escape ? ?? ??
                self.state = TITLE  # 변수 기능
        # 조건 분기
        elif self.state == PLAY:  # ??? ?? ?? ??
            # 조건 분기
            if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):  # ??? ?? ?? ?? ??
                self.player.jump()
            # 조건 분기
            elif event.key == pygame.K_ESCAPE:  # Escape ? ?? ??
                self.save_game()
                self.state = TITLE  # 변수 기능
        # 조건 분기
        elif self.state == QUESTION:  # ?? ?? ?? ??
            key_map = {  # 변수 기능
                pygame.K_1: 1,
                pygame.K_2: 2,
                pygame.K_3: 3,
                pygame.K_4: 4,
                pygame.K_5: 5,
            }
            # 조건 분기
            if event.key in key_map:  # ? ?? ? ?? ??
                self.submit_answer(key_map[event.key])
        # 조건 분기
        elif self.state == RESULT:  # ?? ?? ?? ??
            # 조건 분기
            if event.key == pygame.K_RETURN:  # Enter ? ?? ??
                self.state = TITLE  # 변수 기능
        # 조건 분기
        elif self.state == CREDITS:  # ??? ?? ?? ??
            # 조건 분기
            if event.key == pygame.K_ESCAPE:  # Escape ? ?? ??
                self.state = TITLE  # 변수 기능

    # 함수 기능
    def change_difficulty(self, direction):  # ?? ??? ??
        difficulties = ["??, "以?, "??, "理쒖긽"]  # ??? ??
        index = (difficulties.index(self.difficulty) + direction) % len(difficulties)  # 변수 기능
        self.difficulty = difficulties[index]  # 변수 기능

    # 함수 기능
    def start_game(self):  # ? ?? ???
        self.player = Player("SOLO")  # 변수 기능
        self.battle_manager = BattleManager(self.player)  # 변수 기능
        self.camera_x = 0  # 변수 기능
        self.current_enemy = None  # 변수 기능
        self.current_question = None  # 변수 기능
        self.create_stage()
        self.state = PLAY  # 변수 기능

    # 함수 기능
    def save_game(self):  # ?? ?? ?? ??
        self.save_manager.save(self.player, self.difficulty, self.speedrun)

    # 함수 기능
    def load_game(self):  # ??? ?? ?? ????
        self.player = Player()  # 변수 기능
        result = self.save_manager.load(self.player)  # 변수 기능
        # 조건 분기
        if result is None:  # ?? ??? ?? ?? ??
            self.state = NEW_GAME  # 변수 기능
            return
        self.difficulty = result["difficulty"]  # 변수 기능
        self.speedrun = result["speedrun"]  # 변수 기능
        self.battle_manager = BattleManager(self.player)  # 변수 기능
        self.create_stage()
        self.state = PLAY  # 변수 기능

    # 함수 기능
    def update(self, dt):  # ????? ? ?? ??
        # 조건 분기
        if self.state != PLAY:  # ??? ?? ??? ?? ??
            return

        self.player.update()
        for enemy in self.enemies:
            # 조건 분기
            if not enemy.active:  # ??? ? ?? ??
                continue
            enemy.update(self.player.x)
            # 조건 분기
            if self.player.rect.colliderect(enemy.rect):  # ????? ? ?? ??
                self.current_enemy = enemy  # 변수 기능
                self.current_question = enemy.question  # 변수 기능
                self.state = QUESTION  # 변수 기능
                break

        self.camera_x = self.player.x - SCREEN_WIDTH // 2  # 변수 기능
        self.camera_x = max(0, min(WORLD_WIDTH - SCREEN_WIDTH, self.camera_x))  # 변수 기능

    # 함수 기능
    def submit_answer(self, selected_answer):  # ?? ??? ?? ?? ??
        result = self.battle_manager.answer(self.current_question, selected_answer)  # 변수 기능
        # 조건 분기
        if result["correct"]:  # ??? ? ? ??
            self.current_enemy.active = False

        self.current_enemy = None  # 변수 기능
        self.current_question = None  # 변수 기능

        # 조건 분기
        if not any(enemy.active for enemy in self.enemies):  # ?? ? ?? ?? ??
            self.state = RESULT  # 변수 기능
        else:  # ? ??? ??? ? ??
            self.state = PLAY  # 변수 기능

    # 함수 기능
    def draw(self):  # ?? ?? ?? ??
        # 조건 분기
        if self.state == TITLE:  # ??? ?? ?? ??
            self.renderer.draw_title()
        # 조건 분기
        elif self.state == NEW_GAME:  # ? ?? ?? ?? ??
            self.renderer.draw_new_game(self.difficulty, self.speedrun)
        # 조건 분기
        elif self.state == PLAY:  # ??? ?? ?? ??
            self.draw_game()
        # 조건 분기
        elif self.state == QUESTION:  # ?? ?? ?? ??
            self.draw_game()
            self.renderer.draw_question(self.current_question)
        # 조건 분기
        elif self.state == RESULT:  # ?? ?? ?? ??
            self.renderer.draw_result(self.player, self.battle_manager.get_accuracy())
        # 조건 분기
        elif self.state == CREDITS:  # ??? ?? ?? ??
            self.renderer.draw_credits()

    # 함수 기능
    def draw_game(self):  # ???? ?? ??
        self.screen.fill((25, 25, 35))
        self.renderer.draw_ground(self.camera_x)
        self.renderer.draw_player(self.player, self.camera_x)
        for enemy in self.enemies:
            # 조건 분기
            if enemy.active:  # ?? ?? ??? ??
                self.renderer.draw_enemy(enemy, self.camera_x)
        self.renderer.draw_hud(self.player)
        self.renderer.text(
            "?????대룞 / SPACE ?먰봽 / ESC ???,
            20,
            SCREEN_HEIGHT - 35,
            self.renderer.small_font,
        )
