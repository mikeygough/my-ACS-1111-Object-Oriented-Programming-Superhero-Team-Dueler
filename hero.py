from ability import Ability
from armor import Armor
import random


class Hero:
    def __init__(self, name: str, starting_health: int = 100):
        """Instance properties:
        name: string
        starting_health: integer
        current_health: integer
        abilities: list
        armors: list
        """

        self.name = name
        self.starting_health = starting_health
        # at initialization, current health is equal to starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        """Add ability to abilities list"""

        self.abilities.append(ability)

    def attack(self):
        """Calculate the total damage from all ability attacks.
        return: total_damage: int
        """
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage
    
    def add_armor(self, armor):
        """Add ability to armors list"""
        
        self.armors.append(armor)

    def defend(self):
        """Calculate the total block amount from all armor blocks.
        return: total_block: int
        """
        total_block = 0
        if self.current_health <= 0:
            return total_block
        else:
            for armor in self.armors:
                 total_block += armor.block()
        return total_block
        
    # def defend(self, incoming_damage: int):
    #     pass

    def take_damage(self, damage: int):
        """ Updates self.current_health to reflect the damage minus the defense."""
        impact = damage - self.defend()
        print(impact)
        if impact <= 0:
            return
        else:
            self.current_health -= impact

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
    # create abilities
    throw_kunai_attack = Ability("Throw Kunai", 50)
    rasengan_attack = Ability("Rasengan", 90)
    # create armors
    shadow_clone_armor = Armor("Shadow Clone", 50)
    substitution_armor = Armor("Substitution", 100)
    # create hero
    naruto = Hero("Naruto Uzumaki", 100)
    # add abilities
    naruto.add_ability(throw_kunai_attack)
    naruto.add_ability(rasengan_attack)
    # add armors
    naruto.add_armor(shadow_clone_armor)
    naruto.add_armor(substitution_armor)
    
    # print(naruto.abilities)
    # print(naruto.armors)
    
    print(naruto.current_health)
    print("Attack Value:", naruto.attack())
    print("Defend Value:", naruto.defend())
    naruto.take_damage(30)
    print(naruto.current_health)
    # sasuke = Hero("Sasuke Uchiha", 80)
    # sasuke.fight(naruto)
