import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.display.flip()#uppdatera skärmen
    clock.tick(60)#60fps

pygame.quit()

if __name__ == "__main__":
    pass