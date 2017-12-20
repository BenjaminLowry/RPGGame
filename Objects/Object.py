from enum import Enum


class Object:

    def __init__(self, name, description, collectibles):

        self.name = name
        self.description = description
        self.collectibles = collectibles  # [Collectible: HiddenType]

    def override_description(self, description):

        self.description = description

    def search_object(self, method):

        foundObjects = []
        for (collectible, hiddenType) in self.collectibles:

            if hiddenType == method:
                foundObjects.append(collectible)

        if foundObjects.count() == 0:
            return None, "There was nothing " + str(method).lower() + " the " + self.name.lower()
        else:
            message = str(method) + " the " + self.name.lower() + ", you found a "

            # Loop through objects to generate string declaring what you found by searching
            for i in range(0, foundObjects.count()):

                if i == foundObjects.count() - 1:
                    message += " and a " + foundObjects[i].name + "."
                else:
                    message += foundObjects[i].name + ", "

            return foundObjects, message


class HiddenType(Enum):
    ABOVE = "Above"
    BEHIND = "Behind"
    INSIDE = "Inside"
    UNDER = "Under"

