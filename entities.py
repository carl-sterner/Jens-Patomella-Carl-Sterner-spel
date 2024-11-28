class Föremål:
    def __init__(self, typ, cords):
        self.typ = typ
        self.cords = cords

class player:
    def __init__(self, hp, lvl, str, skill, pos, inventory):
        self.hp = hp
        self.lvl = lvl
        self.str = str
        self.skill = skill
        self.inventory = inventory
        self.maxItems = 9
        self.pos = pos
   
    def Move(self, direction):
        p_y = (self.pos % 10)+1 # din y position 10 är karta.w måste bytas om karta.w ändras
        p_x = (self.pos // 10)+1 # din x position
        if direction == "Norr" and p_y != 1:
            self.pos -= 1
        elif direction == "Syd" and p_y != 10:
            self.pos += 1
        elif direction == "Öst" and p_x != 1:
            self.pos -= 10
        elif direction == "Väst" and p_x != 10:
            self.pos += 10
    
    def Pickup(self, item):
        self.inventory.append(item)

    def levelup(self, amount):
        self.lvl += amount

class Monster:
    def __init__(self, typ, str, cords):
        self.typ = typ
        self.str = str
        self.cords = cords