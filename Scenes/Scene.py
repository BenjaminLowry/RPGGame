
class Scene:

    def __init__(self):
        self.location = ""
        self.openingDescription = ""
        self.objects = []
        self.exits = []  # [Object: Scene]
        self.collectables = []  # [Collectable]
