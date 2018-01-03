from Entities.Entity import Entity

class Human(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__()
        super.health = 100
        self.fatigue = super.health/100
        super.naturalDamage = super.strength/2
        super.speed = 20
        super.strength = super.health/5
        super.intelligence = 1
        super.cognitiveAbility = self.fatigue + super.intelligence
        self.inventory = False



