from Scenes.Scene import Scene
from Locations.Location import Location
from Objects.Object import Object

class OpeningScene(Scene):

    def __init__(self):

        self.location = Location("Bedroom", "You woke up here. You don't know why.", "------"
                            "|    |"
                            "------", (0, 0))

        self.openingDescription = open("OpeningScene.txt", "r").read()

        self.window = Object("A dirty window half-covered with old drapes. Can't seem much outside. It is daytime though.",
                        None)
        self.bed = Object("A metal bed frame with old mattress on it. Some mysterious stains present.")

        self.openingDescript = ["You wake up in a dimly lit room. You're laying on a bed.", "Hmm... there aren't sheets on the bed.", 'Small strands of sunlight illuminate the wall to your right.', 'There’s a socket on the ceiling where a lightbulb used to be. To the left of the bed there’s a dresser. One of its handles is broken.', 'There’s a white wooden door on the other side of the room. It’s shut.', 'You hear a growling noise off in the distance.']


        super()._



