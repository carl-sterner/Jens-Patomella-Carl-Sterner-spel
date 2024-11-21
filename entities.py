class föremål:
    def __init__(self, pos, typ):
        self.pos = pos
        self.typ = typ

    def Placera(self):
        pass
class player:
    def __init__(self, pos, inv = ["ab", "bc", "cfd", "dfc", "fab", "bfc", "cdv", "dvc", "avb"]):
        self.pos = pos
        self.inv = inv
    
    def Move(self, dir):
        try:
            if dir == "Norr":
                self.pos -= 10
            elif dir == "Syd":
                self.pos += 10
            elif dir == "Öst":
                self.pos -= 1
            elif dir == "Väst":
                self.pos += 1
        except:
            print("fel i player.Move()")