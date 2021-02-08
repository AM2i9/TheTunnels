from base.Room import Room

# The first room of the game

name = "Final Room Entrance"
description = ""

finalEntrance = Room(name,description)

@finalEntrance.on_enter()
def on_enter(g):

    if g.puzzle_data["puzzle_complete"]:

        finalEntrance.description = "The room contains a rather large door. It is lit on all sides with torches, unlike the other rooms and tunnels. Stones\nand dust rest on the ground around it, with a massive door, standing open on the end of the room, almost begging you to\nenter it."

        if "enter" not in finalEntrance.actions:

            @finalEntrance.action('enter',"doorway")
            def enter_final_room(g):

                g.set_room("final_room")

    else:

        finalEntrance.description = "The room contains a rather large door. It is lit on all sides with torches, unlike the other rooms and tunnels. You seem\nto have come in through the only entrance, but upon close observation you notice what looks to be a large stone door at the\nend of the room. The door is massive, with many differnent symbols carved into it. There has got to be some way to open it."

@finalEntrance.action('go',"back")
def go_back(g):

    print("You decide to return to the intersection")

    g.set_room("large_intersection")
