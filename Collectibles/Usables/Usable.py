from Entities.Entity import Entity
from Collectibles.Collectible import Collectible

class Usable(Collectible):

    def __init__(self):

        super().__init__()
        self.range = 0

    # Perform function for specific usable
    def use(self, object):

        if isinstance(object, Entity):
            return "Entity"

        print("Item used.")





