# Karl Paju IS22

import pygame

# Käivita pygame
pygame.init()  # Käivitame pygame.

# Seadista ekraani suurus
screen_width = 640  # Seadistame ekraani laiuse
screen_height = 480  # Seadistame ekraani pikkuse
screen = pygame.display.set_mode((screen_width, screen_height))  # Loome ekraani
pygame.display.set_caption('Karl Paju IS22')  # Anname ekraanile nime

# Laadi pildid
platform_image = pygame.image.load('pad.png').convert_alpha()  # Anname platform_imagele väärtuse
ball_image = pygame.image.load('ball-1.webp').convert_alpha()  # Anname Ball_imagele väärtuse.

# Määrame platvormi ja palli algasukohad
platform_x = screen_width / 2 - platform_image.get_width() / 2  # Määrame platvormi x telje algasukoha
platform_y = screen_height - platform_image.get_height() - 50  # Määrame platvormi y telje algasukoha
ball_x = screen_width / 2 - ball_image.get_width() / 2  # Määrame palli x telje algasukoha
ball_y = platform_y - ball_image.get_height()  # Määrame palli y telje algasukoha.

# Määrame palli algne kiirus
ball_speed_x = 2  # Määrame palli x telje kiiruseks 5
ball_speed_y = -2  # Määrame palli y telje kiiruseks 5

# Määra platvormi kiirus
platform_speed = 10  # Määrame platvormi kiiruseks 10

# Määra algne skoor
score = 0

# Määra fondi suurus skoori kuvamiseks
font = pygame.font.SysFont(None, 36)  # Määrame fondi suuruseks 36 ning jätame sellele tavapärase pygame fondi.

# Taustamuusika
pygame.mixer.music.load("theme.wav")  # laeme taustamuusika
pygame.mixer.music.play(-1)  # Käivitame taustamuusika ning paneme selle korduma


# Defineeri mäng läbi funktsioon
def game_over():
    # Kuva mäng läbi teade
    pygame.mixer.music.stop()  # Lõpetab taustamuusika
    game_over_sound = pygame.mixer.Sound("game_over.wav")  # anname game over soundile väärtuse
    game_over_sound.play()  # Käivitame game over soundi
    game_over_text = font.render("Mäng läbi!", True, (255, 0, 0))  # Ekraanile ilmub tekst mäng läbi punases värvis.
    screen.blit(game_over_text, (
        screen_width / 2 - game_over_text.get_width() / 2,  # Määrame teksti suuruse ja laiuse
        screen_height / 2 - game_over_text.get_height() / 2))  # Määrame teksti suuruse ja pikkuse

    # Kuva lõppskoor
    final_score_text = font.render(f"Lõpp tulemus: {score}", True,
                                   (0, 0, 0))  # Ekraanile ilmub Lõpp tulemus: ning mängija skoor mustas värvis.
    screen.blit(final_score_text, (
        screen_width / 2 - final_score_text.get_width() / 2,  # Määrame teksti suuruse ja laiuse
        screen_height / 2 + game_over_text.get_height() / 2))  # Määrame teksti suuruse ja pikkuse

    # uuenda ekraani
    pygame.display.update()  # uuendab ekraani

    # Oota mõned sekundid enne lõpetamist
    pygame.time.wait(3000)  # Ootame 3 sek
    pygame.quit()  # Sulgeme akna
    exit()  # sulgeme akna

0
# Alusta mängu loop-i
while True:
    # sündmustega tegelemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Liiguta platvormi
    keys = pygame.key.get_pressed()  # anname keys muutujale väärtuse
    if keys[pygame.K_LEFT] and platform_x > 0:  # Kui vajutame vasakut klahvi ning platvorm x teljel on väiksem kui 0
        platform_x -= platform_speed  # siis neutraliseerime platformi kiiruse
    if keys[
        pygame.K_RIGHT] and platform_x + platform_image.get_width() < screen_width:  # Kui vajutame paremat klahvi x teljel ja ning on väiksem kui 0
        platform_x += platform_speed  # siis neutraliseerime platformi kiiruse

    # Liiguta palli
    ball_x += ball_speed_x  # Liigutame palli x teljes
    ball_y += ball_speed_y  # Liigutame palli y teljes

    # Põruta pall tagasi seintest
    if ball_x < 0 or ball_x + ball_image.get_width() > screen_width:  # kui pall x teljes on väiksem värtus kui + või pall x teljes + palli laius on väiksem kui ekraani laius
        ball_speed_x = -ball_speed_x  # siis on x palli kiirus võrdne -x palli kiirusega

        # lahutame skoorilt 1
        score -= 1 # Kui pall põrkab vastu seina lahutame punktid ühe võrra.

    if ball_y < 0:
        ball_speed_y = -ball_speed_y  # kui pall y teljes on väiksem värtus kui + või pall x teljes + palli laius on väiksem kui ekraani pikkus
    elif ball_y + ball_image.get_height() > screen_height:
        # Mäng läbi
        game_over()

    # Kontrollime kas pall läheb platformi vastu
    if ball_y + ball_image.get_height() > platform_y and \
            ball_x + ball_image.get_width() > platform_x and \
            ball_x < platform_x + platform_image.get_width():
        ball_speed_y = -ball_speed_y
        score += 1


    # Täiendame ekraani
    screen.fill((255, 255, 255))  # Ekraanile ilmub must värv

    # Joonistame ekraanile nõutud pildid.
    screen.blit(platform_image, (platform_x, platform_y))  # Joonistame ekraanile platvormi
    screen.blit(ball_image, (ball_x, ball_y))  # Joonistame ekraanile palli

    # Joonistame ekraanile skoori
    score_text = font.render(f"Skoor: {score}", True, (0, 0, 0))  # Joonistame ekraanile mustas värvis
    screen.blit(score_text, (10, 10))  # Joonistame ekraanile selle vasakusse nurka

    # Uuendab ekraani
    pygame.display.update()  # uuendame ekraani

    # Sätime fpsi
    pygame.time.Clock().tick(120)  # Määrasime ekraani fpsiks 120


