from base.Room import Room
from base.Item import Item

# The first room of the game

name = "Field of Green"
description = """The field only goes about 20 feet, then is stopped by a wall of rock. Sunlight rains down above you, from a large hole in\nthe ceiling. The only difference in the walls in the room is a tunnel that would appear to lead further into the cave,\nwith a single torch at the entrance."""

torch = Item("Torch","A samll torch, which emits a warm light.")

startRoom = Room(name,description)

@startRoom.on_enter()
def on_enter(g):
    print("You wake up with a bright light shining down on your face. You try to think back to how you got here, but you cannot\nremember. You get up and look around.\n")

@startRoom.action('enter','tunnel')
def enter_tunnel(g):

    if torch in g.player.inventory:
        print("""Now, with the warm light of the torch, you begin your trek down the tunnel.""")
        g.set_room('intersection1')
    else:
        print("""You begin to go down the tunnel, to find that it is lit by a single torch at the entrance. The rest of the tunnel is too\ndark to continue""")

    return g

@startRoom.action('take','torch')
def grab_torch(g):

    if torch in g.player.inventory:
        print("You are already holding the torch")
    else:
        g.player.pickupItem(torch)
        startRoom.del_action(("take",))
        print("You pick up the torch, and you feel its warmth spread over you as you hold it closer. Your fear of the darkness ahead lifts\nslightly.")

    return g