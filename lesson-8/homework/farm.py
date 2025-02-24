class Animal:
    def __init__(self, name, species, food, sound):
        self.name = name
        self.species = species
        self.food = food
        self.sound = sound

    def makes_sound(self):
        print(f"{self.name} says '{self.sound}'")

    def sleep(self):
        print(f"{self.name} is sleeping now.")

    def eats(self):
        print(f"{self.name} eats {self.food}.")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "cow", "grass", "moooo")
    
    def produces_milk(self):
        print(f"{self.name} produces milk.")

class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "sheep", "grass", "baaa")

    def gives_wool(self):
        print(f"{self.name} gives wool")

class Goose(Animal):
    def __init__(self, name):
        super().__init__(name, "goose", "corn", "honk-honk")
    def lays_eggs(self):
        print(f"{self.name} lays eggs")

class Dove(Animal):
    def __init__(self, name):
        super().__init__(name, "dove", "corn", "coo-coo-coo")
    
    def flies(self):
        print(f"{self.name} flies high in the sky")


cow = Cow("Matilda")
sheep = Sheep("Alex")
goose = Goose("Max")
dove = Dove("Daniel")

for animal in [cow, sheep, goose, dove]:
    animal.makes_sound()
    animal.eats()
    animal.sleep()
    print()


cow.produces_milk()
sheep.gives_wool()
goose.lays_eggs()
dove.flies()