from Entities.Human import Human

class User(Human):
    def __init__(self, *args, **kwargs):
        super().__init__()
        super.intelligence = 1.2

