import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from core.game import Game


# 함수 기능
def main():  # ?? ???? ?? ?? ??
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 변수 기능
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()  # 변수 기능
    game = Game(screen)  # 변수 기능

    running = True  # 변수 기능
    while running:
        dt = clock.tick(FPS) / 1000.0  # 변수 기능
        for event in pygame.event.get():
            # 조건 분기
            if event.type == pygame.QUIT:  # ?? ??? ??
                running = False  # 변수 기능
            else:  # ? ??? ??? ? ??
                game.handle_event(event)
        game.update(dt)
        game.draw()
        pygame.display.flip()

    pygame.quit()


# 조건 분기
if __name__ == "__main__":  # ??? ?? ?? ?? ??
    main()
