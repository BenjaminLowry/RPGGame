from Entities.Entity import Entity


class Usable:

    def __init__(self):
        self.name = ""
        self.weight = 0
        self.description = ""
        self.range = 0

    # Perform function for specific usable
    def use(self, object):

        if isinstance(object, Entity):
            return "Entity"

        print("Item used.")




