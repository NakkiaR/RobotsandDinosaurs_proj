#imports
from herd import Herd
from fleet import Fleet

class Battlefield:
#constructor
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()
#Fleet attacks herd
    attack_points = 0
    def game_play(self):
        if self.attack_points == 111:
            print("You hit 3 dinosaurs!You dealt 300 damage!")
        if self.attack_points == 110:
            print("You hit 2 of the dinosaurs! You dealt 200 damage!")
        else:
            self.attack_points = 100
            print("You didn't hit any dinosaurs this time!")

#Herd attacks Fleet
attack_points = 0
def game_play(self):
        if self.attack_points == 111:
            print("You hit 3 robots!You dealt 300 damage!")
        if self.attack_points == 110:
            print("You hit 2 of the robots! You dealt 200 damage!")
        else:
            self.attack_points = 100
            print("You didn't hit any robots this time!")
