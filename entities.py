class Föremål:
    def __init__(self, typ, strbonus, cords):
        self.typ = typ
        self.strbonus = strbonus
        self.cords = cords

class player:
    def __init__(self, hp, lvl, str, skill, pos, inventory):
        self.hp = hp
        self.lvl = lvl
        self.str = str
        self.skill = skill
        self.inventory = inventory
        self.maxItems = 5
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
        if len(self.inventory) == self.maxItems:
            return
        self.inventory.append(item)

    def levelup(self, amount):
        self.lvl += amount

    def Attack(self, fightBoxPos, monster):
        boost = 0
        if fightBoxPos+210 >= 205 and fightBoxPos+210 <= 205+850:
            if fightBoxPos+210 >= 450 and fightBoxPos+210 <= 450+360:
                if fightBoxPos+210 >= 550 and fightBoxPos+210 <= 550+160:
                    if fightBoxPos+210 >= 600 and fightBoxPos+210 <= 600+60:
                        boost = 1.3
                    boost = 1.2
                boost = 1.1
            boost = 1
        if self.str * boost > monster.str:
            return 1
        else:
            return 0

class Monster:
    def __init__(self, typ, str, cords):
        self.typ = typ
        self.str = str
        self.cords = cords