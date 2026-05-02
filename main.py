import pygame
import random
from classes import PlayerOne,PlayerTwo,Ball

GAME_WIDTH = 1280
GAME_HEIGHT = 720

def main():
    # set up the window
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
    pygame.display.set_caption("Pong!")

    # Create game objects
    clock = pygame.time.Clock()
    player_one = PlayerOne(20,GAME_HEIGHT//2,5)
    player_two = PlayerTwo(GAME_WIDTH - 40,GAME_HEIGHT//2,5)
    ball = Ball(GAME_WIDTH//2,GAME_HEIGHT//2,3,random.randint(1,2),random.randint(0,10))

    running = True
    while running:
        clock.tick(60) # Game Runs at 60 FPS

        ##############################################
        # Input
        ##############################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        ##############################################
        # Update
        ##############################################
        # Move Ball
        ball.xpos,ball.ypos = ball.update()
        

        ##############################################
        # Draw
        ##############################################
        #Draw Background
        screen.fill((0,200,0))
        #Draw PlayerOne
        pygame.draw.rect(screen,(0,0,0),(player_one.xpos,player_one.ypos,20,100))
        #Draw PlayerTwo
        pygame.draw.rect(screen,(0,0,0),(player_two.xpos,player_two.ypos,20,100))
        #Draw Ball
        pygame.draw.circle(screen,(255,0,0),(ball.xpos,ball.ypos),10)

        pygame.display.update() # Apply Changes
    
    # Closes out of window
    pygame.quit()


# Program Entry Point
if __name__ == "__main__":
    main()