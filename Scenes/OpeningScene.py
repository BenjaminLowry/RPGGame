from Scenes.Scene import Scene
from Locations.Location import Location
from Objects.Object import Object

class OpeningScene(Scene):

    def __init__(self):

        location = Location("Bedroom", "You woke up here. You don't know why.", "------"
                            "|    |"
                            "------", (0, 0))

        openingDescription = open("OpeningScene.txt", "r").read()

        window = Object("A dirty window half-covered with old drapes. Can't seem much outside. It is daytime though.",
                        None)
        bed = Object("A metal bed frame with old mattress on it. Some mysterious stains present.")

        super()._



