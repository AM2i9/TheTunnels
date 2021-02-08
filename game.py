from base.Player import Player


class Game:

    def __init__(self):
        """
        Main game object. Stores all universal data to be used accross rooms
        """

        # Creates a player, which stores things like inventory
        self.player = Player("PlayerName")

        self.rooms = {}

        self.current_room = ""

        self.puzzle_data = {"current_number":"","puzzle_complete":False}

    def set_room(self,room_name):
        """
        Changes the room the player is currently in.
        param room_name: Name of the room to move to
        """

        # Sets current room then does the 'look' action automatically
        self.current_room = self.rooms[room_name]
        self.current_room.enter(self)

    def addRoom(self,room,room_name):
        """
        Adds a room to the game, making it easier to manage rooms
        param room: a Room object
        param room_name: the name in which this room will be stored and called by
        """

        self.rooms[room_name] = room
