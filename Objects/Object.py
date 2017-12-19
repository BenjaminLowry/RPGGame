
class Object:

    def __init__(self, description, collectibles):

        self.description = description
        self.collectibles = collectibles  # [Collectible]

    def override_description(self, description):

        self.description = description
