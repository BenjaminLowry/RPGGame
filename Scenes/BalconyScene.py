from Scenes.Scene import Scene
from Locations.Location import Location

class BalconyScene(Scene):

    def __init__(self):

        location = Location("Balcony", "A small balcony with a rusty ladder leading down to the ground."
                                       "Some dead plants...look like sunflowers...", "---"
                                                                                     "| |"
                                                                                     "---", (3, 4))


        
