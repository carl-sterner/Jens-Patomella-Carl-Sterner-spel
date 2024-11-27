import pygame
from time import sleep
from entities import *
import random

class Karta():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.minObj = 21
        self.maxObj = 34

        self.minMon = 21
        self.maxMon = 34
        self.monsters = []
        self.monsters_pos = []
    
    def PlaceraFöremål(self):
        j = random.randint(self.minObj, self.maxObj)
        while j > len(föremål.items_pos):
            i = random.randint(1, 100)
            if random.randint(0, 10) == 0:
                if not i == player.pos and not i in föremål.items_pos:
                    k = random.choice(["a", "b", "c", "d"])
                    föremål.Placera(k, i)
    def PlaceraMonster(self):
        j = random.randint(self.minMon, self.maxMon)
        while len(self.monsters) < j:
            i = random.randint(1, 100)
            if not i == player.pos and not i in föremål.items_pos and not i in self.monsters:
                typ = random.choice(["Zombie", "Spöke", "Drake"])
                str = random.randint(5, 20)
                nyaMonster = Monster(typ, str, i)
                self.monsters.append(nyaMonster)


                

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)
running = True

player = player(10, 0, 1, 0, 45, [])
karta = Karta(10, 10)
föremål = föremål()

#meny
menyVal = ""
menyValIndex = 0
menyValValIndex = 0
gameState = 0 #0: vanlig meny, 1:när du är i en fight
harTryckt = False

fightGrej = 0
fightGrejHåll = 1
fightPause = False
fightDelay = 50
fade = 0
fightTimer = 5

#text-rendering
text_index = 0
texts = []
texts_pos = []
priorityIndex = 1
skriver = False

#spelaren
stårVidItem = False
stårVidItem_Item = ""
stårVidItem_Index = 0
skippaItem = False

def DrawText(text, textSpeed, charIndex, x, y, priority):
    #använd inte for-loopar här!!!(fryser programmet) 
    global visadText
    global textSplit
    global text_index
    global priorityIndex
    global skriver
    skriver = True
    if priority == priorityIndex:
        if not text in texts:
            if charIndex <= len(text):
                if charIndex == 0:
                    visadText = ""
                    textSplit = list(text)
                if charIndex < len(text):
                    visadText += textSplit[0]
                    textSurface = font.render(visadText, True, "white")
                    textRect = textSurface.get_rect()
                    textRect.topleft = (x,y)
                    screen.blit(textSurface, textRect)
                    textSplit.pop(0)
                    sleep(textSpeed)
                else:
                    texts.append(text)
                    texts_pos.append((x,y))
                    text_index = 0
                    priorityIndex += 1
                    skriver = False

def PrintText(text, x, y):
    texts.append(text)
    texts_pos.append((x,y))

def draw_ui():
    if gameState == 0:
        #menyval
        if menyVal == "Gå":
            ClearText("allt")
            pygame.draw.rect(screen, (40, 40, 40), (200, 420+5+4, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 420+5+5+4, 860-10, 200-10))

            p_y = (player.pos % karta.w)+1
            p_x = (player.pos // karta.w)+1
            #rita vald grej liksom
            if menyValValIndex == 0:#norr
                pygame.draw.rect(screen, (40, 40, 40), (570-15, 450-8, 110, 60), 0, 5)
            elif menyValValIndex == 1:#syd
                pygame.draw.rect(screen, (40, 40, 40), (570-15, 560-8, 110, 60), 0, 5)
            elif menyValValIndex == 2:#väst
                pygame.draw.rect(screen, (40, 40, 40), (370-15, 500-8, 110, 60), 0, 5)
            else:# öst
                pygame.draw.rect(screen, (40, 40, 40), (770-15, 500-8, 110, 60), 0, 5)

            if p_y == 1:
                PrintText("Norr(nix)", 50, 450)
            else:
                PrintText("Norr", 570, 440+8)
            if p_y == 10:
                PrintText("Syd(nix)", 750, 450)
            else:
                PrintText("Syd", 570, 560)
            if p_x == 1:
                PrintText("Väst(nix)", 250, 550)
            else:
                PrintText("Väst", 370, 500)
            if p_x == 10:
                PrintText("Öst(nix)", 750, 550)
            else:
                PrintText("Öst", 770, 500)
            #DrawText("Norr", 0.05, text_index, 250, 350, 1)
            #DrawText("Syd", 0.05, text_index, 750, 350, 2)
            #DrawText("Väst", 0.05, text_index, 250, 450, 3)
            #DrawText("Öst", 0.05, text_index, 750, 450, 4)

        elif menyVal == "Inventory":
            pygame.draw.rect(screen, (40, 40, 40), (200, 420+5+4, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 420+5+4+5, 860-10, 200-10))
            j=0
            k=0
            for i in range(len(player.inventory)):
                PrintText(str(player.inventory[i]), 250+(280*j), 440+5+4+(60*k))
                j+=1
                if j == 3:
                    k+=1
                    j=0
            j=0
            k=0
        elif menyVal == "Stats":
            pygame.draw.rect(screen, (40, 40, 40), (200, 420+5+4, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 420+5+5+4, 860-10, 200-10))
            PrintText(f"x, y: {(player.pos % karta.w)+1}, {(player.pos // karta.w)+1}", 230, 450)
            PrintText(f"rum: {player.pos}", 230, 500)
            PrintText(f"str: {player.str}", 230, 550)
            PrintText(f"lvl: {player.lvl}", 530, 450)
            PrintText(f"skill: {player.skill}", 530, 500)
            PrintText(f"hp: {player.hp}", 530, 550)
        elif menyVal == " ":
            pygame.draw.rect(screen, (40, 40, 40), (200, 420+5+4, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 420+5+5+4, 860-10, 200-10))
        elif not menyVal == "VidItem":
            for i in range(4):
                pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 550, 200, 80))
                #göra outline för alla boxar förutom den man kollar på så att säga
                if not menyValIndex == i:
                    pygame.draw.rect(screen, (10, 10, 10), (200+(220*i)+5, 550+5, 200-10, 80-10))
        
            PrintText("Gå", 200+25, 567)
            PrintText("Inventory", 440, 567)
            PrintText("Stats", 660+25, 567)
            PrintText(" ", 880+25, 567)
    elif gameState == 1:#i fight
        
        if menyVal == "Fight":
            pygame.draw.rect(screen, (max(40+fade, 0), max(40+fade, 0), max(40+fade,0)), (200, 420+5+4, 860, 200))
            pygame.draw.rect(screen, (max(10+fade, 0), max(10+fade, 0), max(10+fade,0)), (200+5, 420+5+5+4, 860-10, 200-10))
            pygame.draw.rect(screen, (max(40+fade, 0), max(40+fade, 0), max(40+fade,0)), (450, 420+5+4, 360, 200))
            pygame.draw.rect(screen, (max(60+fade, 0), max(60+fade, 0), max(60+fade,0)), (550, 420+5+4, 160, 200))
            pygame.draw.rect(screen, (max(80+fade, 0), max(80+fade, 0), max(80+fade,0)), (600, 420+5+4, 60, 200))
            #fight grej
            pygame.draw.rect(screen, (max(250+fade, 0), max(250+fade, 0), max(250+fade,0)), (210+fightGrej, 420+5+4, 20, 200))

        elif menyVal == "Interagera":
            pygame.draw.rect(screen, (40, 40, 40), (200, 420+5+4, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 420+5+4+5, 860-10, 200-10))
            j=0
            k=0
            for i in player.inventory:#monster.interaktioner?
                    PrintText(str(i), 250+(280*j), 440+5+4+(60*k))
                    
                    j+=1
                    if j == 3:
                        k+=1
                        j=0
            j=0
            k=0
        elif menyVal == "Inventory":
            pygame.draw.rect(screen, (40, 40, 40), (200, 420+5+4, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 420+5+4+5, 860-10, 200-10))

            j=0
            k=0
            for i in player.inventory:
                    PrintText(str(i), 250+(280*j), 440+5+4+(60*k))
                    
                    j+=1
                    if j == 3:
                        k+=1
                        j=0
            j=0
            k=0
        elif menyVal == "Fly":
            pass
        elif not menyVal == "VidItem":
            for i in range(4):
                pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 550, 200, 80))
                #göra outline för alla boxar förutom den man kollar på så att säga
                if not menyValIndex == i:
                    pygame.draw.rect(screen, (10, 10, 10), (200+(220*i)+5, 550+5, 200-10, 80-10))
        
            PrintText("Fight", 200+25, 567)
            PrintText("Interagera", 437, 567)
            PrintText("Inventory", 660, 567)
            PrintText("Fly", 880+25, 567)


    if menyVal == "VidItem":
        for i in range(2):
            pygame.draw.rect(screen, (80, 80, 80), (400+(260*i), 550, 230, 80))
            #göra outline för alla boxar förutom den man kollar på så att säga
            if not menyValIndex == i:
                pygame.draw.rect(screen, (10, 10, 10), (400+(260*i)+5, 550+5, 230-10, 80-10))
        DrawText("Plocka Upp", 0.05, text_index, 410, 567, 2)
        DrawText("Lämna", 0.05, text_index, 680, 567, 3)

    k = 0
    for i in range(karta.w):
        for j in range(karta.h):
            pygame.draw.rect(screen, (40, 40, 40), (i*11+1160, j*11+10, 10, 10))
            for h in föremål.items_pos:
                if k == h:
                    pygame.draw.rect(screen, (240, 0, 0), (i*11+1160, j*11+10, 10, 10))
            for l in range(len(karta.monsters)):
                if k == karta.monsters[l].cords:
                    if karta.monsters[l].typ == "Zombie":
                        pygame.draw.rect(screen, (0, 240, 0), (i*11+1160, j*11+10, 10, 10))
                    elif karta.monsters[l].typ == "Spöke":
                        pygame.draw.rect(screen, (0, 0, 240), (i*11+1160, j*11+10, 10, 10))
                    elif karta.monsters[l].typ == "Drake":
                        pygame.draw.rect(screen, (240, 240, 0), (i*11+1160, j*11+10, 10, 10))

            if k == player.pos:
                pygame.draw.rect(screen, (240, 240, 240), (i*11+1160, j*11+10, 10, 10))
            
            k+=1

def ClearText(text):
    if text == "allt":
        for i in range(len(texts)):
            texts.pop()
            texts_pos.pop()
    if text == "menyer":
        for i in texts:
            if i == "Gå" or i == "Inventory" or i == "Stats" or i == "Fight" or i == "Interagera" or i == "Fly":
                j = texts.index(i)
                texts.pop(j)
                texts_pos.pop(j)
    elif text in texts:
        i = texts.index(text)
        texts.pop(i)
        texts_pos.pop(i)

def Start():#körs en gång i början
    karta.PlaceraFöremål()
    karta.PlaceraMonster()

Start()
while running:
    ClearText("menyer")
    screen.fill((10, 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_LEFT:
                if menyVal == "" or menyVal == "VidItem":
                    if not menyValIndex == 0:
                        menyValIndex -= 1
                if menyVal == "Gå":
                    menyValValIndex = 2

            if event.key == pygame.K_RIGHT:
                if menyVal == "":
                    if not menyValIndex == 3:
                        menyValIndex += 1
                elif menyVal == "VidItem":
                    if not menyValIndex == 1:
                        menyValIndex += 1
                if menyVal == "Gå":
                    menyValValIndex = 3

            if event.key == pygame.K_DOWN:
                if menyVal == "Gå":
                    menyValValIndex = 1

            if event.key == pygame.K_UP:
                if menyVal == "Gå":
                    menyValValIndex = 0

            if event.key == pygame.K_RETURN:
                ClearText("allt")
                if not harTryckt:
                    if menyVal == "Fight":
                        fightPause = True
                        if fightGrej >= 600-210-10 and fightGrej <= 600+60-210-10:
                            PrintText("+30", 500, 200)           #pos+bredd-offset-1/2 bredd
                        elif fightGrej >= 550-210-10 and fightGrej <= 550+160-210-10:
                            PrintText("+20", 500, 200)
                                        #pos-offset+1/2 bredd
                        elif fightGrej >= 450-210-10 and fightGrej <= 450+360-210-10:
                            PrintText("+10", 500, 200)
                        else:
                            PrintText("+0", 500, 200)
                if not harTryckt:
                    if menyVal == "Gå":
                        skippaItem = False
                        p_y = (player.pos % karta.w)+1
                        p_x = (player.pos // karta.w)+1
                        if menyValValIndex == 0:
                            if not p_y == 1:
                                player.Move("Norr")
                        elif menyValValIndex == 1:
                            if not p_y == 10:
                                player.Move("Syd")
                        elif menyValValIndex == 2:
                            if not p_x == 1:
                                player.Move("Öst")
                        else:
                            if not p_x == 10:
                                player.Move("Väst")
                        ClearText("allt")
                        priorityIndex = 1
                        menyValValIndex = 0
                        menyVal = ""
                        fightPause = False
                        harTryckt = True
                    elif menyVal == "VidItem":
                        
                        if menyValIndex == 0:
                            if len(player.inventory) == player.maxItems:
                                pass
                                #----------------------------------------------------LÄGG TILL - droppa eget föremål för att byta ut
                            player.Pickup(stårVidItem_Item)
                            i = föremål.items_pos.index(stårVidItem_Index)
                            föremål.items.pop(i)
                            föremål.items_pos.pop(i)
                            ClearText("allt")
                            priorityIndex = 1
                            menyValValIndex = 0
                            menyValIndex = 0
                            menyVal = ""
                            harTryckt = True
                            stårVidItem_Index = 0
                            stårVidItem = False
                            stårVidItem_Item = ""
                            skippaItem = True
                        elif menyValIndex == 1:
                            ClearText("allt")
                            priorityIndex = 1
                            menyValValIndex = 0
                            menyValIndex = 0
                            menyVal = ""
                            harTryckt = True
                            stårVidItem_Index = 0
                            stårVidItem = False
                            stårVidItem_Item = ""
                            skippaItem = True

                if not harTryckt:
                    if gameState == 0:
                        #kolla vad man väljer i menyn
                        if menyValIndex == 0:
                            text_index=0
                            menyVal = "Gå"
                        elif menyValIndex == 1:
                            text_index=0
                            menyVal = "Inventory"
                        elif menyValIndex == 2:
                            text_index=0
                            menyVal = "Stats"
                        else:
                            text_index=0
                            menyVal = " "
                    elif gameState == 1:
                        if menyValIndex == 0:
                            text_index = 0
                            menyVal = "Fight"
                            if not fightPause:
                                fightGrej = 0
                        elif menyValIndex == 1:
                            text_index = 0
                            menyVal = "Interagera"
                        elif menyValIndex == 2:
                            text_index = 0
                            menyVal = "Inventory"
                        elif menyValIndex == 3:
                            text_index = 0
                            menyVal = "Fly"
                        else:
                            text_index = 0
                            menyVal = " "
                if not harTryckt:
                    if menyVal == " ":
                        gameState = 1
                        ClearText("allt")
                    elif menyVal == "Fly":
                        gameState = 0
                        ClearText("allt")

            if event.key == pygame.K_BACKSPACE:
                ClearText("allt")
                priorityIndex = 1
                menyValValIndex = 0
                menyVal = ""
                fightPause = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                harTryckt = False

    if not skippaItem:
        for i,j in zip(föremål.items, föremål.items_pos):
            if player.pos == j:
                stårVidItem_Index = j
            if player.pos == stårVidItem_Index:
                stårVidItem = True
                stårVidItem_Item = i
            else:
                stårVidItem_Item = ""
                stårVidItem = False
                stårVidItem_Index = 0
        if stårVidItem:
            menyVal = "VidItem"
            if stårVidItem_Item == "a" or stårVidItem_Item == "c":
                DrawText(f"Du ser ett {stårVidItem_Item}", 0.05, text_index, 400, 300, 1)
            elif stårVidItem_Item == "b" or stårVidItem_Item == "d":
                DrawText(f"Du ser en {stårVidItem_Item}", 0.05, text_index, 400, 300, 1)
    
    draw_ui()

    for txt, txt_pos in zip(texts, texts_pos):
        textSurface = font.render(txt, True, "white")
        textRect = textSurface.get_rect()
        textRect.topleft = txt_pos
        screen.blit(textSurface, textRect)
    if skriver:
        text_index += 1
    if not fightPause:
        fightGrej += 7*fightGrejHåll
    if fightGrej > 825:
        fightGrejHåll = -1
    elif fightGrej < 0:
        fightGrejHåll = 1

    if fightPause == True:
        fightDelay -= 1
        fade -= 0.5
    if fightDelay == 0:
        fightPause = False
        ClearText("allt")
        priorityIndex = 1
        menyValValIndex = 0
        menyVal = ""
        fightDelay = 50
        fade = 0
    
    pygame.display.flip()
    clock.tick(120)

pygame.quit()