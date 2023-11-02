from ability import Ability
from armor import Armor
from weapon import Weapon
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
        self.deaths = 0
        self.kills = 0

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

    def take_damage(self, damage: int):
        """Updates self.current_health to reflect the damage minus the defense."""
        impact = damage - self.defend()
        if impact <= 0:
            # is defense greater than damage
            return
        else:
            # damage greater than defense, reduce current_health
            self.current_health -= impact

    def add_weapon(self, weapon):
        """Add eapon to self.abilities"""
        self.abilities.append(weapon)

    def is_alive(self):
        """Return True or False depending on whether the hero is alive or not."""
        if self.current_health > 0:
            return True
        else:
            return False

    def add_kill(self, num_kills):
        """Update self.kills by num_kills amount"""
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        """Update self.deaths by num_deaths amount"""
        self.deaths += num_deaths

    def fight(self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in."""
        # check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if (len(self.abilities) < 1) and (len(opponent.abilities) < 1):
            print("Draw")
            return

        # start the fighting until a hero has won
        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())
            if not opponent.is_alive():
                self.add_kill(1)
                opponent.add_deaths(1)
                print(f"{self.name} won!")
                return
            self.take_damage(opponent.attack())
            if not self.is_alive():
                opponent.add_kill(1)
                self.add_deaths(1)
                print(f"{opponent.name} won!")
                return


# prevent the code from being run when the script is imported by another script
if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

    # # create abilities
    # throw_kunai_attack = Ability("Throw Kunai", 50)
    # rasengan_attack = Ability("Rasengan", 90)
    # chidori_attack = Ability("Chidori", 50)

    # # create armors
    # shadow_clone_armor = Armor("Shadow Clone", 50)
    # substitution_armor = Armor("Substitution", 100)

    # # create naruto
    # naruto = Hero("Naruto Uzumaki", 100)

    # # add naruto abilities
    # naruto.add_ability(throw_kunai_attack)
    # naruto.add_ability(rasengan_attack)
    # # add naruto armors
    # naruto.add_armor(shadow_clone_armor)
    # naruto.add_armor(substitution_armor)

    # # create sasuke
    # sasuke = Hero("Sasuke Uchiha", 80)

    # # add sasuke abilities
    # sasuke.add_ability(throw_kunai_attack)
    # sasuke.add_ability(chidori_attack)
    # # add sasuke armors
    # sasuke.add_armor(shadow_clone_armor)
    # sasuke.add_armor(substitution_armor)

    # # FIGHT
    # sasuke.fight(naruto)
