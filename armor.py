import random


class Armor:
    def __init__(self, name: str, max_block: int):
        """Instance properties:
        name: string
        max_block: integer
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        """Return a value between 0 and the value set by self.max_block."""

        return random.randint(0, self.max_block)


if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())