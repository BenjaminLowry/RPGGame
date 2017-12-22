


class Scene:

    def __init__(self, location, openingDescription, objects, exits, collectibles, entities):
        self.location = location  # Location
        self.openingDescription = openingDescription
        self.objects = objects  # [Object]
        self.exits = exits  # {Object: Scene}
        self.collectibles = collectibles  # [Collectible] -- Does not include collectibles inside objects
        self.entities = entities  # [Entity]

    def get_opening_description(self):
        return self.openingDescription.split(". ")
 
    def parse(self, commandText):

        (command, objectName) = str(commandText).lower().split(":")

        selectedObject = None

        for object in self.objects:

            if objectName == str(object.name).lower():
                selectedObject = object
                break

        if command == "go to":
            return self.go_to(selectedObject)
        elif command == "look under":
            pass

    def go_to(self, object):

        descriptionArray = object.description.split(". ")
        return descriptionArray





