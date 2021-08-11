class Dinosaur:
#constructor
    def __init__(self):
        self.name = ""
        self.attack_power = 100
        self.health = 500
#Methods
#Note: Dinosaur attacks the robot
    def attack_with_teeth(self):
        self.attack = "Bite"

    def attack_with_tail(self):
        self.attack = "Hit with tail"

    def attack_with_claws(self):
        self.attack = "Scratch"