import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
running = True

selected_index = 0

text = "göra outline för alla boxar förutom den man kollar på så att säga"
drawn_text = ""
text_index = 0
text_split = list(text)
texts = []

def draw_ui():
    for i in range(4):
        pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 520, 200, 100))
        #göra outline för alla boxar förutom den man kollar på så att säga
        if not selected_index == i:
            pygame.draw.rect(screen, (10, 10, 10), (200+(220*i)+5, 520+5, 200-10, 100-10))

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
    #draw text
    
    if len(text_split) > 0:
        drawn_text += text_split[0]
        _ts = font.render(drawn_text, True, "white")
        _tr = _ts.get_rect()
        screen.blit(_ts, _tr)
        text_split.pop(0)
        sleep(0.1)
    else:
        if not text in texts:
            texts.append(text)
    for txt in texts:
        _ts = font.render(txt, True, "white")
        _tr = _ts.get_rect()
        screen.blit(_ts, _tr)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
