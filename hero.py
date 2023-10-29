import random


class Hero:
    def __init__(self, name: str, starting_health: int = 100):
        """Instance properties:
        name: string
        starting_health: integer
        current_health: integer
        """

        self.name = name
        self.starting_health = starting_health
        # at initialization, current health is equal to starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        pass

    def attack(self):
        pass

    def defend(self, incoming_damage: int):
        pass

    def take_damage(self, damage: int):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in."""
        # total health
        total_p = self.starting_health + opponent.starting_health
        # self probability
        self_p = self.starting_health / total_p
        # opponent probability
        opponent_p = opponent.starting_health / total_p
        # outcome
        outcome = random.uniform(0, 1)

        if outcome <= self_p:
            # self wins
            print(f"{self.name} defeats {opponent.name}!")
        else:
            # opponent wins
            print(f"{opponent.name} defeats {self.name}!")


# prevent the code from being run when the script is imported by another script
if __name__ == "__main__":
    naruto = Hero("Naruto Uzumaki", 100)
    sasuke = Hero("Sasuke Uchiha", 80)
    sasuke.fight(naruto)
