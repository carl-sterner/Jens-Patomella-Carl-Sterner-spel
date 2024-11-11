import pygame

class Text:
    def __init__(self, screen, font, text_color="white", bg_color="black", text_speed=0.2):
        self.screen = screen
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.text_speed = text_speed
        self.index = 0
        self.pause_duration = 0
        self.text_displayed = ""
    
    def uppdatera_text(self, text, dt):
        #ta bort paus efter . och ,
        if self.pause_duration > 0:
            self.pause_duration -= dt
        else:
            if self.index < len(text):
                current_char = text[int(self.index)]
                self.text_displayed = text[:int(self.index) + 1]
                
                #gör en liten paus om ett komma eller punkt kommer i texten
                if current_char == ".":
                    self.pause_duration = 0.5
                elif current_char == ".":
                    self.pause_duration = 0.25
                #annars, så fortsätter koden
                else:
                    self.index += self.text_speed
                
                if current_char in ".,":
                    self.index += self.text_speed
    
    def draw(self):
        self.screen.fill(self.bg_color)

        text_surface = self.font.render(self.text_displayed, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2))
        self.screen.blit(text_surface, text_rect)

    def skriv_text(self, text, clock):
        running = True
        while running:
            dt = clock.get_time() / 1000
            self.uppdatera_text(text, dt)
            
            self.draw()

            if len(self.text_displayed) == len(text):
                running = False

            pygame.display.flip()
            clock.tick(60)