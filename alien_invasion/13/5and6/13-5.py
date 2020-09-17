import sys
import pygame
from basket import Basket
from ball import Ball


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Catch the ball")

    basket = Basket(screen)
    ball = Ball(screen)

    left_pressed = False
    right_pressed = False

    amount_catched = 0
    lives = 3

    # Start the main loop for the game.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_pressed = False
                elif event.key == pygame.K_RIGHT:
                    right_pressed = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_pressed = True
                elif event.key == pygame.K_RIGHT:
                    right_pressed = True

        # Watch for keyboard and mouse events.
        screen.fill((0, 0, 0))

        ball.update()
        basket.update(left_pressed, right_pressed)

        ball.draw()
        basket.draw()

        if basket.rect.colliderect(ball):
            ball = Ball(screen)
            amount_catched += 1

        catched_text = myfont.render('Catched: ' + str(amount_catched), False, (255, 255, 255))
        lives_text = myfont.render('Lives: ' + str(lives), False, (255, 255, 255))
        screen.blit(catched_text, (0, 0))
        screen.blit(lives_text, (0, 50))

        if ball.y > 768:
            ball = Ball(screen)
            lives -= 1
            if lives < 1:
                break

        # Redraw the screen during each pass through the loop
        pygame.display.flip()


run_game()
