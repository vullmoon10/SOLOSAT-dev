# main.py
# 실행 파일은 최대한 간단하게 유지해.

import pygame

from settings import WIDTH, HEIGHT, TITLE, FPS
from game import Game


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    game = Game(screen)

    # [수정 가능] 게임 실행
    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()