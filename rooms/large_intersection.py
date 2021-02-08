from base.Room import Room

# Large intersection that leads to the puzzle and the final room.
name = "Large Intersection"
description = """This intersection does not appear to be like the others. It is a large square room, with stone tiles as the flooring. In\nthe tiles, there are some tiles that were cut differently, creating the number III in the middle of the floor. From the\nentrance from the previous intersection, the room has three doorways on each side of the room. One on your left, your\nright, and straight ahead."""

large_intersection = Room(name,description)

@large_intersection.action('go',"left")
def go_left(g):

    print("You continue into the room on your left")

    g.set_room("storage")

@large_intersection.action('go',"right")
def go_right(g):

    print("You decide to into the room to your right.")

    g.set_room("final_entrance")

@large_intersection.action('go',"straight")
def go_straight(g):

    print("You decide to go into the room in front of you.")

    g.set_room("puzzle_room")

@large_intersection.action('go',"back")
def go_back(g):

    g.set_room("intersection2")