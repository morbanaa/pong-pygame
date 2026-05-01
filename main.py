import pygame

GAME_WIDTH = 1280
GAME_HEIGHT = 720

def main():
    # set up the window
    pygame.init()
    screen = pygame.display.set_mode((GAME_HEIGHT,GAME_HEIGHT))
    pygame.display.set_caption("Pong!")

    # Create game objects
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60) # Game Runs at 60 FPS

        # Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update

        # Draw
        screen.fill((0,200,0))
        pygame.display.update()
    
    # Closes out of window
    pygame.quit()


# Program Entry Point
if __name__ == "__main__":
    main()