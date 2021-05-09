class Character:
    def __init__(self, name, life, armor, damage):
        self.name = name
        self.life = life
        self.armor = armor
        self.damage = damage
        self.attack_elf = False
        self.attack_human = False
        self.attack_orc = False
        self.attack_dwarf = False

    def attack_Elf(self):
        self.attack_elf = True
    def attack_Human(self):
        return (True)
    def attack_Orc(self):
        self.attack_orc = True
    def attack_Dwarf(self):
        self.attack_dwarf = True
    def get_damage (self):
        return (self.damage)
    def get_life (self):
        return (self.life)



#Elf, Human, Orc, Dwarf
class Elf(Character):
    def state(self):
        if Human.attack_Elf() == True:
            state = (Human.get_damage() - self.armor) - self.life
            return (state)
        if Orc.attack_Elf() == True:
            state = (Orc.get_damage() - self.armor) - self.life
            return (state)
        if Dwarf.attack_Elf() == True:
            state = (Dwarf.get_damage() - self.armor) - self.life
            return (state)
class Human(Character):
    def state(self):
        if Elf.attack_Human() == True:
            self.life = ((Elf.get_damage() - self.armor) - self.life)
            return ("FUNCIONA PA")
        if Orc.attack_Human() == True:
            state = (Orc.get_damage() - self.armor) - self.life
            return (state)
        if Dwarf.attack_Human() == True:
            state = (Dwarf.get_damage() - self.armor) - self.life
            return (state)
class Orc(Character):
    def state(self):
        if elf.attack_Orc() == True:
            state = ((Elf.get_damage() - self.armor) - self.life)
            return (state)
        if Human.attack_Orc() == True:
            state = (Human.get_damage() - self.armor) - self.life
            return (state)
        if Dwarf.attack_Orc() == True:
            state = (Dwarf.get_damage() - self.armor) - self.life
            return (state)
class Dwarf(Character):
    def state (self):
        if Elf.attack_Dwarf() == True:
            state = (Elf.get_damage() - self.armor) - self.life
            return(state)
        if Human.attack_Dwarf() == True:
            state = (Human.get_damage() - self.armor) - self.life
            return (state)
        if Orc.attack_Dwarf() == True:
            state = (Orc.get_damage() - self.armor) - self.life
            return (state)
#type, life, armor, damage
elf= Elf("Elf", 150, 10, 15)
human = Human("Human", 150, 5, 20)
orc = Orc("Orc", 100, 1, 40)
dwarf = Dwarf("Dwarf", 100, 10, 5)

elf.attack_Human()
human.state()