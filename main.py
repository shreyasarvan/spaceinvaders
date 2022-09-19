import random
import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Setting the background
background=pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg =pygame.image.load('enemy.png')
enemyX = 370
enemyY = 50
enemyX_change=4
enemyY_change=40


enemyX=random.randint(0,736)
enemyY=random.randint(0,150)


#Ready-we cannot see the bullet
#Fire-the bullet is fired and it is visible on the screen



#Bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=50
bulletY=480
bulletX_change=0
bullet_state="ready"



def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x,y))

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change=-5
            if event.key == pygame.K_RIGHT:
                playerX_change=5
            if event.key == pygame.K_SPACE:
                if bullet_state=="ready":
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                playerX_change=0
    #5+0.5=5.5
    #5+=0.5
    #7-=1
    playerX+=playerX_change
    #Setting boundaries for the player movement
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736


     #Enemy Movement
    enemyX+=enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY+=enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY+=enemyY_change

    #Bulllet movement
    if bulletY<=0:
        bullet=480
        bulllet_state="ready"
    if bullet_state=="fire":
        fire_bullet(bullletX,bulletY)





    fire_bullet(bulletX,bulletY)
    enemy(enemyX,enemyY)
    player(playerX, playerY)
    pygame.display.update()
