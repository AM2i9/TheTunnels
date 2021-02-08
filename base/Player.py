from base.Item import Item

class Player:

    def __init__(self,name):
        """
		Main player class, to store things like inventory and other things
		param name: The name of the player. Purely for astetics
		"""
        self.name = name
        self.health = 100
        self.inventory = []

        self.looking_at_bird = False
        self.angered_bird = False
        self.boss_defeated = False
        self.door_unlocked = False

        self.game_end = False

    def pickupItem(self,item):
        """
        Adds item to players inventory
        """

        # Check if the given item is actually an Item
        if isinstance(item,Item):
            self.inventory.append(item)

    def damage(self,dmg):

        """
        Damage the player, from getting attacked or otherwise
        """

        self.health = self.health - dmg

        if self.health < 0:
            self.health = 0
    
    def heal(self,health):
        """
        Heal the player
        """
        self.health = self.health + health