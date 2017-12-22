from Collectibles.Usables.Usable import Usable
from Entities.Entity import Entity


class Weapon(Usable):

    def __init__(self, name, weight, description, range, damage, attackSpeed, ammunition, meleeWeapon, durability,
                 durabilityDecayConstant):

        super().__init__(name, weight, description, range)

        self.damage = damage
        self.attackSpeed = attackSpeed  # In seconds

        self.ammunition = ammunition  # -1 for melee weapons
        self.meleeWeapon = meleeWeapon

        self.durability = durability  # From 0 to 1; the inverse of the probability of it breaking after one use
        self.durabilityDecayConstant = durabilityDecayConstant  # How much the durability constant decreases with use

    def use(self, object):

        if super().use(object) == "Entity":  # This is an attack on an entity
            return "Attack"


        print("It is a weapon.")

