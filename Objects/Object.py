from enum import Enum


class Object:

    def __init__(self, name, description, collectibles):

        self.name = name
        self.description = description
        self.collectibles = collectibles  # [Collectible: HiddenType]

    def override_description(self, description):

        self.description = description

    def search_object(self, searchMethod):

        foundObjects = []
        for (collectible, hiddenType) in self.collectibles:

            if hiddenType == searchMethod:
                foundObjects.append(collectible)

        if foundObjects.count() == 0:
            return None, "There was nothing " + str(searchMethod).lower() + " the " + self.name.lower()
        else:
            message = str(searchMethod) + " the " + self.name.lower() + ", you found a "

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

