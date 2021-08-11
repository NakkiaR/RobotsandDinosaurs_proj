class Weapon:
#constructor
    def __init__(self):
        self.name = "Galactic Nukor"
        self.attack_power = 100
#Note: Galactic Nukor fires photon energy rays
    def attack_with_weapon(self):
        self.attack = "fire"
        print("Fire!", self.attack_power)
        

    