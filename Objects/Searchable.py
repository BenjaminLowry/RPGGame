from abc import abstractmethod, ABCMeta
from Objects.Object import HiddenType


class Searchable:

    def search(self, object, searchMethod):
        return object.search_object(searchMethod)


class SearchableAbove(Searchable):

    def search_above(self, object):
        super().search(object, HiddenType.ABOVE)


class SearchableBehind(Searchable):

    def search_behind(self, object):
        super().search(object, HiddenType.BEHIND)


class SearchableInside(Searchable):

    def search_inside(self, object):
        super().search(object, HiddenType.INSIDE)


class SearchableUnder(Searchable):

    def search_under(self, object):
        super().search(object, HiddenType.UNDER)

