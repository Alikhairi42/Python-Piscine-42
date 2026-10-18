
from ex00.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self):
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return "Bloomelle uses Petal Dance!"

    def heal(self):
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self):
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self):
        self.is_transformed = False
        return "Shiftling returns to normal."

    def attack(self):
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self):
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self):
        self.is_transformed = False
        return "Morphagon stabilizes its form."

    def attack(self):
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."
