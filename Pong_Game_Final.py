#########################################
# Original Programmer: Mr.G
# Heavily Modified: Brian Mao
# Date: March 4, 2014
# File Name: Pong_Game.py
# Description: I "made" pong again with Gamecube colours this time. 
#########################################

#Soundtracks Considered:
#1. Super Mario Galaxy 2 Final Boss Theme (chosen)
#2. The Legend of Zelda Twilight Princess Hidden Village
#3. Mega Man 2 Dr. Wily
#4. Super Smash Bros. Brawl Final Destination
#5. Street Fighter 2 Guile Theme

import pygame, random, sys
pygame.init()

HEIGHT = 480                            #
WIDTH  = 640                            #
TOP    = 0                              # the reference (0,0) of the coordinate system
BOTTOM = HEIGHT                         # is the top left corner
LEFT   = 0                              # 
RIGHT  = WIDTH                          #

game_window = pygame.display.set_mode((WIDTH,HEIGHT))

GREEN = (200,200,200)                 #actually grey
SILVER = (255,150,0)                  # actually orange
BLACK = (  0,  10,  0)                # is black
CYAN  = (150,5,255)                   #actually purple
WHITE=(255,255,255)                   #is white
TITLEC= (150,190,220)                 #some shade of light blue      
YELLOW=(225, 240, 0)                   #actual colours

outline = 0                             # thickness of the shapes' outline

cheatactive=False

font=pygame.font.Font('freesansbold.ttf', 65)

#---------------------------------------#
# Ball's Properties                     #
#---------------------------------------#
ballX  =  0	                        # x coordinate of the ball
ballY  =  0                             # y coordinate of the ball
ballR  = 20                             # radius of the ball
speedX =  3       #2=normal, 3=fast     # horizontal step of ball movement   #############
speedY =  3       #2=normal, 3=fast     # vertical step of ball movement    ##############

#---------------------------------------#
# Paddles' Properties                   #
#---------------------------------------#
paddleW  = 19                           # paddle width
paddle1H  = 105                           # paddle height
paddle2H  =105
paddle1X = LEFT + 10                    # x coordinate of left paddle
paddle1Y =(HEIGHT-paddle1H)/2            # y coordinate of left paddle
paddle2X = RIGHT - 10 - paddleW         # x coordinate of right paddle
paddle2Y =(HEIGHT-paddle2H)/2            # y coordinate of right paddle
paddleShift = 3                         # vertical step of paddle movement
                                        # (faster than the ball)
scoreP1 = 0
scoreP2 = 0

#---------------------------------------#
# Functions                             #
#---------------------------------------#

def closegame():
    print "You quit the game."
    pygame.quit()
    sys.exit()
    
def showscore(text,cord):
    text=str(text)
    fontsurface= font.render(text, False, WHITE)
    fontrect=fontsurface.get_rect()
    fontrect.center=cord
    game_window.blit(fontsurface,fontrect)

    
def redraw_game_window():
    game_window.fill(BLACK)
    pygame.draw.line(game_window, CYAN, (WIDTH/2, TOP), (WIDTH/2, BOTTOM), 7)#middle divider
    pygame.draw.circle(game_window, SILVER, (ballX, ballY), ballR, outline) #ball
    pygame.draw.rect(game_window, GREEN, (paddle1X, paddle1Y, paddleW, paddle1H), outline)#left paddle
    pygame.draw.rect(game_window, GREEN, (paddle2X, paddle2Y, paddleW, paddle2H), outline)#right paddle    
    pygame.draw.rect(game_window, CYAN, (0,0, WIDTH, HEIGHT), 20)  #border
    showscore(scoreP1,(WIDTH/2-50,50))
    showscore(scoreP2,(WIDTH/2+50,50))
    
    pygame.display.update()             # display must be updated to show any changes


def titlescreen():
    while True:
        game_window.fill(TITLEC)
        showscore("Python Pong", ((WIDTH/2),100))
        showscore("Hit space to play.", ((WIDTH/2),200))
        showscore("Hit ESC to exit.", ((WIDTH/2),300))
        showscore("First to 7 wins.", ((WIDTH/2),400))
        
        pygame.event.get()
        keys=pygame.key.get_pressed()
        if keys [pygame.K_SPACE]:
            break
        pygame.display.update()
        pygame.time.delay(1)

        if keys[pygame.K_ESCAPE]:
            inPlay = False
            closegame()
            #pygame.quit()
            

def gameoverscreen():
    global scoreP1, scoreP2
    if scoreP1==7:
        game_window.fill(BLACK)
        showscore("Player 1 Wins!", (335,200))
        pygame.draw.line(game_window, YELLOW, (WIDTH/2, TOP), (WIDTH/2, BOTTOM), 7)#middle divider
        #pygame.draw.circle(game_window, SILVER, (ballX, ballY), ballR, outline) #ball
        pygame.draw.rect(game_window, GREEN, (paddle1X, paddle1Y, paddleW, paddle1H), outline)#left paddle
        pygame.draw.rect(game_window, GREEN, (paddle2X, paddle2Y, paddleW, paddle2H), outline)#right paddle    
        pygame.draw.rect(game_window, YELLOW, (0,0, WIDTH, HEIGHT), 20)

        pygame.display.update()
        pygame.time.delay(8000)
        
    elif scoreP2==7:
        game_window.fill(BLACK)
        showscore("Player 2 Wins!", (335,200))
        pygame.draw.line(game_window, YELLOW, (WIDTH/2, TOP), (WIDTH/2, BOTTOM), 7)#middle divider
        #pygame.draw.circle(game_window, SILVER, (ballX, ballY), ballR, outline) #ball
        pygame.draw.rect(game_window, GREEN, (paddle1X, paddle1Y, paddleW, paddle1H), outline)#left paddle
        pygame.draw.rect(game_window, GREEN, (paddle2X, paddle2Y, paddleW, paddle2H), outline)#right paddle    
        pygame.draw.rect(game_window, YELLOW, (0,0, WIDTH, HEIGHT), 20)
       
        pygame.display.update()
        pygame.time.delay(8000)
        

def checkball():
    if (ballX + ballR)>0 and (ballX-ballR)<WIDTH:
        return True
    else:
        return False
   
    
def castnewball():
    ballAlive = checkball()
    global ballX, speedX, scoreP1, scoreP2, ballY, speedY
    if  ballAlive==False and ballX+ballR<=WIDTH/2:
        #game_window.fill(BLACK)
        #showscore("Goal!", ((WIDTH/2),100))
        pygame. time.delay(500)
        scoreP2=scoreP2+1
        speedX = -speedX
        speedY= speedY*random.choice((-1,1))
        ballX = paddle1X + paddleW + ballR  #ball respawns here in the center after leaving the screen
        ballY= paddle1Y+(paddle1H/2)
        
    if ballAlive==False and ballX-ballR>=WIDTH/2:
        #showscore("Goal!", ((WIDTH/2),100))
        pygame.time.delay(500)
        scoreP1=scoreP1+1
        speedX = -speedX
        speedY=speedY*random.choice((-1,1))
        ballX = paddle2X - ballR
        ballY= paddle2Y+(paddle2H/2)
        


#---------------------------------------#
# Main Program                          #
#---------------------------------------#
inPlay = True

#Music
pygame.mixer.music.load("smg.mp3") # soundtrack
pygame.mixer.music.play(-1) # makes it play the whole game

titlescreen()

while inPlay:

# check for key events
    pygame.event.get()
    keys = pygame.key.get_pressed()

# act upon key events
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_w] and paddle1Y > TOP:
        paddle1Y = paddle1Y - paddleShift
    if keys[pygame.K_s] and paddle1Y < BOTTOM - paddle1H:
        paddle1Y = paddle1Y + paddleShift        
    if keys[pygame.K_UP] and paddle2Y > TOP:
        paddle2Y = paddle2Y - paddleShift
    if keys[pygame.K_DOWN] and paddle2Y < BOTTOM - paddle2H:
        paddle2Y = paddle2Y + paddleShift
        
#Cheat function
    if keys[pygame.K_p]:
       cheatactive=True
    if cheatactive==True:
        paddle1H=180   #cheat lasts for the entire match
        

# move the ball
    ballX = ballX + speedX
    ballY = ballY + speedY

#function
    checkball()
    
# bounce the ball horisontally if it hit a paddle
    if ballX - ballR <= paddle1X + paddleW and ballY >= paddle1Y and ballY <= paddle1Y+paddle1H and ballX+ballR>=paddle1X:
        speedX = -speedX
        ballX = paddle1X +ballR +paddleW #ball respawns here in the center after leaving the screen
  
    if ballX + ballR >= paddle2X and ballY >= paddle2Y and ballY <= paddle2Y+paddle2H and ballX-ballR<=paddle2X+paddleW:
        speedX = -speedX
        ballX = paddle2X - ballR 
        
# bounce the ball vertically if it hit top or bottom of the game window
    if ballY < TOP or ballY > BOTTOM:
        speedY = -speedY

# Update the screen with functions
    redraw_game_window()
    castnewball()
    pygame.time.delay(3)
    

#check if the game is over
    if scoreP1==7 or scoreP2==7:
       pygame.mixer.music.stop()
       gameoverscreen()
       break
#---------------------------------------#
#"Credit" Screen
print 'The final score was: ',scoreP1,':',scoreP2
print "\n"
print "******I don't have the budget for a good credits screen.*********"
print "Template by: Mr. Grigorov"
print "Modified by: Brian Mao"
print "Special Thanks to: Kenneth Sinder and Sam Raisbeck"
print "Soundtrack: Super Mario Galaxy 2 Final Boss Theme"
print "\n"
pygame.quit()

