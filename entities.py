class föremål:
    def __init__(self):
        self.items = []
        self.items_pos = []

    def Placera(self, typ, pos):
        self.items.append(typ)
        self.items_pos.append(pos)

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
        if direction == "Norr":
            self.pos -= 1
        elif direction == "Syd":
            self.pos += 1
        elif direction == "Öst":
            self.pos -= 10
        elif direction == "Väst":
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