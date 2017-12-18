from Collectables.Usables.Usable import Usable
from Entities.Entity import Entity

class Weapon(Usable):

    def __init__(self):

        super().__init__()

        self.damage = 0
        self.attackSpeed = 0

        self.ammunition = 0  # -1 for melee weapons
        self.meleeWeapon = True

        self.durability = 1  # From 0 to 1; the inverse of the probability of it breaking after one use
        self.durabilityDecayConstant = 0.01  # How much the durability constant decreases with each use


    def use(self, object):

        if super().use(object) == "Entity":  # This is an attack on an entity
            return "Attack"


        print("It is a weapon.")


weapon = Weapon()

entity = Entity()

weapon.use(entity)
