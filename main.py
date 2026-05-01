import pygame

GAME_WIDTH = 1280
GAME_HEIGHT = 720

def main():
    # set up the window
    pygame.init()
    screen = pygame.display.set_mode((GAME_HEIGHT,GAME_HEIGHT))
    pygame.display.set_caption("Pong!")


# Program Entry Point
if __name__ == "__main__":
    main()