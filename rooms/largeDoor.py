from base.Room import Room
from rooms.finalRoom import key
# A large door, which is also the exit to the game

name = "Large Door"
description = """The room at the end of the tunnel is relativly shallow, maybe two meters in depth from the end of the tunnel. As you wave\nthe torch around, you realize that the room contains a large, wood and iron door. In the middle of the door near\nthe ground, there is a small keyhole, which is ever so ironic considering the size of the door. On the floor of the room\nis a large V."""

large_door = Room(name,description)

@large_door.action('go',"back")
def go_back(g):

    print("There is nothing much else to see in the room, so you decide to return through the tunnel you came.")

    g.set_room("intersection1")

@large_door.action('unlock',"door")
def unlock_door(g):
    
    if key in g.player.inventory:

        print("You take the key you found, and place it into the hole in the door. You turn the key, with little effort, and the door\nbegins to make a large clanking noise.")
        print("After a few seconds, the noise stops. The door is unlocked")
        g.player.door_unlocked = True

        large_door.del_action(("unlock",))

        @large_door.action('open',"door")
        def open_door(g):
            
            if g.player.door_unlocked:

                print("You walk up to the door, and begin to push it open. As it slowly opens, sunlight begins to seep in through the opening.")
                print("You step out into the light, finally having escaped the tunnels.")

                g.player.game_end = True
    else:

        print("You do not have a key to unlock the door.")


