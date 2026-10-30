import pygame

from config import FONT_PATH, SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_Y


# 클래스 기능
class Renderer:  # ?? ?? ???
    # 함수 기능
    def __init__(self, screen):  # ?? ?? ?? ??
        self.screen = screen  # 변수 기능
        self.font = pygame.font.Font(FONT_PATH, 28)  # 변수 기능
        self.small_font = pygame.font.Font(FONT_PATH, 20)  # 변수 기능
        self.big_font = pygame.font.Font(FONT_PATH, 50)  # 변수 기능
        self.title_font = pygame.font.Font(FONT_PATH, 72)  # 변수 기능

    # 함수 기능
    def text(self, text, x, y, font=None, color=(255, 255, 255)):  # ?? ??? ??? ??
        font = font or self.font  # 변수 기능
        self.screen.blit(font.render(str(text), True, color), (x, y))

    # 함수 기능
    def center(self, text, y, font=None, color=(255, 255, 255)):  # ??? ?? ??? ??
        font = font or self.font  # 변수 기능
        surface = font.render(str(text), True, color)  # 변수 기능
        self.screen.blit(surface, ((SCREEN_WIDTH - surface.get_width()) // 2, y))

    # 함수 기능
    def draw_ground(self, camera_x):  # ?? ???
        pygame.draw.rect(
            self.screen,
            (70, 70, 70),
            (-camera_x, GROUND_Y, SCREEN_WIDTH + camera_x, SCREEN_HEIGHT - GROUND_Y),
        )

    # 함수 기능
    def draw_player(self, player, camera_x):  # ???? ???
        rect = player.rect.copy()  # 변수 기능
        rect.x -= camera_x
        pygame.draw.rect(self.screen, (70, 130, 255), rect)

    # 함수 기능
    def draw_enemy(self, enemy, camera_x):  # ?? ?? ???
        rect = enemy.rect.copy()  # 변수 기능
        rect.x -= camera_x
        pygame.draw.rect(self.screen, (210, 70, 70), rect)
        self.text(enemy.question.get("formula", ""), rect.x + 10, rect.y + 20, self.small_font)

    # 함수 기능
    def draw_hud(self, player):  # ???? ?? ??
        self.text(player.nickname, 20, 20)
        self.text(f"LV.{player.level}", 20, 55)
        self.text(f"EXP {player.exp}/{player.max_exp}", 20, 90)
        self.text(f"SCORE {player.score}", 20, 125)
        self.text(f"HP {player.hp}/{player.max_hp}", 20, 160)

    # 함수 기능
    def draw_question(self, question):  # ??? ??? ??
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)  # 변수 기능
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        panel = pygame.Rect(120, 90, 1040, 540)  # 변수 기능
        pygame.draw.rect(self.screen, (30, 30, 40), panel)

        self.text(f"{question['subject']} 쨌 {question['category']}", 160, 120, self.small_font)
        self.text(question["question"], 160, 160, self.big_font)

        for index, choice in enumerate(question["choices"], start=1):
            self.text(f"{index}. {choice}", 180, 255 + (index - 1) * 55)

        self.text("1~5 : ???좏깮", 180, 550, self.small_font)

    # 함수 기능
    def draw_title(self):  # ??? ?? ??
        self.screen.fill((20, 20, 30))
        self.center("SOLO SAT", 100, self.title_font)
        self.center("???쇱옄留?1?깃툒", 195, self.big_font)
        self.center("1. ??寃뚯엫", 330)
        self.center("2. 遺덈윭?ㅺ린", 380)
        self.center("3. ?щ젅??, 430)
        self.center("踰덊샇瑜??뚮윭 ?좏깮", 560, self.small_font)

    # 함수 기능
    def draw_new_game(self, difficulty, speedrun):  # ? ?? ?? ??
        self.screen.fill((20, 20, 30))
        self.center("??寃뚯엫", 100, self.title_font)
        self.center("?됰꽕??: SOLO", 250)
        self.center(f"?쒖씠??: {difficulty}", 310)
        self.center(f"?ㅽ뵾?쒕윴 : {'ON' if speedrun else 'OFF'}", 360)
        self.center("?????쒖씠??/ S ?ㅽ뵾?쒕윴", 420, self.small_font)
        self.center("ENTER : ?쒖옉", 470)
        self.center("ESC : ?ㅻ줈", 520, self.small_font)

    # 함수 기능
    def draw_result(self, player, accuracy):  # ?? ?? ??
        self.screen.fill((20, 20, 30))
        self.center("RESULT", 80, self.title_font)
        self.center(player.nickname, 190)
        self.center(f"LEVEL {player.level}", 240)
        self.center(f"SCORE {player.score}", 290)
        self.center(f"?뺣떟 {player.correct}", 340)
        self.center(f"?ㅻ떟 {player.wrong}", 390)
        self.center(f"?뺣떟瑜?{accuracy:.1f}%", 440)
        self.center("ENTER : ??댄?", 550, self.small_font)

    # 함수 기능
    def draw_credits(self):  # ??? ?? ??
        self.screen.fill((20, 20, 30))
        self.center("SOLO SAT", 130, self.title_font)
        self.center("2026 VIAUS PROJECT", 250)
        self.center("SOLO SAT ?????쇱옄留?1?깃툒", 320)
        self.center("ESC : ?ㅻ줈", 520, self.small_font)
