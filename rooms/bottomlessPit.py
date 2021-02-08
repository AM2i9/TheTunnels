from base.Room import Room
from base.Item import Item

# It's bottomless.

name = "Bottomless Pit"
description = """You enter the room, and a wave of anxiety rushes over you as you stare into a large pit before you. It descends deep\ninto the darkness, the bottom not even touched by the torchlight. Perhaps you could drop a rock to see how deep it is?"""

bottomless_pit = Room(name,description)

health_potion = Item("Health Potion","Will heal you back 50 health")
@bottomless_pit.action('go',"back")
def go_back(g):

    print("You decide to turn back, and return down the tunnel.")

    g.set_room("intersection2")

@bottomless_pit.action('drop',"rock")
def drop_rock(g):

    print("You pick up a sizeable rock next to you, and toss it down the hole. The rock falls, and you hear nothing for a few seconds.\nYou hear the rock hit, but a few seconds later it hits again, hitting the walls. The rock hits the wall a total of SIX\ntimes before the sound disappears.")

    if health_potion not in g.player.inventory:

        print("However, next to the spot on the ground where the rock that you just dropped was beforehand, you notice a small glass vile.")

        @bottomless_pit.action('take','vile')
        def take_potion(g):

            g.player.pickupItem(health_potion)
            print("You pick up the bottle, and examine it for a few seconds to find it is a health potion.")
            bottomless_pit.del_action(('take',))
