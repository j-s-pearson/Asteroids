import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH  # pyright: ignore[reportMissingImports]
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    should_play = True

    while(should_play):
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_play = False

        screen.fill("black")
        pygame.display.flip()

    print("Closing Asteroids")

if __name__ == "__main__":
    main()
