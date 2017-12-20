from Entities.Entity import Entity
from Collectibles.Collectible import Collectible


class Usable(Collectible):

    def __init__(self, name, weight, description, range):

        super().__init__(name, weight, description)
        self.range = range  # In meters

    # Perform function for specific usable
    def use(self, object):

        if isinstance(object, Entity):
            return "Entity"

        print("Item used.")





