#Imports
from weapon import Weapon
#constructor
class Robot:
    def __init__(self):
        self.name = ''
        self.health = 300 #It can be hit 3x before dying
        self.weapon = Weapon()
 #Methods
 #The robot attacks the dinosaur
    def add_robot_team(self):
        self.robot_one = Weapon()
        self.robot_two = Weapon()
        self.robot_three = Weapon()

       
