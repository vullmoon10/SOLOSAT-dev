import pygame
import random
import json
import os

# =========================================================
# SOLO SAT — 나 혼자만 1등급
# Python / Pygame Prototype
# =========================================================

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SOLO SAT — 나 혼자만 1등급")

clock = pygame.time.Clock()

# ---------------------------------------------------------
# Font
# ---------------------------------------------------------

FONT_PATH = "C:/Windows/Fonts/malgun.ttf"

font = pygame.font.Font(FONT_PATH, 28)
small_font = pygame.font.Font(FONT_PATH, 22)
big_font = pygame.font.Font(FONT_PATH, 48)
title_font = pygame.font.Font(FONT_PATH, 72)


# =========================================================
# COLORS
# =========================================================

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GRAY = (120, 120, 120)
LIGHT_GRAY = (220, 220, 220)

BLUE = (70, 120, 220)
GREEN = (70, 180, 100)
RED = (210, 70, 70)
YELLOW = (220, 180, 60)


# =========================================================
# QUESTION DATA
# =========================================================
# 나중에는 이 부분을 JSON으로 분리하면 됨.
# 기획서의 QuestionData 구조를 유지한다.
#
# id
# subject
# category
# difficulty
# question
# choices
# answer
# explanation
# exp
# penalty
# formula
# =========================================================

questions = [
    {
        "id": 1,
        "subject": "수학",
        "category": "인수분해",
        "difficulty": "중하",
        "question": "x² + 5x + 6을 인수분해한 것은?",
        "choices": [
            "(x+1)(x+6)",
            "(x+2)(x+3)",
            "(x-2)(x-3)",
            "(x+2)(x-3)",
            "(x-2)(x+3)"
        ],
        "answer": 2,
        "explanation": "곱이 6이고 합이 5인 두 수는 2와 3이다.",
        "exp": 20,
        "penalty": 5,
        "formula": "x² + 5x + 6"
    },

    {
        "id": 2,
        "subject": "수학",
        "category": "인수분해",
        "difficulty": "중하",
        "question": "x² - 9를 인수분해한 것은?",
        "choices": [
            "(x-9)(x+1)",
            "(x-3)²",
            "(x-3)(x+3)",
            "(x+9)(x-1)",
            "(x+3)²"
        ],
        "answer": 3,
        "explanation": "x² - 3²은 두 제곱의 차이므로 (x-3)(x+3)이다.",
        "exp": 20,
        "penalty": 5,
        "formula": "x² - 9"
    },

    {
        "id": 3,
        "subject": "수학",
        "category": "인수분해",
        "difficulty": "중",
        "question": "x² + 7x + 12를 인수분해한 것은?",
        "choices": [
            "(x+2)(x+6)",
            "(x+3)(x+4)",
            "(x-3)(x-4)",
            "(x+1)(x+12)",
            "(x-2)(x-6)"
        ],
        "answer": 2,
        "explanation": "곱이 12이고 합이 7인 두 수는 3과 4이다.",
        "exp": 30,
        "penalty": 7,
        "formula": "x² + 7x + 12"
    },

    {
        "id": 4,
        "subject": "수학",
        "category": "인수분해",
        "difficulty": "중",
        "question": "x² - 6x + 8을 인수분해한 것은?",
        "choices": [
            "(x-2)(x-4)",
            "(x+2)(x+4)",
            "(x-1)(x-8)",
            "(x+1)(x-8)",
            "(x-3)(x-3)"
        ],
        "answer": 1,
        "explanation": "곱이 8이고 합이 -6이므로 -2와 -4를 사용한다.",
        "exp": 30,
        "penalty": 7,
        "formula": "x² - 6x + 8"
    },

    {
        "id": 5,
        "subject": "수학",
        "category": "인수분해",
        "difficulty": "중상",
        "question": "4x² - 25를 인수분해한 것은?",
        "choices": [
            "(2x-5)(2x+5)",
            "(4x-5)(x+5)",
            "(2x-25)(2x+1)",
            "(4x+5)(x-5)",
            "(x-5)(4x+5)"
        ],
        "answer": 1,
        "explanation": "4x² - 25 = (2x)² - 5²이므로 두 제곱의 차이를 이용한다.",
        "exp": 40,
        "penalty": 10,
        "formula": "4x² - 25"
    }
]


# =========================================================
# PLAYER DATA
# =========================================================

player = {
    "nickname": "PLAYER",
    "x": 300,
    "y": 500,

    "width": 45,
    "height": 65,

    "speed": 5,
    "velocity_y": 0,
    "jump_power": -14,

    "on_ground": False,

    "hp": 100,
    "max_hp": 100,

    "level": 1,
    "exp": 0,
    "max_exp": 100,

    "score": 0,

    "correct": 0,
    "wrong": 0,
    "solved": 0
}


# =========================================================
# WORLD
# =========================================================

WORLD_WIDTH = 5000
GROUND_Y = 620

camera_x = 0


# =========================================================
# GAME SETTINGS
# =========================================================

difficulty = "중"
speedrun = False

current_question = None
current_enemy = None

answer_result = None
answer_message = ""

question_start_time = 0


# =========================================================
# GAME STATES
# =========================================================

TITLE = "title"
NEW_GAME = "new_game"
PLAY = "play"
QUESTION = "question"
RESULT = "result"
CREDITS = "credits"

game_state = TITLE


# =========================================================
# ENEMIES
# =========================================================
# 문제 = 몹
#
# 수식 자체를 몹의 외형으로 사용한다.
# =========================================================

def create_enemies():

    selected = questions.copy()
    random.shuffle(selected)

    enemies = []

    positions = [
        1000,
        1600,
        2300,
        3100,
        4000
    ]

    for i, question in enumerate(selected):

        enemies.append({
            "x": positions[i],
            "y": GROUND_Y - 70,

            "width": 150,
            "height": 70,

            "speed": 1.2 + i * 0.15,

            "question": question,

            "active": True
        })

    return enemies


enemies = create_enemies()


# =========================================================
# DRAW TEXT
# =========================================================

def draw_text(text, x, y, selected_font=font, color=WHITE):

    surface = selected_font.render(str(text), True, color)
    screen.blit(surface, (x, y))


def draw_center(text, y, selected_font=font, color=WHITE):

    surface = selected_font.render(str(text), True, color)

    x = (SCREEN_WIDTH - surface.get_width()) // 2

    screen.blit(surface, (x, y))


# =========================================================
# PLAYER
# =========================================================

def reset_player():

    player["x"] = 300
    player["y"] = 500

    player["velocity_y"] = 0
    player["on_ground"] = False

    player["hp"] = player["max_hp"]

    player["level"] = 1
    player["exp"] = 0
    player["max_exp"] = 100

    player["score"] = 0

    player["correct"] = 0
    player["wrong"] = 0
    player["solved"] = 0


def update_player():

    keys = pygame.key.get_pressed()

    dx = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx -= player["speed"]

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx += player["speed"]

    player["x"] += dx

    player["x"] = max(
        0,
        min(WORLD_WIDTH - player["width"], player["x"])
    )

    # 점프
    if (
        (keys[pygame.K_SPACE] or keys[pygame.K_w])
        and player["on_ground"]
    ):
        player["velocity_y"] = player["jump_power"]
        player["on_ground"] = False

    # 중력
    player["velocity_y"] += 0.7
    player["y"] += player["velocity_y"]

    # 바닥 충돌
    if player["y"] + player["height"] >= GROUND_Y:

        player["y"] = GROUND_Y - player["height"]

        player["velocity_y"] = 0
        player["on_ground"] = True


def draw_player():

    rect = pygame.Rect(
        int(player["x"] - camera_x),
        int(player["y"]),
        player["width"],
        player["height"]
    )

    pygame.draw.rect(screen, BLUE, rect)

    draw_text(
        player["nickname"],
        rect.x - 5,
        rect.y - 30,
        small_font
    )


# =========================================================
# ENEMY AI
# =========================================================

def update_enemies():

    for enemy in enemies:

        if not enemy["active"]:
            continue

        distance = player["x"] - enemy["x"]

        # 플레이어 쪽으로 이동
        if abs(distance) > 80:

            if distance > 0:
                enemy["x"] += enemy["speed"]

            else:
                enemy["x"] -= enemy["speed"]


# =========================================================
# DRAW ENEMIES
# =========================================================

def draw_enemies():

    for enemy in enemies:

        if not enemy["active"]:
            continue

        x = int(enemy["x"] - camera_x)
        y = int(enemy["y"])

        rect = pygame.Rect(
            x,
            y,
            enemy["width"],
            enemy["height"]
        )

        pygame.draw.rect(
            screen,
            RED,
            rect,
            border_radius=10
        )

        formula = enemy["question"]["formula"]

        surface = big_font.render(
            formula,
            True,
            WHITE
        )

        formula_x = (
            rect.centerx -
            surface.get_width() // 2
        )

        formula_y = (
            rect.centery -
            surface.get_height() // 2
        )

        screen.blit(
            surface,
            (formula_x, formula_y)
        )


# =========================================================
# COLLISION
# =========================================================

def player_enemy_collision(enemy):

    player_rect = pygame.Rect(
        player["x"],
        player["y"],
        player["width"],
        player["height"]
    )

    enemy_rect = pygame.Rect(
        enemy["x"],
        enemy["y"],
        enemy["width"],
        enemy["height"]
    )

    return player_rect.colliderect(enemy_rect)


# =========================================================
# START QUESTION
# =========================================================

def start_question(enemy):

    global current_question
    global current_enemy
    global question_start_time
    global answer_result
    global game_state

    current_enemy = enemy
    current_question = enemy["question"]

    answer_result = None

    question_start_time = pygame.time.get_ticks()

    game_state = QUESTION


# =========================================================
# ANSWER
# =========================================================

def check_answer(answer):

    global answer_result
    global answer_message
    global game_state

    if current_question is None:
        return

    player["solved"] += 1

    if answer == current_question["answer"]:

        player["correct"] += 1

        player["score"] += 100

        player["exp"] += current_question["exp"]

        answer_result = True

        answer_message = (
            f"정답! +{current_question['exp']} EXP"
        )

        # 문제 몹 제거
        current_enemy["active"] = False

        # 레벨업
        while player["exp"] >= player["max_exp"]:

            player["exp"] -= player["max_exp"]

            player["level"] += 1

            player["max_exp"] = int(
                player["max_exp"] * 1.25
            )

    else:

        player["wrong"] += 1

        player["score"] = max(
            0,
            player["score"] - current_question["penalty"]
        )

        answer_result = False

        answer_message = (
            f"오답! -{current_question['penalty']} Score"
        )

    game_state = QUESTION


# =========================================================
# QUESTION SCREEN
# =========================================================

def draw_question():

    # 어두운 배경
    overlay = pygame.Surface(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    overlay.set_alpha(235)

    screen.blit(overlay, (0, 0))

    draw_center(
        "수학 영역",
        40,
        big_font
    )

    # 문제
    draw_text(
        current_question["question"],
        100,
        140,
        font
    )

    # 선택지
    for i, choice in enumerate(
        current_question["choices"]
    ):

        y = 220 + i * 65

        box = pygame.Rect(
            100,
            y,
            1080,
            50
        )

        pygame.draw.rect(
            screen,
            LIGHT_GRAY,
            box
        )

        draw_text(
            f"{i + 1}. {choice}",
            120,
            y + 10,
            font,
            BLACK
        )

    if answer_result is not None:

        if answer_result:

            draw_text(
                answer_message,
                100,
                570,
                font,
                GREEN
            )

        else:

            draw_text(
                answer_message,
                100,
                570,
                font,
                RED
            )

        draw_text(
            current_question["explanation"],
            100,
            615,
            small_font
        )

        draw_text(
            "ENTER → 계속",
            930,
            665,
            small_font
        )


# =========================================================
# HUD
# =========================================================

def draw_hud():

    # HP
    draw_text(
        f"HP {player['hp']} / {player['max_hp']}",
        20,
        20,
        small_font
    )

    # Level
    draw_text(
        f"Lv.{player['level']}",
        20,
        50,
        small_font
    )

    # EXP
    draw_text(
        f"EXP {player['exp']} / {player['max_exp']}",
        20,
        80,
        small_font
    )

    # Score
    draw_text(
        f"SCORE {player['score']}",
        20,
        110,
        small_font
    )

    # 수학 영역
    draw_text(
        "수학 영역 · 인수분해",
        900,
        20,
        small_font
    )


# =========================================================
# CAMERA
# =========================================================

def update_camera():

    global camera_x

    target = player["x"] - SCREEN_WIDTH * 0.35

    camera_x += (
        target - camera_x
    ) * 0.1

    camera_x = max(
        0,
        min(
            WORLD_WIDTH - SCREEN_WIDTH,
            camera_x
        )
    )


# =========================================================
# WORLD
# =========================================================

def draw_world():

    screen.fill((35, 35, 45))

    # 하늘 / 배경
    for x in range(
        -100,
        SCREEN_WIDTH + 200,
        200
    ):

        world_x = x + int(camera_x)

        pygame.draw.rect(
            screen,
            (45, 45, 60),
            (x, 300, 180, 200)
        )

    # 바닥
    pygame.draw.rect(
        screen,
        (70, 70, 80),
        (
            0,
            GROUND_Y,
            SCREEN_WIDTH,
            SCREEN_HEIGHT - GROUND_Y
        )
    )

    # 바닥 라인
    pygame.draw.line(
        screen,
        LIGHT_GRAY,
        (0, GROUND_Y),
        (SCREEN_WIDTH, GROUND_Y),
        3
    )


# =========================================================
# RESULT
# =========================================================

def draw_result():

    screen.fill(BLACK)

    draw_center(
        "RESULT",
        80,
        title_font
    )

    draw_center(
        f"PLAYER : {player['nickname']}",
        190
    )

    draw_center(
        f"LEVEL : {player['level']}",
        240
    )

    draw_center(
        f"SCORE : {player['score']}",
        290
    )

    draw_center(
        f"정답 : {player['correct']}",
        350
    )

    draw_center(
        f"오답 : {player['wrong']}",
        400
    )

    if player["solved"] > 0:

        accuracy = (
            player["correct"]
            / player["solved"]
            * 100
        )

    else:
        accuracy = 0

    draw_center(
        f"정답률 : {accuracy:.1f}%",
        450
    )

    draw_center(
        "R → 타이틀로",
        560,
        small_font
    )


# =========================================================
# TITLE
# =========================================================

def draw_title():

    screen.fill(BLACK)

    draw_center(
        "SOLO SAT",
        100,
        title_font
    )

    draw_center(
        "나 혼자만 1등급",
        190,
        big_font
    )

    draw_center(
        "1. 새 게임",
        330
    )

    draw_center(
        "2. 불러오기",
        380
    )

    draw_center(
        "3. 크레딧",
        430
    )

    draw_center(
        "번호를 눌러 선택",
        560,
        small_font
    )


# =========================================================
# NEW GAME
# =========================================================

def draw_new_game():

    screen.fill(BLACK)

    draw_center(
        "NEW GAME",
        70,
        title_font
    )

    draw_center(
        f"닉네임 : {player['nickname']}",
        210
    )

    draw_center(
        f"난이도 : {difficulty}",
        270
    )

    draw_center(
        f"스피드런 : {'ON' if speedrun else 'OFF'}",
        330
    )

    draw_center(
        "N : 닉네임 입력",
        420,
        small_font
    )

    draw_center(
        "D : 난이도 변경",
        460,
        small_font
    )

    draw_center(
        "S : 스피드런 ON/OFF",
        500,
        small_font
    )

    draw_center(
        "ENTER : 게임 시작",
        560,
        small_font
    )


# =========================================================
# CREDITS
# =========================================================

def draw_credits():

    screen.fill(BLACK)

    draw_center(
        "SOLO SAT",
        150,
        title_font
    )

    draw_center(
        "2026 VIAUS PROJECT",
        260,
        big_font
    )

    draw_center(
        "Python / Pygame Prototype",
        350
    )

    draw_center(
        "ESC → 돌아가기",
        550,
        small_font
    )


# =========================================================
# SAVE / LOAD
# =========================================================

SAVE_FILE = "solosat_save.json"


def save_game():

    data = {
        "player": player,
        "difficulty": difficulty,
        "speedrun": speedrun
    }

    with open(
        SAVE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def load_game():

    global difficulty
    global speedrun

    if not os.path.exists(SAVE_FILE):
        return False

    with open(
        SAVE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    player.update(data["player"])

    difficulty = data["difficulty"]
    speedrun = data["speedrun"]

    return True


# =========================================================
# START NEW GAME
# =========================================================

def start_new_game():

    global enemies

    reset_player()

    enemies = create_enemies()


# =========================================================
# MAIN LOOP
# =========================================================

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # -------------------------------------------------
        # TITLE
        # -------------------------------------------------

        if game_state == TITLE:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:

                    start_new_game()

                    game_state = NEW_GAME

                elif event.key == pygame.K_2:

                    if load_game():

                        game_state = PLAY

                elif event.key == pygame.K_3:

                    game_state = CREDITS

        # -------------------------------------------------
        # NEW GAME
        # -------------------------------------------------

        elif game_state == NEW_GAME:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    game_state = PLAY

                elif event.key == pygame.K_d:

                    if difficulty == "하":
                        difficulty = "중"
                    elif difficulty == "중":
                        difficulty = "상"
                    elif difficulty == "상":
                        difficulty = "최상"
                    else:
                        difficulty = "하"

                elif event.key == pygame.K_s:

                    speedrun = not speedrun

                elif event.key == pygame.K_n:

                    # 현재는 간단한 테스트용
                    player["nickname"] = "SOLO"

        # -------------------------------------------------
        # PLAY
        # -------------------------------------------------

        elif game_state == PLAY:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    save_game()

                    game_state = TITLE

        # -------------------------------------------------
        # QUESTION
        # -------------------------------------------------

        elif game_state == QUESTION:

            if event.type == pygame.KEYDOWN:

                # 아직 답을 안 골랐을 때
                if answer_result is None:

                    if pygame.K_1 <= event.key <= pygame.K_5:

                        answer = (
                            event.key
                            - pygame.K_0
                        )

                        check_answer(answer)

                else:

                    if event.key == pygame.K_RETURN:

                        current_question = None
                        current_enemy = None

                        # 모든 몹 제거 여부
                        remaining = any(
                            enemy["active"]
                            for enemy in enemies
                        )

                        if not remaining:

                            save_game()

                            game_state = RESULT

                        else:

                            game_state = PLAY

        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        elif game_state == RESULT:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:

                    game_state = TITLE

        # -------------------------------------------------
        # CREDITS
        # -------------------------------------------------

        elif game_state == CREDITS:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    game_state = TITLE


    # =====================================================
    # UPDATE
    # =====================================================

    if game_state == PLAY:

        update_player()

        update_enemies()

        # 몹과 충돌
        for enemy in enemies:

            if enemy["active"]:

                if player_enemy_collision(enemy):

                    start_question(enemy)

                    break

        update_camera()


    # =====================================================
    # DRAW
    # =====================================================

    if game_state == TITLE:

        draw_title()

    elif game_state == NEW_GAME:

        draw_new_game()

    elif game_state == PLAY:

        draw_world()

        draw_enemies()

        draw_player()

        draw_hud()

    elif game_state == QUESTION:

        # 배경은 그대로 유지
        draw_world()

        draw_enemies()

        draw_player()

        draw_hud()

        draw_question()

    elif game_state == RESULT:

        draw_result()

    elif game_state == CREDITS:

        draw_credits()

    pygame.display.flip()


pygame.quit()