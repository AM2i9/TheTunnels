class Boss:

    def __init__(self,name,desc,health,damage):

        """
        A Boss class, for creating the final boss
        """
        self.name = name
        self.desc = desc
        self.health = health
        self.damage = damage

    def dmg(self,damage):
        """
        Damage the boss, from getting attacked or otherwise
        """
        self.health = self.health - damage
        
        if self.health < 0:
            self.health = 0