import pygame
from time import sleep
from entities import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)
running = True

player = player()

#meny
menyVal = ""
menyValIndex = 0
menyValValIndex = 0
gameState = 0 #0: vanlig meny, 1:när du är mot monster, osv

fightGrej = 0
fightGrejHåll = 1
fightPause = False
fightDelay = 50
fade = 0

#text-rendering
text_index = 0
texts = []
texts_pos = []
priorityIndex = 1

def DrawText(text, textSpeed, charIndex, x, y, priority):
    #använd inte for-loopar här!!!(fryser programmet) 
    global visadText
    global textSplit
    global text_index
    global priorityIndex
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

def PrintText(text, x, y):
    if not text in texts:
        texts.append(text)
        texts_pos.append((x,y))

def draw_ui():
    if gameState == 0:
        for i in range(4):
            pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 550, 200, 80))
            #göra outline för alla boxar förutom den man kollar på så att säga
            if not menyValIndex == i:
                pygame.draw.rect(screen, (10, 10, 10), (200+(220*i)+5, 550+5, 200-10, 80-10))
        #menyval
        if menyVal == "Gå":
            pygame.draw.rect(screen, (40, 40, 40), (200, 320, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 320+5, 860-10, 200-10))

            #rita vald grej liksom
            if menyValValIndex == 0:
                pygame.draw.rect(screen, (40, 40, 40), (235, 340, 110, 60))
            elif menyValValIndex == 1:
                pygame.draw.rect(screen, (40, 40, 40), (235+500, 340, 110, 60))
            elif menyValValIndex == 2:
                pygame.draw.rect(screen, (40, 40, 40), (235, 340+100, 110, 60))
            else:
                pygame.draw.rect(screen, (40, 40, 40), (235+500, 340+100, 110, 60))
            #PrintText("Norr", 250, 350)
            #PrintText("Syd", 750, 350)
            #PrintText("Öst", 250, 450)
            #PrintText("Väst", 750, 450)
            DrawText("Norr", 0.05, text_index, 250, 350, 1)
            DrawText("Syd", 0.05, text_index, 750, 350, 2)
            DrawText("Öst", 0.05, text_index, 250, 450, 3)
            DrawText("Väst", 0.05, text_index, 750, 450, 4)
        elif menyVal == "Inventory":
            pygame.draw.rect(screen, (40, 40, 40), (200, 320, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 320+5, 860-10, 200-10))
        elif menyVal == "Stats":
            pygame.draw.rect(screen, (40, 40, 40), (200, 320, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 320+5, 860-10, 200-10))
            #DrawText("x, y: ", 0.01, text_index, 230, 350, 1)
            #DrawText("  ", 0.01, text_index, 250, 350, 2)
            #DrawText("rum: ", 0.01, text_index, 230, 400, 3)
            #DrawText("   ", 0.01, text_index, 250, 400, 4)
            #DrawText("str: ", 0.01, text_index, 230, 450, 5)
            #DrawText("    ", 0.01, text_index, 250, 450, 6)
            #DrawText("lvl: ", 0.01, text_index, 530, 350, 7)
            #DrawText("     ", 0.01, text_index, 550, 350, 8)
            #DrawText("luck: ", 0.01, text_index, 530, 400, 9)
            #DrawText("      ", 0.01, text_index, 550, 400, 10)

            PrintText("x, y: ", 230, 350)
            PrintText("  ", 250, 350)
            PrintText("rum: ", 230, 400)
            PrintText("   ", 250, 400)
            PrintText("str: ", 230, 450)
            PrintText("    ", 250, 450)
            PrintText("lvl: ", 530, 350)
            PrintText("     ", 550, 350)
            PrintText("luck: ", 530, 400)
            PrintText("      ", 550, 400)
        elif menyVal == " ":
            pygame.draw.rect(screen, (40, 40, 40), (200, 320, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 320+5, 860-10, 200-10))
    elif gameState == 1:#i fight
        for i in range(4):
            pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 550, 200, 80))
            #göra outline för alla boxar förutom den man kollar på så att säga
            if not menyValIndex == i:
                pygame.draw.rect(screen, (10, 10, 10), (200+(220*i)+5, 550+5, 200-10, 80-10))
        if menyVal == "Fight":
            pygame.draw.rect(screen, (max(40+fade, 0), max(40+fade, 0), max(40+fade,0)), (200, 320, 860, 200))
            pygame.draw.rect(screen, (max(10+fade, 0), max(10+fade, 0), max(10+fade,0)), (200+5, 320+5, 860-10, 200-10))
            pygame.draw.rect(screen, (max(40+fade, 0), max(40+fade, 0), max(40+fade,0)), (450, 320, 360, 200))
            pygame.draw.rect(screen, (max(60+fade, 0), max(60+fade, 0), max(60+fade,0)), (550, 320, 160, 200))
            pygame.draw.rect(screen, (max(80+fade, 0), max(80+fade, 0), max(80+fade,0)), (600, 320, 60, 200))
            #fight grej
            pygame.draw.rect(screen, (max(250+fade, 0), max(250+fade, 0), max(250+fade,0)), (210+fightGrej, 320, 20, 200))

        elif menyVal == "Interagera":
            pygame.draw.rect(screen, (40, 40, 40), (200, 320, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 320+5, 860-10, 200-10))
        elif menyVal == "Inventory":
            pygame.draw.rect(screen, (40, 40, 40), (200, 320, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 320+5, 860-10, 200-10))
        elif menyVal == "Fly":
            pass
        
def ClearText(text):
    if text == "allt":
        for i in range(len(texts)):
            texts.pop()
            texts_pos.pop()
    if text in texts:
        i = texts.index(text)
        texts.pop(i)
        texts_pos.pop(i)

while running:
    screen.fill((10, 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_LEFT:
                if menyVal == "":
                    if not menyValIndex == 0:
                        menyValIndex -= 1
                if not menyVal == "":
                    if not menyValValIndex == 0:
                        menyValValIndex -= 1

            if event.key == pygame.K_RIGHT:
                if menyVal == "":
                    if not menyValIndex == 3:
                        menyValIndex += 1
                if not menyVal == "":
                    if not menyValValIndex == 3:
                        menyValValIndex += 1

            if event.key == pygame.K_DOWN:
                if not menyVal == "":
                    if not menyValValIndex >= 2:
                        menyValValIndex += 2

            if event.key == pygame.K_UP:
                if not menyVal == "":
                    if not menyValValIndex < 2:
                        menyValValIndex -= 2

            if event.key == pygame.K_RETURN:
                if menyVal == "Fight":
                    fightPause = True
                    if fightGrej >= 600-210+10 and fightGrej <= 600+60-210+10:
                        PrintText("+30", 500, 200)              #pos+bredd-offset+1/2 bredd
                    elif fightGrej >= 550-210+10 and fightGrej <= 550+160-210+10:
                        PrintText("+20", 500, 200)
                                    #pos-offset+1/2 bredd
                    elif fightGrej >= 450-210+10 and fightGrej <= 450+360-210+10:
                        PrintText("+10", 500, 200)
                if menyVal == "Gå":
                    if menyValValIndex == 0:
                        print("Norr")
                    elif menyValValIndex == 1:
                        print("Syd")
                    elif menyValValIndex == 2:
                        print("Väst")
                    else:
                        print("Öst")
                if gameState == 0:
                    #kolla om man väljer "Gå" i menyn
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

    draw_ui()
    if gameState == 0:
        PrintText("Gå", 200+25, 567)
        PrintText("Inventory", 430+25, 567)
        PrintText("Stats", 660+25, 567)
        PrintText(" ", 880+25, 567)
    elif gameState == 1:
        PrintText("Fight", 200+25, 567)
        PrintText("Interagera", 437, 567)
        PrintText("Inventory", 660, 567)
        PrintText("Fly", 880+25, 567)
    
    for txt, txt_pos in zip(texts, texts_pos):
        textSurface = font.render(txt, True, "white")
        textRect = textSurface.get_rect()
        textRect.topleft = txt_pos
        screen.blit(textSurface, textRect)

    pygame.display.flip()

    clock.tick(120)
    text_index += 1
    if not fightPause:
        fightGrej += 7*fightGrejHåll
    if fightGrej > 830:
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

pygame.quit()