# Racing Game for MTE-2
import pygame
#for fps 
import time
#for other car genetare at random
import random

pygame.init()#starting pygame

# images of game
icon = pygame.image.load('icon.png')
l_track = pygame.image.load('left_side.png')
r_track = pygame.image.load('right_side.png')
p_car = pygame.image.load('player car.png')
o_car1 = pygame.image.load('other car1.png')
o_car2 = pygame.image.load('other car2.png')
o_car3 = pygame.image.load('other car3.png')
start_s = pygame.image.load('start_screen.png')

#drawing a rectangle around the object to dictate hit
p_ract = p_car.get_rect()
o_ract1 = o_car1.get_rect()
o_ract2 = o_car2.get_rect()
o_ract3 = o_car3.get_rect()
o_ract4 = o_car2.get_rect()
o_ract5 = o_car3.get_rect()
o_ract6 = o_car1.get_rect()
o_ract7 = o_car2.get_rect()

#audio of car
#pygame.mixer.music.load('car.mp3')


# game screen
screen = pygame.display.set_mode((800, 600))

# game title
pygame.display.set_caption('Racing Game for MTE-2')
pygame.display.set_icon(icon)

#score of game
score_v = 0
font = pygame.font.Font('SCOREBOARD.ttf',28)
textX = 1
textY = 10
def show_score(x,y):
    score = font.render('Score:'+ str(score_v),True, (255,0,0))
    screen.blit (score,(x,y))

# Game over 
over_font = pygame.font.Font('over.ttf',150)
score_f = pygame.font.Font('SCOREBOARD.ttf',50)
def game_over():
    over_text = over_font.render('GAME OVER',True, (0,0,0))
    screen.blit (over_text,(220,170))
    screen.blit (p_car,(p_ract))
    score = score_f.render('Score:'+ str(score_v),True, (0,0,0))
    screen.blit (score,(285,5))
    pygame.mixer.music.stop()



# player and other car x and y codinte and speed
o_ract1.x = random.randint(130, 632)
o_ract1.y = random.randint(5, 50)
change_o1y = 6 #speed

o_ract2.x = random.randint(110, 612)
o_ract2.y = random.randint(5, 50)
change_o2y = 4

o_ract3.x = random.randint(110, 612)
o_ract3.y = random.randint(5, 50)
change_o3y = 3

o_ract4.x = random.randint(110, 612)
o_ract4.y = random.randint(5, 50)
change_o4y = 2

o_ract5.x = random.randint(110, 612)
o_ract5.y = random.randint(5, 50)
change_o5y = 5

o_ract6.x = random.randint(130, 632)
o_ract6.y = random.randint(5, 50)
change_o6y = 3

o_ract7.x = random.randint(110, 612)
o_ract7.y = random.randint(5, 50)
change_o7y = 4

p_ract.x = 365
p_ract.y = 520
change_x= 0
    
# game fps setup
FPS = 60
clock = pygame.time.Clock()

start = True
run = True
over = True
# game starting screen
while start:
    clock.tick(FPS)
    
    screen.blit(start_s, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            start = False
            break
        if event.type == pygame.QUIT:
            run = False
            start = False
            over = False
            break
#pygame.mixer.music.play(-1)#run car audio in loop


#loop for run game
while run:
    clock.tick(FPS)

    score_v +=1
    # draw track on screen
    screen.fill((255, 255, 255))
    screen.blit(l_track, (0, 0))
    screen.blit(r_track, (666, 0))
    
    for event in pygame.event.get():
    #for quiting game
        if event.type == pygame.QUIT:
            run = False
            break
    
    # taking input from keybord for player motion 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x -= 5
            if event.key == pygame.K_RIGHT:
                change_x += 5   
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_x = 0
    # motion of player and other car
    o_ract1.y += change_o1y
    o_ract2.y += change_o2y
    o_ract3.y += change_o3y
    o_ract4.y += change_o4y
    o_ract5.y += change_o5y
    o_ract6.y += change_o6y
    o_ract7.y += change_o7y
    p_ract.x += change_x
    if p_ract.x <= 130:
        p_ract.x = 130
    elif p_ract.x >= 632:
        p_ract.x = 632
    
    #game over condication
    if p_ract.colliderect(o_ract1):
        car_hit = pygame.mixer.Sound('crash.wav')
        car_hit.play()
        break
    if p_ract.colliderect(o_ract2):
        car_hit = pygame.mixer.Sound('crash.wav')
        car_hit.play()
        break
    if p_ract.colliderect(o_ract3):
        car_hit = pygame.mixer.Sound('crash.wav')
        car_hit.play()
        break
    if p_ract.colliderect(o_ract4):
        car_hit = pygame.mixer.Sound('crash.wav')
        car_hit.play()
        break
    if p_ract.colliderect(o_ract5):
        car_hit = pygame.mixer.Sound('crash.wav')
        car_hit.play()
        break
    if p_ract.colliderect(o_ract6):
        car_hit = pygame.mixer.Sound('crash.wav')
        car_hit.play()
        break
    if p_ract.colliderect(o_ract7):
        car_hit = pygame.mixer.Sound('crash.wav')
        car_hit.play()
        break

    # macking new car top on the screeen
    if o_ract1.y >= 600:
        o_ract1.x = random.randint(130, 632)
        o_ract1.y = random.randint(5, 50)
    if o_ract2.y >= 600:
        o_ract2.x = random.randint(130, 632)
        o_ract2.y = random.randint(5, 50)
    if o_ract3.y >= 600:
        o_ract3.x = random.randint(130, 632)
        o_ract3.y = random.randint(5, 50)
    if o_ract4.y >= 600:
        o_ract4.x = random.randint(130, 632)
        o_ract4.y = random.randint(5, 50)
    if o_ract5.y >= 600:
        o_ract5.x = random.randint(130, 632)
        o_ract5.y = random.randint(5, 50)
    if o_ract6.y >= 600:
        o_ract6.x = random.randint(130, 632)
        o_ract6.y = random.randint(5, 50)
    if o_ract7.y >= 600:
        o_ract7.x = random.randint(130, 632)
        o_ract7.y = random.randint(5, 50)
# drawing cars on screen
    screen.blit (p_car,(p_ract))
    screen.blit (o_car1,(o_ract1))
    screen.blit (o_car2,(o_ract2))
    screen.blit (o_car3,(o_ract3))
    screen.blit (o_car2,(o_ract4))
    screen.blit (o_car3,(o_ract5))
    screen.blit (o_car1,(o_ract6))
    screen.blit (o_car2,(o_ract7))
    show_score(textX,textY)
    pygame.display.update()#update tha display

# game over loop
while over:
    clock.tick(FPS)
    
    screen.fill((255, 255, 255))
    screen.blit(l_track, (0, 0))
    screen.blit(r_track, (666, 0))
    game_over()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False
            break


pygame.quit()
