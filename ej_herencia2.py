class Character:
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage
    def get_attack(self, name, damage):
        self.health = (self.health - (damage - self.armor))
        if self.health <= 0:
            print(f"{self.name} has died.")
        print(f" {name} has attacked {self.name}. His health point is: {self.health}")

    def attack(self, enemy):
        enemy.get_attack(self.name,self.damage)

class Elf(Character):
    pass
class Human(Character):
    pass
class Orc(Character):
    pass
class Dwarf(Character):
    pass

#type, life, armor, damage
elf= Elf("Elf", 150, 10, 25)
human = Human("Human", 150, 5, 30)
orc = Orc("Orc", 100, 1, 40)
dwarf = Dwarf("Dwarf", 100, 10, 20)

elf.attack(human)
human.attack(elf)
