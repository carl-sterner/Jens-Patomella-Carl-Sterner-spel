import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 48)
running = True

selected_index = 0

#text-rendering
text_index = 0
texts = []
texts_pos = []
priorityIndex = 1

def draw_ui():
    for i in range(4):
        pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 520, 200, 100))
        #göra outline för alla boxar förutom den man kollar på så att säga
        if not selected_index == i:
            pygame.draw.rect(screen, (10, 10, 10), (200+(220*i)+5, 520+5, 200-10, 100-10))

def DrawText(text, textSpeed, charIndex, x, y, priority):
    #använd inte for-loopar här!!!(fryser programmet) 
    global dt
    global textSplit
    global text_index
    global priorityIndex
    if priority == priorityIndex:
        if not text in texts:
            if charIndex <= len(text):
                if charIndex == 0:
                    dt = ""
                    textSplit = list(text)

                if charIndex < len(text):
                    dt += textSplit[0]
                    textSurface = font.render(dt, True, "white")
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not selected_index == 0:
                    selected_index -= 1
            if event.key == pygame.K_RIGHT:
                if not selected_index == 3:
                    selected_index += 1

    screen.fill((10, 10, 10))
    draw_ui()
    
    DrawText("ei ei ei", 0.1, text_index, 400, 200, 1)
    DrawText("estoy de vacaciones", 0.1, text_index, 400, 240, 2)

    for txt, txt_pos in zip(texts, texts_pos):
        textSurface = font.render(txt, True, "white")
        textRect = textSurface.get_rect()
        textRect.topleft = txt_pos
        screen.blit(textSurface, textRect)

    pygame.display.flip()

    clock.tick(60)
    text_index += 1

pygame.quit()