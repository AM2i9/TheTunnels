from base.Room import Room

# A puzzle. Attached to large intersection

name = "Weird Puzzle"
description = """The first thing you notice about the room is a large grid on the floor. There are nine squares, each with one number\nbetween 1 and 9 on it in Roman numerals. It seems to be some form of large keypad, the code hidden somewhere across the\ntunnels. On the back wall, three large diamond shaped gemstones sit, possibly to represent the numbers entered. """

puzzle_room = Room(name,description)

@puzzle_room.action('press','*')
def enter_number(g,noun):

    # Checks if puzzle has already been solved
    if g.puzzle_data["puzzle_complete"]:
        print("You have already completed the puzzle.")
        return

    try:

        # Checks if the number is an actual number and if it is negative at the same time
        if int(noun) < 0:
            print(f"The number {noun} does not exist on the keypad")
            return

        # Checks to make sure the number is within size contraints
        if len(noun) > 3:
            print(f"You enter the number {noun}, but all three gemstones light up, then turn off. Seeing the number of gemstones, the number\nshould be only 3 digits.")
        elif len(noun) < 1:
            print("You must enter a number.")
        else:

            # Enters each number seperatley
            for digit in noun:

                number = int(digit)

                # Checks to make sure the number is on a keypad
                if number <= 9 and number >= 0:

                    print(f"You enter the number {number}, and a gemstone on the back wall lights up.")

                    # Adds number to a variable to store it
                    g.puzzle_data["current_number"] = ''.join((g.puzzle_data["current_number"],str(number)))

                    print("You have currently entered the number", g.puzzle_data["current_number"])

                    # If 3 numbers have been inputted, check to make sure it is correct
                    if len(g.puzzle_data["current_number"]) >= 3:

                        # The code is 563. The 5 is the V on the floor of the large door, the 6 is the number of times the rock hit the wall in the bottomless pit, and 3 is the III in the large intersection
                        # In order, that makes 563
                        if g.puzzle_data["current_number"] == "563":

                            # Sets in game data that the puzzle has been solved
                            print("All three gemstones now turn off, but then turn back on a few seconds later with a flashing motion. You feel a great rumble\nas you hear somthing move in another part of the tunnels.")
                            g.puzzle_data["puzzle_complete"] = True
                            puzzle_room.del_action(("press",))

                        else:

                            # Forgot password? Just kidding. You don't get to reset it. At least I don't lock you out after 3 attempts.
                            print("The three gemstones come on, but then turn back off. All is silent, signaling that the combination was incorrect.")
                            g.puzzle_data["current_number"] = ""

                else:

                    print(f"The number {number} does not exist on the keypad")

    except ValueError:
        print("That is not a number!")

@puzzle_room.action('go',"back")
def go_back(g):

    # Shows a different 'go back' message if the player has just completed the puzzle
    if g.puzzle_data["puzzle_complete"]:

        if g.puzzle_data["current_number"]:

            print("Having completed the puzzle, you decide to go back and investigate the sound.")
            g.puzzle_data["current_number"] = None
            g.set_room("large_intersection")
            return

    print("You turn back around, and go back to the intersection.")
    g.set_room("large_intersection")

