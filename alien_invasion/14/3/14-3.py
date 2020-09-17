import sys
import pygame
from button import Button
from pygame.sprite import Group
from ship import Ship
from bullet import Bullet
from target import Target

game_active = False
lives = 3
amount_hit = 0
speed_factor = 1


def fire_bullet(screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < 100:
        new_bullet = Bullet(screen, ship)
        bullets.add(new_bullet)


def check_events(ship, bullets, play_button, screen, target):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.up_pressed = True
            elif event.key == pygame.K_DOWN:
                ship.down_pressed = True
            elif event.key == pygame.K_SPACE:
                fire_bullet(screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.up_pressed = False
            elif event.key == pygame.K_DOWN:
                ship.down_pressed = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ship, bullets, play_button, mouse_x, mouse_y, target)


def start_game(ship, bullets, target):
    global game_active, lives, amount_hit

    game_active = True
    lives = 3
    amount_hit = 0

    target.set_speed(1)

    pygame.mouse.set_visible(False)

    # Empty the list of aliens and bullets.
    bullets.empty()

    # Center the ship.
    ship.center_ship()


def check_play_button(ship, bullets, play_button, mouse_x, mouse_y, target):
    global game_active

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_active:
        start_game(ship, bullets, target)


def update_screen(screen, ship, play_button, target, bullets, catched_text, lives_text):
    screen.fill((230, 230, 230))
    ship.blitme()
    target.draw()

    for bullet in bullets:
        bullet.draw()

    global game_active
    if not game_active:
        play_button.draw_button()

    screen.blit(catched_text, (0, 0))
    screen.blit(lives_text, (0, 50))

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(screen, bullets, target):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.right > screen.get_rect().right:
            bullets.remove(bullet)
            global lives
            # lives -= 1

        if target.rect.colliderect(bullet):
            global amount_hit
            amount_hit += 1
            bullets.remove(bullet)
            target.set_speed(target.get_speed() * 1.1)


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Target practice")

    # Make the Play button.
    play_button = Button(screen, "Play")

    ship = Ship(screen)
    bullets = Group()
    target = Target(screen)

    # Invoke globals
    global game_active

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        check_events(ship, bullets, play_button, screen, target)

        catched_text = myfont.render('Hits: ' + str(amount_hit), False, (0, 0, 0))
        lives_text = myfont.render('Lives: ' + str(lives), False, (0, 0, 0))

        if game_active:
            # Update ship
            ship.update()
            # Update target
            target.update()
            # Update bullets
            update_bullets(screen, bullets, target)

            if lives == 0:
                game_active = False
                pygame.mouse.set_visible(True)

        # Redraw the screen during each pass through the loop
        update_screen(screen, ship, play_button, target, bullets, catched_text, lives_text)


run_game()
