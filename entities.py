class föremål:
    def __init__(self):
        self.items = []
        self.items_pos = []

    def Placera(self, typ, pos):
        self.items.append(typ)
        self.items_pos.append(pos)

class player:
    def __init__(self, hp, lvl, str, skill, pos, inventory = ["ab", "bc", "cfd", "dfc", "fab", "bfc", "cdv", "dvc", "avb"]):
        self.hp = hp
        self.lvl = lvl
        self.str = str
        self.skill = skill
        self.inventory = inventory
        self.pos = pos
   
    def Move(self, direction):
        try:
            if direction == "Norr":
                self.pos -= 1
            elif direction == "Syd":
                self.pos += 1
            elif direction == "Öst":
                self.pos -= 10
            elif direction == "Väst":
                self.pos += 10
        except:
            print("fel i player.Move()")
    
    def levelup(self, amount):
        self.lvl += amount

   

class monster:
    def __init__(self, str, cords):
        self.str = str
        self.cords = cords