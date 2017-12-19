from Objects.Object import Object


class Window(Object):

    def __init__(self, collectibles):

        super().__init__("A normal window. Slightly dirty.", collectibles)
