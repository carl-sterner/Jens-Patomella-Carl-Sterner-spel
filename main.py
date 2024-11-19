import pygame
from time import sleep
from entities import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)
running = True

#meny
menyVal = ""
menyValIndex = 0
menyValValIndex = 0
gameState = 0 #0: vanlig meny, 1:fight

fightGrej = 0
fightGrejHåll = 1
fightPause = False

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
            DrawText("x, y: ", 0.01, text_index, 230, 350, 1)
            DrawText("  ", 0.01, text_index, 250, 350, 2)
            DrawText("rum: ", 0.01, text_index, 230, 400, 3)
            DrawText("   ", 0.01, text_index, 250, 400, 4)
            DrawText("str: ", 0.01, text_index, 230, 450, 5)
            DrawText("    ", 0.01, text_index, 250, 450, 6)
            DrawText("lvl: ", 0.01, text_index, 530, 350, 7)
            DrawText("     ", 0.01, text_index, 550, 350, 8)
            DrawText("luck: ", 0.01, text_index, 530, 400, 9)
            DrawText("      ", 0.01, text_index, 550, 400, 10)
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
            pygame.draw.rect(screen, (40, 40, 40), (200, 320, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 320+5, 860-10, 200-10))

            #fight grej
            pygame.draw.rect(screen, (40, 40, 40), (210+fightGrej, 320, 20, 200))
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
                if menyVal == "Gå":
                    if menyValValIndex == 0:
                        print("Norr")
                    elif menyValValIndex == 1:
                        print("Syd")
                    elif menyValValIndex == 2:
                        print("Väst")
                    else:
                        print("Öst")
                #kolla om man väljer "Gå" i menyn
                if gameState == 0:
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
                elif menyVal == "Fight":
                    fightPause = True

            if event.key == pygame.K_BACKSPACE:
                ClearText("allt")
                priorityIndex = 1
                menyValValIndex = 0
                menyVal = ""
                fightPause = False


    draw_ui()
    print(menyVal)
    if gameState == 0:
        PrintText("Gå", 200+25, 560)
        PrintText("Inventory", 440+25, 560)
        PrintText("Stats", 660+25, 560)
        PrintText(" ", 880+25, 560)
    elif gameState == 1:
        PrintText("Fight", 200+25, 567)
        PrintText("Interagera", 440+25, 567)
        PrintText("Inventory", 660, 567)
        PrintText("Fly", 880+25, 567)
    
    for txt, txt_pos in zip(texts, texts_pos):
        textSurface = font.render(txt, True, "white")
        textRect = textSurface.get_rect()
        textRect.topleft = txt_pos
        screen.blit(textSurface, textRect)

    pygame.display.flip()

    clock.tick(60)
    text_index += 1
    if not fightPause:
        fightGrej += 6*fightGrejHåll
    if fightGrej > 830:
        fightGrejHåll = -1
    elif fightGrej < 0:
        fightGrejHåll = 1

pygame.quit()