from Objects.Object import Object


class Bed(Object):

    def __init__(self, collectibles):

        super().__init__("Bed", "A metal bed frame with old mattress on it. Some mysterious stains present.", collectibles)

