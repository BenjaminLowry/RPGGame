from abc import abstractmethod, ABCMeta

class Breakable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def breakObject(self):
        pass
