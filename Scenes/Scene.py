
class Scene:

    def __init__(self, location, openingDescription, objects, objectDescriptions, exits, collectibles, entities):
        self.location = location  # Location
        self.openingDescription = openingDescription
        self.objects = objects  # [Object]
        self.exits = exits  # [Object: Scene]
        self.collectibles = collectibles  # [Collectible] -- Does not include collectibles inside objects
        self.entities = entities  # [Entity]




