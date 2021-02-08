from base.Room import Room

# Second intersection, comes after the first one
name = "Intersection"
description = """You arrive at an intersection. From here, with the path to the place you started behind you, the tunnel splits off to the\nleft and to the right."""

intersection2 = Room(name,description)

@intersection2.action('go',"left")
def go_left(g):

    print("You continue left down the tunnel")

    g.set_room("large_intersection")

@intersection2.action('go',"right")
def go_right(g):

    print("You decide to go down the tunnel to your right.")

    g.set_room("bottomless_pit")

@intersection2.action('go','back')
def go_back(g):

    g.set_room("intersection1")