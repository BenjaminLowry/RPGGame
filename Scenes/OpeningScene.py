from Scenes.Scene import Scene
from Scenes.BalconyScene import BalconyScene
from Locations.Location import Location
from Objects.Window import Window
from Objects.Bed import Bed
from Objects.Dresser import Dresser
from Collectibles.Usables.Weapons.Pipe import Pipe


class OpeningScene(Scene):

    def __init__(self):

        location = Location("Bedroom", "You woke up here. You don't know why.", "------"
                            "|    |"
                            "------", (1, 1))

        openingDescription = open("OpeningScene.txt", "r").read()

        window = Window(None)
        window.override_description("A dirty window half-covered with old drapes. Can't see much outside. "
                                    "It is daytime though.")

        rustedPipe = Pipe()

        bed = Bed(rustedPipe)
        dresser = Dresser(None)

        balconyScene = BalconyScene()

        exit = {window: balconyScene}

        super().__init__(location, openingDescription, [window, bed, dresser], exit, None, None)





