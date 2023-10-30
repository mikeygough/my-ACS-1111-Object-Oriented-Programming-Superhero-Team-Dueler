from ability import Ability
import random


class Weapon(Ability):
    def __init__(self, name: str, max_damage: int):
        super().__init__(name, max_damage)

    def attack(self):
        """This method returns a random value
        between one half to the full atack power of the weapon."""
        return random.randint(self.max_damage // 2, self.max_damage)
