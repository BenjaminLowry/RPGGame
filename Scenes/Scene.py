


class Scene:

    def __init__(self, location, openingDescription, objects, objectDescriptions, exits, collectibles, entities):
        self.location = location  # Location
        self.openingDescription = openingDescription
        self.objects = objects  # [Object]
        self.exits = exits  # {Object: Scene}
        self.collectibles = collectibles  # [Collectible] -- Does not include collectibles inside objects
        self.entities = entities  # [Entity]

    def get_opening_description(self):
        return self.openingDescription.split(". ")

    def parse(self, commandText):

        errorMessage = "Invalid request. Please try again."

        # If the user does not put a colon, throw error
        if not str(commandText).__contains__(":"):
            return errorMessage

        (command, objectName) = str(commandText).lower().split(":")

        selectedObject = None

        for object in self.objects:

            if objectName == str(object.name).lower():
                selectedObject = object
                break

        # If the user inputs an invalid object, throw error
        if selectedObject is None:
            return errorMessage

        if command == "go to":
            return self.go_to(selectedObject)
        elif command == "look under":
            pass
        else:  # If the command is invalid, throw error
            return errorMessage

    def go_to(self, object):

        descriptionArray = object.description.split(". ")
        return descriptionArray





