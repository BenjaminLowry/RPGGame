from Objects.Object import Object
from Objects.Searchable import SearchableUnder

class Bed(Object, SearchableUnder):

    def __init__(self, collectibles):

        super().__init__("Bed", "A metal bed frame with an old mattress on it. "
                                "Some mysterious stains present.", collectibles)

    def __search_under__(self):
        return super().search_under(self)  # Returns (collectibles, message)

