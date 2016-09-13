####################
#David Yao
#Alex Cole
#CS111 final project
####################

import pygame, datetime, time, random

#global variables
SCORELIST = []
USERNAME = ''
HARDMODE = False
MEDMODE = False
EASYMODE = False

#sets the properties of the buttons
class Buttons:
    def __init__(self, text):
        self.obj = None
        self.__text = text
        self.__fontColor = (0,0,0)
        self.__buttonColor = (125,125,125)
        self.__highlight = (255,255,0)
        self.__shouldHighlight = False

    #creates the text font on the button
    def buttonText(self):
        buttonFont = pygame.font.Font(None,20)
        return buttonFont.render(self.__text, 1, self.__fontColor)

    #detects if mouse is over button
    def highlightButton(self, myMouse):
        if self.obj.collidepoint(myMouse):
            self.__shouldHighlight = True
        else:
            self.__shouldHighlight = False
            
    #highlights button when mouse is hovering over it      
    def highlightColor(self):
        if self.__shouldHighlight == True:
            return self.__highlight
        else:
            return self.__buttonColor

    #puts the button on the screen
    def makeButton(self, gameScreen, myMouse, buttonPos, textPos):
        self.obj = pygame.draw.rect(gameScreen, self.highlightColor(), buttonPos)
        self.highlightButton(myMouse)
        gameScreen.blit(self.buttonText(), textPos)

def screenInitialize():
    pygame.init()
    pygame.display.set_caption('Samurai Duel')
    
    #assigns button variables
    scoreButton = Buttons('Scoreboard')
    playGameButton = Buttons('Play')
    instructionButton = Buttons('Instructions')
    
    menuBacking = pygame.image.load("game_images/samurai_showdown.png")
    gameScreen = pygame.display.set_mode((640, 480))

    showScreen = True
    
    #whole while-loop makes the window actually stay up and not insta-close
    while showScreen:
        myMouse = pygame.mouse.get_pos()
        
        #makes the menu window display a cool picture
        gameScreen.blit(menuBacking, (0, 0))
        
        #sets the buttons
        playGameButton.makeButton(gameScreen, myMouse, (275,290,100,40), (310,303))
        scoreButton.makeButton(gameScreen, myMouse, (275,340,100,40), (290,353))
        instructionButton.makeButton(gameScreen, myMouse, (275,390,100,40), (290,403))
        
        #quits if the player x's out
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showScreen = False
#detects which button the user has clicked on and gets rid of prior screens
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if scoreButton.obj.collidepoint(myMouse):
                    scoreScreen()
                    showScreen = False
                elif playGameButton.obj.collidepoint(myMouse):
                    difficultyScreen()
                    showScreen = False
                elif instructionButton.obj.collidepoint(myMouse):
                    instructionScreen()
                    showScreen = False
                    
        #need this to actually show stuff on screen
        pygame.display.update()

#sets up the instruction screen following the erasure of the menu screen
def instructionScreen():
    pygame.init()
    pygame.display.set_caption('Samurai Duel')
    backButton = Buttons('Back')
    showScreen = True
    gameScreen = pygame.display.set_mode((640, 480))
    
    #Place holder in lieu of real instructions
    instructionBacking = pygame.image.load("game_images/instructions.png")
    
    #shows the instruction screen and basically repeats the menu screen magic
    while showScreen:
        myMouse = pygame.mouse.get_pos()
        gameScreen.blit(instructionBacking, (0, 0))
        backButton.makeButton(gameScreen, myMouse, (105,390,100,40), (135,403))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showScreen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.obj.collidepoint(myMouse):
                    #gets you back to the menu screen
                    screenInitialize()
                    showScreen = False
        pygame.display.update()
        
#sets up the score screen following the erasure of the menu screen   
def scoreScreen():
    pygame.init()
    pygame.display.set_caption('Samurai Duel')
    readScore()
    backButton = Buttons('Menu')
    showScreen = True
    gameScreen = pygame.display.set_mode((640, 480))
    
    #shows the score screen and uses magic again
    while showScreen:
        myMouse = pygame.mouse.get_pos()
        scoreFont = pygame.font.Font(None,20)
        titleFont = pygame.font.Font(None,40)
        gameScreen.fill((253,134,83))

        gameScreen.blit(titleFont.render("TOP SCORES", True, (0,0,0)),(260,120))
        #iterates through SCORELIST, putting up each score on screen
        for i in range(len(SCORELIST)):
            gameScreen.blit(scoreFont.render('rank ' + str(i+1)+ ':  ' + SCORELIST[i], True, (0,0,0)),(220,(160+(i*20))))

        backButton.makeButton(gameScreen, myMouse, (275,390,100,40), (310,403))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showScreen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.obj.collidepoint(myMouse):
                    #gets you back to the menu screen
                    screenInitialize()
                    showScreen = False
        pygame.display.update()

def difficultyScreen():
    pygame.init()
    pygame.display.set_caption('Samurai Duel')
#global difficulty variables
    global HARDMODE
    global MEDMODE
    global EASYMODE

    difficultyBacking = pygame.image.load("game_images/difficulty_selection.bmp")

    backButton = Buttons('Menu')
    gameButton = Buttons('Play')
    hardButton = Buttons('Expert')
    medButton = Buttons('Novice')
    easyButton = Buttons('Beginner')

    showScreen = True
    gameScreen = pygame.display.set_mode((640, 480))
    
    titleFont = pygame.font.Font(None,40)
    
    while showScreen:
        myMouse = pygame.mouse.get_pos()
        gameScreen.blit(difficultyBacking, (0, 0))
#reminder: buttons go ((x,y,length,height),(text x, text y))
        backButton.makeButton(gameScreen, myMouse, (90,390,100,40), (120,403))
        gameButton.makeButton(gameScreen, myMouse, (455,390,100,40), (490,403))
        hardButton.makeButton(gameScreen, myMouse, (455,170,100,65), (480,195))
        medButton.makeButton(gameScreen, myMouse, (270,170,100,65), (295,195))
        easyButton.makeButton(gameScreen, myMouse, (90,170,100,65), (112,195))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showScreen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.obj.collidepoint(myMouse):
                    #gets you back to the menu screen
                    HARDMODE = False
                    EASYMODE = False
                    MEDMODE = False
                    screenInitialize()
                    showScreen = False
                elif hardButton.obj.collidepoint(myMouse):
                    #sets hard mode
                    HARDMODE
                    EASYMODE = False
                    MEDMODE = False
                elif medButton.obj.collidepoint(myMouse):
                    #sets medium mode
                    MEDMODE
                    HARDMODE = False
                    EASYMODE = False
                elif easyButton.obj.collidepoint(myMouse):
                    #sets easy
                    EASYMODE = True
                    MEDMODE = False
                    HARDMODE = False
                elif gameButton.obj.collidepoint(myMouse):
                    if HARDMODE == True or EASYMODE == True or MEDMODE == True:
                        reflexGame()
                        showScreen = False
                    else:
                        gameScreen.blit(titleFont.render("Please select a difficulty!", True, (0,0,0)),(140,100))
                        pygame.display.update()
                        time.sleep(3)
        pygame.display.update()

#this IS the game
def reflexGame():
    gameScreen = pygame.display.set_mode((640,480))
    battleBack = pygame.image.load("game_images/empty_field.png")
    battleFont = pygame.font.SysFont(None,30)
    cutEm = pygame.image.load("game_images/cut_em.png")
    
#loads all player images
    
    youStand = pygame.image.load("game_images/player_stand.png")
    youStrike = pygame.image.load("game_images/player_strike.png")
    youDead = pygame.image.load("game_images/player_death.png")
    youPrep1 = pygame.image.load("game_images/player_prep_1.png")
    youPrep2 = pygame.image.load("game_images/player_prep_2.png")
    youPrep3 = pygame.image.load("game_images/player_prep_3.png")
    youPrep4 = pygame.image.load("game_images/player_prep_4.png")
    youPrep5 = pygame.image.load("game_images/player_prep_4.png")
    
    chopYou = pygame.image.load("game_images/chopped_you.png")
    youSlash = pygame.mixer.Sound('game_sound/Slash1.ogg')
    dramaticWind = pygame.mixer.Sound('game_sound/dramatic_wind.ogg')
    japanFlute = pygame.mixer.Sound('game_sound/Japanese_Flute.ogg')
    goTime = pygame.mixer.Sound('game_sound/Flash2.ogg')
    
    gameScreen.blit(battleFont.render("GET READY!", True, (0,255,0)),(260,180))
    levelCount = 1
    timeCount = 0
    
    youLose = False
    showScreen = True
    
#sets time to react based on difficulty level
    if HARDMODE == True:
        level1Time = 240
        level2Time = 230
        level3Time = 220
        level4Time = 210
        level5Time = 200
    elif MEDMODE == True:
        level1Time = 280
        level2Time = 270
        level3Time = 260
        level4Time = 250
        level5Time = 240
    elif EASYMODE == True:
        level1Time = 300
        level2Time = 290
        level3Time = 280
        level4Time = 270
        level5Time = 260
    
    pygame.display.update()
    time.sleep(2)
    
    for i in range(5):
        japanFlute.set_volume(.5)
        japanFlute.play()
        
#loads enemy images based on level
        enemyStand = pygame.image.load("game_images/enemy_"+str(levelCount)+"_stand.png")
        enemyStrike = pygame.image.load("game_images/enemy_"+str(levelCount)+"_slice.png")
        enemyDead = pygame.image.load("game_images/enemy_"+str(levelCount)+"_dead.png")
        enemyPrep1 = pygame.image.load("game_images/enemy_"+str(levelCount)+"_prep_1.png")
        enemyPrep2 = pygame.image.load("game_images/enemy_"+str(levelCount)+"_prep_2.png")
        enemyPrep3 = pygame.image.load("game_images/enemy_"+str(levelCount)+"_prep_3.png")
        enemyPrep4 = pygame.image.load("game_images/enemy_"+str(levelCount)+"_prep_4.png")
        enemyPrep5 = pygame.image.load("game_images/enemy_"+str(levelCount)+"_prep_5.png")

        gameScreen.fill((0,0,0))
        gameScreen.blit(battleFont.render("LEVEL "+str(levelCount)+"! GET READY!", True, (255,255,255)),(210,180))
            
        #sets battle conditions: location, sound, and enemy prep animations
        enemyPrepLst = [enemyPrep1, enemyPrep2, enemyPrep3, enemyPrep4, enemyPrep5]
        playerPrepLst = [youPrep1, youPrep2, youPrep3, youPrep4, youPrep5]
        dramaticWind.play()
        pygame.display.update()
        time.sleep(2)
            
        gameScreen.blit(battleBack,(0,0))
        gameScreen.blit(youStand,(0,0))
        gameScreen.blit(enemyStand, (0,0))
        pygame.display.update()
        time.sleep(1)
        
        for i in range(5):
            gameScreen.blit(battleBack,(0,0))
            gameScreen.blit(enemyPrepLst[i], (0,0))
            gameScreen.blit(playerPrepLst[i], (0,0))
            pygame.display.update()
            time.sleep(.05)
        
        #after showing the samurai, waits to show cutEm
        time.sleep(random.random()*3+4)
            
        goTime.play()
        time.sleep(.35)
        gameScreen.blit(cutEm, (0,0))
        #makes the reaction cue appear
        pygame.display.update()
        #starts timer
        timerStart = datetime.datetime.now()
        timerOn = True
        #clears the move queue, so no cheating with queued moves
        pygame.event.clear()
        while timerOn:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    timerEnd = datetime.datetime.now()
                    timerOn = False
        reactTime = timerEnd-timerStart
        print("Your time on level",levelCount,"was",reactTime)

        #checks what level you're on
        if levelCount == 1:
            if reactTime > datetime.timedelta(milliseconds=level1Time):
                youLose = True
            
        elif levelCount == 2:
            if reactTime > datetime.timedelta(milliseconds=level2Time):
                youLose = True
            
        elif levelCount == 3:
            if reactTime > datetime.timedelta(milliseconds=level3Time):
                youLose = True
            
        elif levelCount == 4:
            if reactTime > datetime.timedelta(milliseconds=level4Time):
                youLose = True
            
        elif levelCount == 5:
            if reactTime > datetime.timedelta(milliseconds=level5Time):
                youLose = True
                
        timeCount += (reactTime.total_seconds())
            
        gameScreen.fill((0,0,0))
        pygame.display.update()
        dramaticWind.stop()
        time.sleep(.5)
        youSlash.play()
        gameScreen.blit(chopYou, (0,0))
        pygame.display.update()
        time.sleep(.5)
        gameScreen.fill((0,0,0))
        pygame.display.update()
        time.sleep(.5)

        #what happens if you lose
        if youLose:
            gameScreen.blit(battleFont.render("YOU LOST!", True, (255,255,255)),(220,180))
            gameScreen.blit(battleBack,(0,0))
            gameScreen.blit(youDead,(0,0))
            gameScreen.blit(enemyStrike, (0,0))
            pygame.display.update()
            time.sleep(3)
            break
        #and what happens if you win
        else:
            gameScreen.blit(battleBack,(0,0))
            gameScreen.blit(youStrike,(0,0))
            gameScreen.blit(enemyDead, (0,0))
            pygame.display.update()
            levelCount += 1
            time.sleep(2)
#shows reaction time (note that "%.2f"% is necessary to cut off the decimal at the hundreths)
        gameScreen.fill((0,0,0))
        gameScreen.blit(battleFont.render("Your reaction time for this level was:", True, (255,255,255)),(130,180))
        gameScreen.blit(battleFont.render(str("%.2f"%(reactTime.total_seconds()))+' seconds',True,(255,255,255)), (250,200))
        pygame.display.update()
        time.sleep(4)

    #end of game background screen
    gameScreen.blit(battleBack, (0,0))
    pygame.display.update()

    #exits program after loss or after beating all 5 levels
    dramaticWind.stop()
    gameScreen.fill((0,0,0))
    pygame.display.update()
    gameScreen.blit(battleFont.render("Your average reaction time is:", True, (255,255,255)),(150,180))
    gameScreen.blit(battleFont.render(str("%.2f"%(timeCount/levelCount))+' seconds', True, (255,255,255)),(230,200))
    pygame.display.update()
    time.sleep(4)

    #writes avg reaction time to scoreDoc.txt
    fin = open('scoreDoc.txt','a')
    fin.write(USERNAME+' - '+str("%.2f"%(timeCount/levelCount))+' seconds'+ ' - Level '+str(levelCount-1)+'\n')
    fin.close()
    
    gameScreen.fill((0,0,0))
    gameScreen.blit(battleFont.render("PRESS ANY KEY TO SEE SCORES", True, (255,255,255)),(140,180))
    pygame.display.update()

    #quits the program
    while showScreen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                scoreScreen()
                showScreen = False
            if event.type == pygame.QUIT:
                pygame.quit()

#reads a list of scores
def readScore():
    file = open('scoreDoc.txt','r')
    scores = file.readlines()

    global SCORELIST

    listoscores = []
    for line in scores:
        raw = line.split()
        score = float(raw[2])
        listoscores.append(score)
    listoscores.sort()
#if-loop prevents index range errors
    if len(listoscores) >= 5:
        for i in range(5):
            for line in scores:
                if str(listoscores[i]) in line:
                    #prevents duplicates from appearing on scoreboard
                    if ''.join(line.split('\n')) not in SCORELIST:
                        SCORELIST.append(''.join(line.split('\n')))
    elif len(listoscores)< 5:
        for i in range(len(listoscores)):
            for line in scores:
                if str(listoscores[i]) in line:
                    if ''.join(line.split('\n')) not in SCORELIST:
                        SCORELIST.append(''.join(line.split('\n')))
def main():
    global USERNAME
    USERNAME = str(input("Input your name: "))
    screenInitialize()
main()
