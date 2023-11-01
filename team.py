class Team():
    def __init__(self, name):
        """ Initialize your team with its team name and an empty list of heroes """
        self.name = name
        self.heroes = list()
    
    def add_hero(self, hero):
        """ Add Hero object to self.heroes. """
        self.heroes.append(hero)
        
    def remove_hero(self, name):
        """ Remove hero from heroes list.
        If Hero isn't found return 0."""
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        """ Prints out all heroes to the console. """
        [print(hero.name) for hero in self.heroes]
        
    def stats(self):
        """ Print team statistics """
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
            
    def revive_heroes(self):
        """ Reset all heroes health to starting_health """
        for hero in self.heroes:
            hero.current_health = hero.starting_health