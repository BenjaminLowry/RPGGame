from
from Locations.Location import Location
from Objects.Window import Window
from Objects.Bed import Bed

class OpeningScene(Scene):

    def __init__(self):

        location = Location("Bedroom", "You woke up here. You don't know why.", "------"
                            "|    |"
                            "------", (1, 1))

        openingDescription = open("OpeningScene.txt", "r").read()

        window = Window(None)
        window.override_description("A dirty window half-covered with old drapes. Can't seem much outside. "
                                    "It is daytime though.")

        bed = Bed(None)

        bed =

        # exit = [window: scene2]

        super().__init__()



