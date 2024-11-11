import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
running = True

selected_index = 0

def draw_ui():
    for i in range(4):
        pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 520, 200, 100))
        text = font.render("hejhej", True, "white")
        textRect = text.get_rect()
        screen.blit(text, (textRect.x+1000, textRect.y, textRect.width, textRect.height))
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

    pygame.display.flip()

    clock.tick(60)

pygame.quit()