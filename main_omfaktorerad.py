import pygame
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
    
    def PlaceraFöremål(self):
        j = random.randint(self.minObj, self.maxObj)
        while j > len(föremål.items_pos):
            i = random.randint(1, 100)
            if random.randint(0, 10) == 0:
                if not i == player.pos and not i in föremål.items_pos:
                    k = random.choice(["Svärd", "Sköld", "Svamp", "Potion"])
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

class F:
    @staticmethod
    def PrintText(screen, font, text, x, y, textObjekt):
        text_surface = font.render(text, True, "white")
        text_rect = text_surface.get_rect(topleft=(x, y))
        screen.blit(text_surface, text_rect)
        textObjekt.append((text, x, y))
        
    @staticmethod
    def ClearText(textObjekt):
        textObjekt.clear()

    @staticmethod#jeh
    def CheckForItems():
        global gameState
        for itemPos in föremål.items_pos:
            if itemPos == player.pos:
                    gameState = 2
    
    @staticmethod
    def CheckForMonsters():
        global gameState, menyVal
        for i in range(len(karta.monsters)):
            if karta.monsters[i].cords == player.pos:
                gameState = 1
                menyVal = 5
                return karta.monsters[i]

#globala variabler
gameState = 0
menyVal = 0
#menyVal 0 = när man ser val 1-4
#menyVal 1 = gå-meny
#menyVal 2 = inventory-meny
#menyVal 3 = stats-meny
#menyVal 4 = obestämt
#menyVal 5(gamestate 1) = när man ser val 6-9
#menyVal 6(gamestate 1) = fight grej
#menyVal 7(gamestate 1) = inventory-meny
#menyVal 8(gamestate 1) = obestämt
#menyVal 9(gamestate 1) = fly från fight
#menyVal 11 = du står vid item
subMenyVal = 0
#tex när du är i menyVal 1 så är subMenyVal 0 = Norr, 1 = Syd osv

#variabler för när du är i en fight
fightBoxen = 0 #själva offsetten för boxen
fightBoxHåll = 1

#Skapa objekt
player = player(10, 0, 1, 0, 45, [])
karta = Karta(10, 10)
föremål = föremål()

class UI:
    @staticmethod
    def DrawMinimap(screen):
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

    @staticmethod
    def DrawUI(screen, font, textObjekt):
        UI.DrawMinimap(screen)
        #gamestate 1 är här
        if gameState == 1:
            if menyVal == 5:
                for i in range(4):
                    pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 550, 200, 80))
                    #göra outline för alla boxar förutom den man kollar på så att säga
                    if not subMenyVal == i:
                        pygame.draw.rect(screen, (10, 10, 10), (205+(220*i), 555, 190, 70))
                F.PrintText(screen, font, "Fight", 225, 567, textObjekt)
                F.PrintText(screen, font, "Inventory", 437, 567, textObjekt)
                F.PrintText(screen, font, "Stats", 660, 567, textObjekt)
                F.PrintText(screen, font, "Fly", 880, 567, textObjekt)
                F.PrintText(screen, font, )
                return
            if menyVal == 6:
                #när du är i en fight så kommer dethär ritas till skärmen
                pygame.draw.rect(screen, (40, 40, 40), (200, 429, 860, 200))
                pygame.draw.rect(screen, (10, 10, 10), (205, 434, 850, 190))
                pygame.draw.rect(screen, (40, 40, 40), (450, 429, 360, 200))
                pygame.draw.rect(screen, (60, 60, 60), (550, 429, 160, 200))
                pygame.draw.rect(screen, (80, 80, 80), (600, 429, 60, 200))

                pygame.draw.rect(screen, (250, 250, 250), (210+fightBoxen, 429, 20, 200))
                return
            
            if menyVal == 7:
                #rita box, obestämt
                pygame.draw.rect(screen, (40, 40, 40), (200, 420+5+4, 860, 200))
                pygame.draw.rect(screen, (10, 10, 10), (200+5, 420+5+5+4, 860-10, 200-10))
                return
            
            if menyVal == 8:
                #rita själva boxen
                pygame.draw.rect(screen, (40, 40, 40), (200, 429, 860, 200))
                pygame.draw.rect(screen, (10, 10, 10), (205, 434, 850, 190))
                
                #allt under här är för att räkna x,y offset(samt text) för de olika grejerna man har i inventory
                x=0
                y=0
                for i in range(len(player.inventory)):
                    F.PrintText(screen, font, str(player.inventory[i]), 250+(280*x), 449+(60*y), textObjekt)
                    x+=1
                    if x == 3:
                        y+=1
                        x=0
                x=0
                y=0
                return
            if menyVal == 9:
                pass
                return
            if menyVal == 10:
                pass
                return
            return
        #gameState 0 här under
        if menyVal == 0:
            for i in range(4):
                pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 550, 200, 80))
                #göra outline för alla boxar förutom den man kollar på så att säga
                if not subMenyVal == i:
                    pygame.draw.rect(screen, (10, 10, 10), (205+(220*i), 555, 190, 70))
        
            F.PrintText(screen, font, "Gå", 225, 567, textObjekt)
            F.PrintText(screen, font, "Inventory", 437, 567, textObjekt)
            F.PrintText(screen, font, "Stats", 660, 567, textObjekt)
            F.PrintText(screen, font, "Obestämt", 880, 567, textObjekt)
            return

        if menyVal == 1:
            #rita själva boxen
            pygame.draw.rect(screen, (40, 40, 40), (200, 429, 860, 200), 0, 0)
            pygame.draw.rect(screen, (10, 10, 10), (205, 434, 850, 190), 0, 0)

            p_y = (player.pos % karta.w)+1 # din y position
            p_x = (player.pos // karta.w)+1 # din x position

            #rita vald grej liksom
            if subMenyVal == 0:#norr
                pygame.draw.rect(screen, (40, 40, 40), (555, 442, 110, 60), 0, 10)
            elif subMenyVal == 1:#syd
                pygame.draw.rect(screen, (40, 40, 40), (555, 552, 110, 60), 0, 10)
            elif subMenyVal == 2:#väst
                pygame.draw.rect(screen, (40, 40, 40), (355, 492, 110, 60), 0, 10)
            else:# öst
                pygame.draw.rect(screen, (40, 40, 40), (755, 492, 110, 60), 0, 10)

            if not p_y == 1:
                F.PrintText(screen, font, "Norr", 570, 448, textObjekt)
            if not p_y == 10:
                F.PrintText(screen, font, "Syd", 570, 560, textObjekt)
            if not p_x == 1:
                F.PrintText(screen, font, "Väst", 370, 500, textObjekt)
            if not p_x == 10:
                F.PrintText(screen, font, "Öst", 770, 500, textObjekt)
            return

        if menyVal == 2:
            #rita själva boxen
            pygame.draw.rect(screen, (40, 40, 40), (200, 429, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (205, 434, 850, 190))
            
            #allt under här är för att räkna x,y offset(samt text) för de olika grejerna man har i inventory
            x=0
            y=0
            for i in range(len(player.inventory)):
                F.PrintText(screen, font, str(player.inventory[i]), 250+(280*x), 449+(60*y), textObjekt)
                x+=1
                if x == 3:
                    y+=1
                    x=0
            x=0
            y=0
            return
        
        if menyVal == 3:
            #rita box och stats
            pygame.draw.rect(screen, (40, 40, 40), (200, 429, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (205, 434, 850, 190))
            F.PrintText(screen, font, f"x, y: {(player.pos % karta.w)+1}, {(player.pos // karta.w)+1}", 230, 450, textObjekt)
            F.PrintText(screen, font, f"rum: {player.pos}", 230, 500, textObjekt)
            F.PrintText(screen, font, f"str: {player.str}", 230, 550, textObjekt)
            F.PrintText(screen, font, f"lvl: {player.lvl}", 530, 450, textObjekt)
            F.PrintText(screen, font, f"skill: {player.skill}", 530, 500, textObjekt)
            F.PrintText(screen, font, f"hp: {player.hp}", 530, 550, textObjekt)
            return
        
        if menyVal == 4:
            #rita box, obestämt
            pygame.draw.rect(screen, (40, 40, 40), (200, 420+5+4, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (200+5, 420+5+5+4, 860-10, 200-10))
            return
        
        if menyVal == 11:
            F.PrintText(screen, font, "Du står vid en item", 400, 300, textObjekt)

            for i in range(2):
                pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 550, 200, 80))
                #göra outline för alla boxar förutom den man kollar på så att säga
                if not subMenyVal == i:
                    pygame.draw.rect(screen, (10, 10, 10), (205+(220*i), 555, 190, 70))
class Input:
    @staticmethod
    def Upp():
        global menyVal, subMenyVal
        if menyVal == 1:
            subMenyVal = 0 
    
    @staticmethod
    def Ner():
        global menyVal, subMenyVal
        if menyVal == 1:
            subMenyVal = 1

    @staticmethod
    def Höger():
        global menyVal, subMenyVal
        if menyVal == 0 or menyVal == 5:
            if subMenyVal != 3:
                subMenyVal += 1
            
        elif menyVal == 1:
            subMenyVal = 3

    @staticmethod
    def Vänster():
        global menyVal, subMenyVal
        if menyVal == 0 or menyVal == 5:
            if subMenyVal != 0:
                subMenyVal -= 1
        elif menyVal == 1:
            subMenyVal = 2

    @staticmethod
    def Enter():
        global menyVal, subMenyVal, gameState
        if menyVal == 0:
            if subMenyVal == 0: #om man tryckt på "Gå"
                menyVal = 1
            elif subMenyVal == 1: #om man tryckt på "Inventory"
                menyVal = 2
            elif subMenyVal == 2: #om man tryckt på "Stats"
                menyVal = 3
            elif subMenyVal == 3: #om man tryckt på "Ombestämt"
                menyVal = 4
            subMenyVal = 0
            return
        
        if menyVal == 5:
            if subMenyVal == 0: #om man tryckt på "Fight"
                menyVal = 6
            elif subMenyVal == 1: #om man tryckt på "Inventory"
                menyVal = 2
            elif subMenyVal == 2: #om man tryckt på "Stats"
                menyVal = 3
            elif subMenyVal == 3: #om man tryckt på "Fly"
                menyVal = 9
            subMenyVal = 0
            return

        if menyVal == 1:
            if subMenyVal == 0:
                player.Move("Norr")
            if subMenyVal == 1:
                player.Move("Syd")
            if subMenyVal == 2:
                player.Move("Öst")
            if subMenyVal == 3:
                player.Move("Väst")
        
            #kolla om gubben är i samma ruta som föremål eller monster
            for itemPos in föremål.items_pos:
                if itemPos == player.pos:
                    print("djfaodsjfio")
            
            for i in range(len(karta.monsters)):
                print("fkdafljasdlkfjasldkfjasdlkfj")
                if karta.monsters[i].cords == player.pos:
                    gameState = 1
                    menyVal = 5
                    print("d")

    @staticmethod
    def Tillbaka():
        global menyVal, subMenyVal
        if gameState == 0:
            menyVal = 0
            subMenyVal = 0
        elif gameState == 1:
            subMenyVal = 0
            menyVal = 5
            
class Spel:
    def __init__(self):
        #spel variabler
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 36)

        #textvariabler
        self.textObjekter = [] #håller koll på de texterna som ska ritas

    def Input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                    return

                if event.key == pygame.K_BACKSPACE:
                    Input.Tillbaka()
                    return

                if event.key == pygame.K_RETURN:
                    Input.Enter()
                    return

                if event.key == pygame.K_UP:
                    Input.Upp()
                    return
                
                if event.key == pygame.K_DOWN:
                    Input.Ner()
                    return

                if event.key == pygame.K_LEFT:
                    Input.Vänster()
                    return

                if event.key == pygame.K_RIGHT:
                    Input.Höger()
                    return

    def Rendera(self):
        #töm skärmen
        self.screen.fill((10, 10, 10))
        
        UI.DrawUI(self.screen, self.font, self.textObjekter)

        #uppdatera skärmen
        pygame.display.flip()
    
    def Uppdatera(self):
        global fightBoxHåll, fightBoxen
        if menyVal == 6: #om du är i fight
            #rörelse fram och tillbaka
            if fightBoxen > 825:
                fightBoxHåll = -1
            elif fightBoxen < 0:
                fightBoxHåll = 1
            fightBoxen += 7*fightBoxHåll

        
    def Kör(self):
        karta.PlaceraFöremål()
        karta.PlaceraMonster()
        while self.running:
            self.Input()
            self.Uppdatera()
            self.Rendera()
            self.clock.tick(120)

if __name__ == "__main__":
    spel = Spel()
    spel.Kör()