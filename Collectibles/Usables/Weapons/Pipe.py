from Collectibles.Usables.Weapons.Weapon import Weapon


class Pipe(Weapon):

    def __init__(self):

        super().__init__("Pipe", 3, "A rusted pipe. Heavy but brings a punch.", 1, 25, 1, -1, True, 0.999, 0.001)

