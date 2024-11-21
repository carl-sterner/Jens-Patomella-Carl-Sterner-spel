class föremål:
    def __init__(self, pos, typ):
        self.pos = pos
        self.typ = typ
class player:
    def __init__(self, pos, inv = {'a': 1, 'b': 2, 'c': 3}):
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