from Objects.Object import Object
from Objects.Breakable import Breakable
from Objects.Object import HiddenType

class Window(Object, Breakable):

    def __init__(self, collectibles):

        super().__init__("Window", "A normal window. Slightly dirty.", collectibles)

    def breakObject(self):

        collectibles, message = super().search_object(HiddenType.INSIDE)
        return collectibles, message
