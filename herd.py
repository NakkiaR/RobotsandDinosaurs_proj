#imports
from dinosaur import Dinosaur

class Herd:
#constructor
    def __init__(self):
        self.herd = [Dinosaur("Anklyosaurus", 100, 300, "Tail lash"), Dinosaur("Anklyosaurus", 100, 300, "Tail lash"), Dinosaur("Anklyosaurus", 100, 300, "Tail lash")]
        
#Methods
#Note: The Anklyosaurus delivers a painful blow to the robots
        def attack_robot(self):
            self.attack = "Hit with tail"