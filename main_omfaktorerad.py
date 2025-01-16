import pygame
from entities import *
import random
import spara

class Karta():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.minObj = 12
        self.maxObj = 18
        self.items = []
        self.itemPos = []

        self.minMon = 12
        self.maxMon = 18
        self.monsters = []
        self.monsterPos = []

        self.minFäl = 6
        self.maxFäl = 13
        self.fällor = []
        self.fällorPos = []

    def PlaceraFöremål(self, data):
        if data != None:
            for item in data:
                nyItem = Föremål(item[0], item[1], item[2], item[3])
                self.items.append(nyItem)
                self.itemPos.append(item[2])
            return

        j = random.randint(self.minObj, self.maxObj)
        while len(self.items) < j:
            i = random.randint(0, 99)
            if not i == player.pos and not i in self.itemPos:
                typ = random.choice(["Äpple", "Svärd", "Potion"])
                container = random.choice(["buske", "kista", "grop"])
                strBonus = random.randint(1, 10)
                nyItem = Föremål(typ, strBonus, i, container)
                self.items.append(nyItem)
                self.itemPos.append(i)
    
    def PlaceraMonster(self, data):
        if data != None:
            for monster in data:
                nyMonster = Monster(monster[0], monster[1], monster[2])
                self.monsters.append(nyMonster)
                self.monsterPos.append(monster[2])
            return
        j = random.randint(self.minMon, self.maxMon)
        while len(self.monsters) < j:
            i = random.randint(0, 99)
            if not i == player.pos and not i in self.itemPos and not i in self.monsterPos and not i in self.fällorPos:
                typ = random.choice(["Zombie", "Varulv", "Drake"])
                str = random.randint(5, 20)
                nyaMonster = Monster(typ, str, i)
                self.monsters.append(nyaMonster)
                self.monsterPos.append(i)
    
    def SpawnaMonster(self):
        if not len(self.monsters) >= self.maxMon:
            for j in range(100):
                i = random.randint(0, 99)
                if not i == player.pos and not i in self.itemPos and not i in self.monsterPos and not i in self.fällorPos:
                    typ = random.choice(["Zombie", "Varulv", "Drake"])
                    str = random.randint(5, 20)
                    nyaMonster = Monster(typ, str, i)
                    self.monsters.append(nyaMonster)
                    self.monsterPos.append(i)
                    return
    
    def PlaceraFällor(self, data):
        if data != None:
            for fälla in data:
                nyFälla = Fällor(int(fälla))
                self.fällor.append(nyFälla)
                self.fällorPos.append(fälla)
            return
        j = random.randint(self.minFäl, self.maxFäl)
        while len(self.fällor) < j:
            i = random.randint(0, 99)
            if not i == player.pos and not i in self.itemPos and not i in self.monsterPos and not i in self.fällorPos:
                print(i)
                nyFälla = Fällor(i)
                self.fällor.append(nyFälla)
                self.fällorPos.append(i)

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
    def CheckForItems(k=0):
        if k==0:
            global gameState, menyVal, subMenyVal
            for i in range(len(karta.items)):
                if karta.items[i].cords == player.pos:
                    if gameState != 3:
                        gameState = 2
                    return karta.items[i]
        else:
            for i in range(len(karta.items)):
                if karta.items[i].cords == player.pos:
                    return True
            return False
    
    @staticmethod
    def CheckForMonsters(k=0):
        if k==0:
            global gameState, menyVal, subMenyVal
            for i in range(len(karta.monsters)):
                if karta.monsters[i].cords == player.pos:
                    if gameState != 1:
                        gameState = 1
                        menyVal = 5
                        subMenyVal = 0
                    return karta.monsters[i]
        else:
            for i in range(len(karta.items)):
                if karta.items[i].cords == player.pos:
                    return True
            return False

    @staticmethod
    def LaddaIn():
        #ladda in information
        information = spara.Läs()
        if information != None:
            i = information.splitlines()
            items = []
            monsters = []
            fällor = []
            appendObj = ""
            count = 2
            tT = []
            for line in i:  
                if appendObj == "Items":
                    if count == 4:
                        tT.append(str(line))
                        count = 3
                    elif count == 3:
                        tT.append(int(line))
                        count = 2
                    elif count == 2:
                        tT.append(int(line))
                        count = 1
                    else:
                        count = 4
                        tT.append(str(line))
                        items.append(tT)
                        tT = []
                elif appendObj == "Monster":
                    if count == 3:
                        tT.append(line)
                        count = 2
                    elif count == 2:
                        tT.append(int(line))
                        count = 1
                    else:
                        count = 3
                        tT.append(int(line))
                        monsters.append(tT)
                        tT = []
                elif appendObj == "Fällor":
                    if(line != "-----SPELARE"):
                        fällor.append(int(line))
                    
                elif appendObj == "Spelare":
                    if count == 5:
                        player.pos = int(line)
                        count = 4
                    elif count == 4:
                        player.str = int(line)
                        global startStrength
                        startStrength = int(line)
                        count = 3
                    elif count == 3:
                        player.hp = int(line)
                        count = 2
                    elif count == 2:
                        player.lvl = int(line)
                        count = 1
                    else:
                        player.skill = int(line)
                        appendObj = ""
                elif appendObj == "Inventory":
                    if count == 4:
                        tT.append(str(line))
                        count = 3
                    elif count == 3:
                        tT.append(int(line))
                        count=2
                    elif count == 2:
                        tT.append(int(line))
                        count = 1
                    else:
                        count = 4
                        tT.append(str(line))
                        nyItem = Föremål(tT[0], tT[1], tT[2], tT[3])
                        player.inventory.append(nyItem)
                        tT = []      

                if line == "-----ITEMS I VÄRLDEN":
                    tT = []
                    appendObj = "Items"
                    count = 4
                elif line == "-----MONSTER I VÄRLDEN":
                    tT = []
                    appendObj = "Monster"
                    count = 3
                elif line == "-----FÄLLOR I VÄRLDEN":
                    appendObj = "Fällor"
                elif line == "-----SPELARE":
                    appendObj = "Spelare"
                    count = 5
                    tT = []
                elif line == "-----INVENTORY":
                    appendObj = "Inventory"
                    tT = []
                    count = 4

            karta.PlaceraFöremål(items)
            karta.PlaceraMonster(monsters)
            karta.PlaceraFällor(fällor)
        else:
            karta.PlaceraFöremål(None)
            karta.PlaceraMonster(None)
            karta.PlaceraFällor(None)
    
    @staticmethod
    def BytUtItem():
        global gameState, subMenyVal, menyVal, valtItem
        #droppa föremålet du valt
        itemAttTappa = player.inventory[valtItem] #spara själva objektet
        player.inventory.pop(valtItem) #ta bort från inventory
        itemAttTappa.cords = player.pos #lägga till nuvarande position till föremål
        itemAttTappa.container = "mark"

        #plocka upp föremålet du står vid
        föremål = F.CheckForItems() #hitta objektet av föremålet du står vid
        player.inventory.insert(valtItem, föremål) #lägg till i inventory
        index = karta.items.index(föremål) #hitta index av föremålet på kartan
        karta.items.pop(index) #ta bort det föremålet från kart
        karta.items.append(itemAttTappa) #lägga det föremålet du tappa på kart

        #nollställ variabler
        gameState = 0
        subMenyVal = 0
        menyVal = 0
        valtItem = None
        


#----------------------------globala variabler
gameState = 0
#gameState 0 = vanlig meny
#gameState 1 = i en fight
#gameState 2 = vid item
#gameState 3 = byt ut item i inventory
#gameState 4 = du är död
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
fightBoxPos = 0 #själva offsetten för boxen
fightBoxHåll = 1

#om du förloared fight
fightresultat = 0
fällaResultat = 0

#valt item som ska bytas ut
valtItem = None

#strength när du laddar in
startStrength = 0



#Skapa objekt 
#        hp, lvl, str, skill, pos, inventory
player = player(10, 0, 1, 1, 45, [])
karta = Karta(10, 10)

class UI:
    @staticmethod
    def DrawMinimap(screen):
        k = 0
        for i in range(karta.w):
            for j in range(karta.h):
                pygame.draw.rect(screen, (40, 40, 40), (i*11+1160, j*11+10, 10, 10))
                for h in range(len(karta.items)):
                    if k == karta.items[h].cords:
                        if karta.items[h].typ == "Äpple":
                            pygame.draw.rect(screen, (70, 70, 70), (i*11+1160, j*11+10, 10, 10))
                        elif karta.items[h].typ == "Svärd":
                            pygame.draw.rect(screen, (70, 70, 70), (i*11+1160, j*11+10, 10, 10))
                        elif karta.items[h].typ == "Potion":
                            pygame.draw.rect(screen, (70, 70, 70), (i*11+1160, j*11+10, 10, 10))
                for l in range(len(karta.monsters)):
                    if k == karta.monsters[l].cords:
                        if karta.monsters[l].typ == "Zombie":
                            pygame.draw.rect(screen, (70, 70, 70), (i*11+1160, j*11+10, 10, 10))
                        elif karta.monsters[l].typ == "Varulv":
                            pygame.draw.rect(screen, (70, 70, 70), (i*11+1160, j*11+10, 10, 10))
                        elif karta.monsters[l].typ == "Drake":
                            pygame.draw.rect(screen, (70, 70, 70), (i*11+1160, j*11+10, 10, 10))
                for p in range(len(karta.fällor)):
                    if k == karta.fällor[p].cords:
                        pygame.draw.rect(screen, (70, 70, 70), (i*11+1160, j*11+10, 10, 10))

                if k == player.pos:
                    pygame.draw.rect(screen, (240, 240, 240), (i*11+1160, j*11+10, 10, 10))
        
                k+=1

    @staticmethod
    def DrawUI(screen, font, textObjekt):
        if gameState == 4:
            F.ClearText(textObjekt)
            F.PrintText(screen, font, "Du är död", 400, 300, textObjekt)
            return
        if gameState == 3:#g3
            #rita själva boxen
            pygame.draw.rect(screen, (40, 40, 40), (200, 329, 860, 200))
            pygame.draw.rect(screen, (10, 10, 10), (205, 334, 850, 190))
        
            #allt under här är för att räkna x,y offset(samt text) för de olika grejerna man har i inventory
            x=0
            y=0
            for i in range(len(player.inventory)):
                if subMenyVal == i and valtItem == None:
                    pygame.draw.rect(screen, (40, 40, 40), (240+(280*x), 344+(60*y), 120, 50), 0, 5)
                F.PrintText(screen, font, player.inventory[i].typ, 250+(280*x), 349+(60*y), textObjekt)
                F.PrintText(screen, font, str(player.inventory[i].strbonus), 370+(280*x), 349+(60*y), textObjekt)
                x+=1
                if x == 3:
                    y+=1
                    x=0
            x=0
            y=0
            if valtItem != None:
                for i in range(2):
                    pygame.draw.rect(screen, (80, 80, 80), (450+(220*i), 550, 200, 80))
                    #göra outline för alla boxar förutom den man kollar på så att säga
                    if not subMenyVal == i:
                        pygame.draw.rect(screen, (10, 10, 10), (455+(220*i), 555, 190, 70))
                
            F.PrintText(screen, font, "Fortsätt", 460, 565, textObjekt)
            F.PrintText(screen, font, "Annat", 680, 565, textObjekt)
            return

        if gameState == 2:
            if(F.CheckForItems().container == "mark"):
                if(F.CheckForItems().typ == "Potion"):
                    F.PrintText(screen, font, f"Du ser en {F.CheckForItems().typ} på {F.CheckForItems().container}en", 400, 300, textObjekt)
                else:
                    F.PrintText(screen, font, f"Du ser ett {F.CheckForItems().typ} på {F.CheckForItems().container}en", 400, 300, textObjekt)
            else:
                if(F.CheckForItems().typ == "Potion"):    
                    F.PrintText(screen, font, f"Du ser en {F.CheckForItems().typ} i en {F.CheckForItems().container}", 400, 300, textObjekt)
                else:
                    F.PrintText(screen, font, f"Du ser ett {F.CheckForItems().typ} i en {F.CheckForItems().container}", 400, 300, textObjekt)
            F.PrintText(screen, font, f"som ger {F.CheckForItems().strbonus} styrka", 400, 350, textObjekt)

            for i in range(2):
                pygame.draw.rect(screen, (80, 80, 80), (450+(220*i), 550, 200, 80))
                #göra outline för alla boxar förutom den man kollar på så att säga
                if not subMenyVal == i:
                    pygame.draw.rect(screen, (10, 10, 10), (455+(220*i), 555, 190, 70))
            
            if len(player.inventory) == player.maxItems:
                F.PrintText(screen, font, "Byt ut", 460, 565, textObjekt)
            else:
                F.PrintText(screen, font, "Plocka Upp", 460, 565, textObjekt)
            F.PrintText(screen, font, "Lämna", 680, 565, textObjekt)
            return

        #gamestate 1 är här
        if gameState == 1:
            try:
                F.PrintText(screen, font, f"Du har stött på en {F.CheckForMonsters().typ} med {F.CheckForMonsters().str + round(player.lvl*2)} styrka", 400, 300, textObjekt)
            except:
                return
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
                return
            if menyVal == 6:
                #när du är i en fight så kommer dethär ritas till skärmen
                pygame.draw.rect(screen, (40, 40, 40), (200, 429, 860, 200))
                pygame.draw.rect(screen, (10, 10, 10), (205, 434, 850, 190))
                pygame.draw.rect(screen, (40, 40, 40), (450, 429, 360, 200))
                pygame.draw.rect(screen, (60, 60, 60), (550, 429, 160, 200))
                pygame.draw.rect(screen, (80, 80, 80), (600, 429, 60, 200))

                pygame.draw.rect(screen, (250, 250, 250), (210+fightBoxPos, 429, 20, 200))
                return
            
            if menyVal == 7:

                #rita själva boxen
                pygame.draw.rect(screen, (40, 40, 40), (200, 429, 860, 200))
                pygame.draw.rect(screen, (10, 10, 10), (205, 434, 850, 190))
                
                #allt under här är för att räkna x,y offset(samt text) för de olika grejerna man har i inventory
                x=0
                y=0
                for item in player.inventory:
                    F.PrintText(screen, font, item.typ, 250+(280*x), 449+(60*y), textObjekt)
                    F.PrintText(screen, font, str(item.strbonus), 370+(280*x), 449+(60*y), textObjekt)
                    x+=1
                    if x == 3:
                        y+=1
                        x=0
                x=0
                y=0
                return
            
            if menyVal == 8:
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

            if menyVal == 9:
                pass
                return
            if menyVal == 10:
                pass
                return
            return
        #gameState 0 här under
        UI.DrawMinimap(screen)
        if menyVal == 0:
            for i in range(4):
                pygame.draw.rect(screen, (80, 80, 80), (200+(220*i), 550, 200, 80))
                #göra outline för alla boxar förutom den man kollar på så att säga
                if not subMenyVal == i:
                    pygame.draw.rect(screen, (10, 10, 10), (205+(220*i), 555, 190, 70))
        
            F.PrintText(screen, font, "Gå", 225, 567, textObjekt)
            F.PrintText(screen, font, "Inventory", 437, 567, textObjekt)
            F.PrintText(screen, font, "Stats", 660, 567, textObjekt)
            F.PrintText(screen, font, "Stäng av", 880, 567, textObjekt)
            
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
            for item in player.inventory:
                F.PrintText(screen, font, item.typ, 250+(280*x), 449+(60*y), textObjekt)
                F.PrintText(screen, font, str(item.strbonus), 370+(280*x), 449+(60*y), textObjekt)
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
        global menyVal, subMenyVal, valtItem
        if gameState == 3:
            if valtItem == None:
                if subMenyVal == 3:
                    subMenyVal = 0
                    return
                if subMenyVal == 4:
                    subMenyVal = 1
            return
        if menyVal == 1:
            subMenyVal = 0 
    
    @staticmethod
    def Ner():
        global menyVal, subMenyVal, valtItem
        if gameState == 3:
            if valtItem == None:
                if len(player.inventory) >= 4:
                    if subMenyVal == 0:
                        subMenyVal = 3
                    elif subMenyVal == 1:
                        subMenyVal = 4
            return
        if menyVal == 1:
            subMenyVal = 1

    @staticmethod
    def Höger():
        global menyVal, subMenyVal, gameState, valtItem
        if gameState == 3:
            if valtItem == None:
                if subMenyVal != len(player.inventory)-1:
                    subMenyVal += 1
                return
            else:
                if subMenyVal != 1:
                    subMenyVal = 1
                return
        if gameState == 2:
            subMenyVal = 1
            return
        if menyVal == 0 or menyVal == 5:
            if subMenyVal != 3:
                subMenyVal += 1
            
        elif menyVal == 1:
            subMenyVal = 3

    @staticmethod
    def Vänster():
        global menyVal, subMenyVal, gameState, valtItem
        if gameState == 3:
            if valtItem == None:
                if subMenyVal != 0:
                    subMenyVal -= 1
                return
            else:
                if subMenyVal != 0:
                    subMenyVal = 0
                return
        if gameState == 2:
            subMenyVal = 0
            return
        if menyVal == 0 or menyVal == 5:
            if subMenyVal != 0:
                subMenyVal -= 1
        elif menyVal == 1:
            subMenyVal = 2

    @staticmethod
    def Enter():
        global menyVal, subMenyVal, gameState, fightresultat, valtItem, fällaResultat
        if gameState == 3:
            if valtItem == None:
                valtItem = subMenyVal
                subMenyVal = 0
            else:
                if subMenyVal == 0:
                    F.BytUtItem()
                    return
                if subMenyVal == 1:
                    valtItem = None
                    return
            return
        if gameState == 2:
            if subMenyVal == 0: # du tryckt på plocka upp
                if len(player.inventory) >= player.maxItems:
                    gameState = 3
                    subMenyVal = 0
                    return
                föremål = F.CheckForItems()
                player.Pickup(föremål)
                index = karta.items.index(föremål)
                karta.items.pop(index)
            gameState = 0
            menyVal = 0
            
            return

        #i vanliga menyn
        if menyVal == 0:
            if subMenyVal == 0: #om man tryckt på "Gå"
                menyVal = 1
            elif subMenyVal == 1: #om man tryckt på "Inventory"
                menyVal = 2
            elif subMenyVal == 2: #om man tryckt på "Stats"
                menyVal = 3
            elif subMenyVal == 3: #om man tryckt på "stäng av"
                print("exporterat data") if spara.Spara(karta.items, karta.monsters, karta.fällor, player) == 0 else "fel med export"

                pygame.quit()
                exit()
            subMenyVal = 0
            return
        
        #i fightmenyn
        if menyVal == 5:
            if subMenyVal == 0: #om man tryckt på "Fight"
                menyVal = 6
            elif subMenyVal == 1: #om man tryckt på "Inventory"
                menyVal = 7
            elif subMenyVal == 2: #om man tryckt på "Stats"
                menyVal = 8
            elif subMenyVal == 3: #om man tryckt på "Fly"
                menyVal = 0
                gameState = 0
            subMenyVal = 0
            return

        if menyVal == 1:
            fightresultat = 0
            fällaResultat = 0

            if subMenyVal == 0:
                player.Move("Norr")
            if subMenyVal == 1:
                player.Move("Syd")
            if subMenyVal == 2:
                player.Move("Öst")
            if subMenyVal == 3:
                player.Move("Väst")
          
            #kolla om gubben är i samma ruta som föremål eller monster
            if F.CheckForItems() != None:
                subMenyVal = 0
            F.CheckForMonsters()


        if menyVal == 6:
            global fightBoxPos
            if player.Attack(fightBoxPos, F.CheckForMonsters()) == 1:
                # du vann
                player.levelup(1)
                fightresultat = 2
                gameState = 0
                menyVal = 0
                for monster in karta.monsters:
                    if monster.cords == player.pos:
                        i = karta.monsters.index(monster)
                        karta.monsters.pop(i)
            else:
                player.hp -= 1
                fightresultat = 1
                gameState = 0
                menyVal = 0
            fightBoxPos = 0

    @staticmethod
    def Tillbaka():
        global menyVal, subMenyVal, gameState, valtItem
        if gameState == 3:
            gameState = 0
            valtItem = None
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

        #bakgrundstimer
        self.tid = pygame.USEREVENT + 1
        pygame.time.set_timer(self.tid, 1000)  # tickar varje 1000ms(1s)
        self.passeradTid = 0

    def Input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                print("exporterat data") if spara.Spara(karta.items, karta.monsters, karta.fällor, player) == 0 else "fel med export"

                pygame.quit()
                exit()

            if event.type == self.tid:
                self.passeradTid += 1
                print(self.passeradTid)
                if self.passeradTid >= 10:
                    #spawna monster
                    karta.SpawnaMonster()
                    self.passeradTid = 0

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
        if gameState != 4:
            if fightresultat == 1:
                F.PrintText(self.screen, self.font, "Du förlorade fighten", 400, 260, self.textObjekter)
                F.PrintText(self.screen, self.font, "Du har tappat 1 hp", 400, 300, self.textObjekter)
            if fightresultat == 2:
                F.PrintText(self.screen, self.font, "Du vann fighten", 400, 260, self.textObjekter)
                F.PrintText(self.screen, self.font, "Du har gått upp en level", 400, 300, self.textObjekter)

        if F.CheckForItems(1) == True:
            F.PrintText(self.screen, pygame.font.SysFont("Arial", 16), "du står vid ett item", 400, 20, self.textObjekter)
        
        global fällaResultat
        
        for fälla in karta.fällor:
            if player.pos == fälla.cords:
                fällaResultat = player.Undvik()
                karta.fällor.pop(karta.fällor.index(fälla))
                global menyVal, subMenyVal
                menyVal = 0
                subMenyVal = 0

        if(fällaResultat == 1):
            F.PrintText(self.screen, self.font, "du unvek fällan", 400, 300, self.textObjekter)
        elif(fällaResultat == 2):
            F.PrintText(self.screen, self.font, "du gick i en fälla och tappade 1 hp", 400, 300, self.textObjekter)

        if player.lvl == 10:
            F.PrintText(self.screen, self.font, "Du har vunnit", 200, 200, self.textObjekter)

        #uppdatera skärmen
        pygame.display.flip()
    
    def Uppdatera(self):
        global fightBoxHåll, fightBoxPos, valtItem, gameState
        if menyVal == 6: #om du är i fight
            #rörelse fram och tillbaka
            if fightBoxPos > 825:
                fightBoxHåll = -1
            elif fightBoxPos < 0:
                fightBoxHåll = 1
            fightBoxPos += 9*fightBoxHåll

        j = 0
        for item in player.inventory:
            j += item.strbonus
        player.str = j+startStrength
        if player.hp == 0:
            gameState = 4


    def Kör(self): # flödeskema
        #ladda in sparad information från export-filen
        F.LaddaIn()
            
        while self.running:
            self.Input()
            self.Uppdatera()
            self.Rendera()

            self.clock.tick(120)

if __name__ == "__main__":
    spel = Spel()
    spel.Kör()