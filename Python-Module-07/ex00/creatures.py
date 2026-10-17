from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, name: str, type_name: str):
        self.name = name
        self.type_name = type_name

    def describe(self):
        print(f"{self.name} is a {self.type_name} type Creature")

    @abstractmethod
    def attack(self):
        pass


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self):
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self):
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self):
        return "Torragon uses Hydro Pump!"