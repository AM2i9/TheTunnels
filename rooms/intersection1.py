from base.Room import Room

# First intersection, comes right after the startroom

name = "Intersection"
description = """You arrive at an intersection, with a path heading off to the right, and one continuing forward, with the tunnel to the\ngrassy area behind you. A faint light is at the end of the tunnel to your right."""

intersection1 = Room(name,description)

@intersection1.action('go',"straight")
def continue_straight(g):

    print("You continue straight down the tunnel")

    g.set_room("intersection2")

@intersection1.action('go',"right")
def go_right(g):

    print("You decide to go down the tunnel to your right.")

    g.set_room("large_door")

@intersection1.action('go','back')
def go_back(g):

    g.set_room('start_room')