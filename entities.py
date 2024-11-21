class föremål:
    def __init__(self):
        self.items = []
        self.items_pos = []

    def Placera(self, typ, pos):
        self.items.append(typ)
        self.items_pos.append(pos)

class player:
    def __init__(self, pos, inv = ["ab", "bc", "cfd", "dfc", "fab", "bfc", "cdv", "dvc", "avb"]):
        self.pos = pos
        self.inv = inv

    def Move(self, dir):
        try:
            if dir == "Norr":
                self.pos -= 1
            elif dir == "Syd":
                self.pos += 1
            elif dir == "Öst":
                self.pos -= 10
            elif dir == "Väst":
                self.pos += 10
        except:
            print("fel i player.Move()")