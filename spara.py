
def Spara(items, monsters, fällor, player):
    try:
        with open("export.txt", "w", encoding="utf-8") as file:
            file.write("-----ITEMS I VÄRLDEN" + "\n")
            for item in items:
                file.write(str(item.typ) + "\n")
                file.write(str(item.strbonus) + "\n")
                file.write(str(item.cords) + "\n")
                file.write(str(item.container) + "\n")
            file.write("-----MONSTER I VÄRLDEN" + "\n")
            for monster in monsters:
                file.write(str(monster.typ) + "\n")
                file.write(str(monster.str) + "\n")
                file.write(str(monster.cords) + "\n")
            file.write("-----FÄLLOR I VÄRLDEN" + "\n")
            for fälla in fällor:
                file.write(str(fälla.cords) + "\n")
            file.write("-----SPELARE" + "\n")
            file.write(str(player.pos) + "\n")
            j = 0
            for item in player.inventory:
                j += item.strbonus
            file.write(str(player.str - j) + "\n")
            file.write(str(player.hp) + "\n")
            file.write(str(player.lvl) + "\n")
            file.write(str(player.skill) + "\n")
            file.write("-----INVENTORY" + "\n")
            for item in player.inventory:
                file.write(str(item.typ)+"\n")
                file.write(str(item.strbonus)+"\n")
                file.write(str(item.cords)+"\n")
        return 0
    except Exception as e:
        print(f"exportfel: {e}")
        return 1

def Läs():
    try:
        with open("export.txt", "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"exportfel: {e}")