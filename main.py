import pygame, sys

pygame.init()

screenW = 400
screenH = 600

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption('Space Invaders')

ship = pygame.image.load('ship.png')
ship = pygame.transform.scale(ship, (90, 90))
sx = 157
sSpeed = 0

bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (10, 18))
by = -300
bx = -200
bSpeed = .3

alienList = []
xPos = []
yPos = []
num = 0
aspeed = .2

# sounds
alien_sound = pygame.mixer.Sound("../pythonProject11/other sound.wav")
bullet_sound = pygame.mixer.Sound("../pythonProject11/sound2.wav")

# scores
score = 0

# define the score board function
def display_scores():
   font = pygame.font.SysFont('comic sans', size=25)
   text = font.render(f"Score: {score}", True, (255, 255, 255))
   text_rect = text.get_rect(center=(screenW / 2, 20))
   screen.blit(text, text_rect)

for i in range(5):
    for j in range(11):
        alienList.append(pygame.image.load('alien.png').convert_alpha())
        alienList[num] = pygame.transform.scale(alienList[num], (55, 50))
        xPos.append(j * 30 + 1)
        yPos.append(i * 35)
        num += 1

# set the start screen flag
start_screen = True

# start screen loop
while start_screen:
   # events
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           start_screen = False
           game_over = True
       if event.type == pygame.KEYDOWN:
           start_screen = False

   # draw the start screen
   screen.fill((0, 0, 0))
   font = pygame.font.SysFont('comic sans', size=40)
   font2 = pygame.font.SysFont('comic sans', size=30)
   title = font.render("Space Invaders", True, (255, 255, 255))
   message = font2.render("Press any key to start", True, (255, 255, 255))
   start_text_rect = title.get_rect(center=(screenW / 2, 200))
   screen.blit(title, start_text_rect)
   start_text_rect2 = title.get_rect(center=(188, 400))
   screen.blit(message, start_text_rect2)
   pygame.display.update()

gameOn = True

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                sSpeed += .2
            if e.key == pygame.K_LEFT:
                sSpeed -= .2

            if e.key == pygame.K_SPACE and by < 0:
                pygame.mixer.Sound.play(bullet_sound)
                bx = sx + 40
                by = 520 - 29
                bSpeed = -.5

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                sSpeed -= .2
            if e.key == pygame.K_LEFT:
                sSpeed += .2

        # logic
    sx += sSpeed
    if sx > 340:
        sx = 340
    if sx < 0:
        sx = 0

    by += bSpeed
    changeD = False
    for i in range(55):
        xPos[i] += aspeed
        if xPos[i] > screenW - 25 or xPos[i] < 0:
            changeD = True

    if changeD:
        changeD = False
        aspeed *= -1
        for i in range(55):
            yPos[i] += 20

    for i in range(55):
        if pygame.rect.Rect(bx, by, bullet.get_width(), bullet.get_height()).colliderect(pygame.rect.Rect(xPos[i], yPos[i], alienList[i].get_width(), alienList[i].get_height())):
            pygame.mixer.Sound.play(alien_sound)
            score += 1
            yPos[i] -= 3000
            by -= 500
            pygame.rect.Rect(bx, by, bullet.get_width(), bullet.get_height())

    # display
    screen.fill((0, 0, 0))
    screen.blit(ship, (sx, 500))
    screen.blit(bullet, (bx, by))
    for i in range(55):
        screen.blit(alienList[i], (xPos[i], (yPos[i])))
    display_scores()
    pygame.display.update()