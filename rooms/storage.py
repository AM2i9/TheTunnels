from base.Room import Room
from base.Item import Item

# Storage room, attached to the large intersection

name = "Storage Room"
description = """The room appears to be some kind of storage. Entering, a few mice scurry away. Looking around reveals a few new-looking\nswords, and nothing much else except for a large amount of barrels."""

storage = Room(name,description)

sword = Item("Sword","A shiny, sharp sword. It looks as though it has never been used.")

@storage.action('take',"sword")
def pickup_sword(g):

    if sword not in g.player.inventory:

        g.player.pickupItem(sword)
        storage.del_action(("take",))

        print("You pickup a sword form among the boxes, and hold it in your hand. The torchlight glints off of it as you turn it, admiring\nit. You place it away on your back.")

    else:

        print("You already have a sword, strapped to you back.")


@storage.action('go',"back")
def go_back(g):

    print("You decide there is not much more to do in a storage room, and decide to return to the intersection.")

    g.set_room("large_intersection")
