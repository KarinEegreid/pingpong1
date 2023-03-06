import pygame

# Käivita pygame
pygame.init()

# Seadista ekraani suurus
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Karl Paju IS22')

# Laadi pildid
platform_image = pygame.image.load('pad.png').convert_alpha()
ball_image = pygame.image.load('ball-1.webp').convert_alpha()

# Määrame platvormi ja palli algasukohad
platform_x = screen_width / 2 - platform_image.get_width() / 2
platform_y = screen_height - platform_image.get_height() - 50
ball_x = screen_width / 2 - ball_image.get_width() / 2
ball_y = platform_y - ball_image.get_height()

# Määrame palli algne kiirus
ball_speed_x = 5
ball_speed_y = -5

# Määra platvormi kiirus
platform_speed = 10

# Määra algne skoor
score = 0

# Määra fondi suurus skoori kuvamiseks
font = pygame.font.SysFont(None, 36)


# Defineeri mäng läbi funktsioon
def game_over():
    # Kuva mäng läbi teade
    game_over_text = font.render("Mäng läbi!", True, (255, 0, 0))
    screen.blit(game_over_text, (
        screen_width / 2 - game_over_text.get_width() / 2, screen_height / 2 - game_over_text.get_height() / 2))

    # Kuva lõppskoor
    final_score_text = font.render(f"Lõpp tulemus: {score}", True, (0, 0, 0))
    screen.blit(final_score_text, (
        screen_width / 2 - final_score_text.get_width() / 2, screen_height / 2 + game_over_text.get_height() / 2))

    # uuenda ekraani
    pygame.display.update()

    # Oota mõned sekundid enne lõpetamist
    pygame.time.wait(3000)
    pygame.quit()
    exit()


# Alusta mängu loop-i
while True:
    # Tee sündmustega tegelemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Liiguta platvormi
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= platform_speed
    if keys[pygame.K_RIGHT] and platform_x + platform_image.get_width() < screen_width:
        platform_x += platform_speed

    # Liiguta palli
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Põruta pall tagasi seintest
    if ball_x < 0 or ball_x + ball_image.get_width() > screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y < 0:
        ball_speed_y = -ball_speed_y
    elif ball_y + ball_image.get_height() > screen_height:
        # Mäng läbi
        game_over()

    # Kontrollime kas pall läheb platformi vastu
    if ball_y + ball_image.get_height() > platform_y and \
            ball_x + ball_image.get_width() > platform_x and \
            ball_x < platform_x + platform_image.get_width():
        ball_speed_y = -ball_speed_y
        score += 1

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the images
    screen.blit(platform_image, (platform_x, platform_y))
    screen.blit(ball_image, (ball_x, ball_y))

    # Joonistame ekraanile skoori
    score_text = font.render(f"Skoor: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Uuendab ekraani
    pygame.display.update()

    # Sätime fpsi
    pygame.time.Clock().tick(120)
