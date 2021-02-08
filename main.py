from game import Game
import rooms
# import os

def main():

    g = Game()


	# Adding rooms
    g.addRoom(rooms.start_room,"start_room")
    g.addRoom(rooms.intersection1,"intersection1")
    g.addRoom(rooms.large_door,"large_door")
    g.addRoom(rooms.intersection2,"intersection2")
    g.addRoom(rooms.bottomless_pit,"bottomless_pit")
    g.addRoom(rooms.large_intersection,"large_intersection")
    g.addRoom(rooms.storage,"storage")
    g.addRoom(rooms.puzzle_room,"puzzle_room")
    g.addRoom(rooms.final_entrance,"final_entrance")
    g.addRoom(rooms.final_room,"final_room")

	# Clear the console, get rid of that clutter from previous tests
	# Does not work in repl.it
    # os.system("cls")
    # repl.it friendly version, other IDE may not like it
    clear_screen()
    
    title_graphic = """
 _______ _            _______                     _     
|__   __| |          |__   __|                   | |         .-.
   | |  | |__   ___     | |_   _ _ __  _ __   ___| |___     /'v'\ 
   | |  | '_ \ / _ \    | | | | | '_ \| '_ \ / _ \ / __|   (/   \)
   | |  | | | |  __/    | | |_| | | | | | | |  __/ \__ \  ='="="===< 
   |_|  |_| |_|\___|    |_|\__,_|_| |_|_| |_|\___|_|___/  mrf|_|"""

    print(title_graphic)
    print("↓--------------------------------------------------------------------------------------------------------------------------")
    print("↑ | Change your console size to fit the line above, so that the two arrows have nothing in between.")

    input("\n<Press Enter>")

    print_divider()

    player_name = input("What is your name?\n>")
    g.player.name = player_name

    print_divider()

	# Putting player in first room
    g.set_room("start_room")

	# Main loop
    while True:

        print_divider()

		# Taking user input
        verb = ""
        noun = ""
        
        user_input = input("What do you want to do? You can: {0}\n>".format(g.current_room.get_actions()))

		# Splitting the input, so we get both a verb and a noun, or just a verb
        try:
            verb, noun = user_input.split(" ")
        except:
        	verb = user_input

		# Executing the inputted verb
        g.current_room.do_action(g,verb,noun)


        if g.player.health == 0:
            player_dead()
            break
        
        if g.player.game_end:
            game_end()
            break

def player_dead():

    print("""
__   _______ _   _  ______ _____ ___________ 
\ \ / /  _  | | | | |  _  \_   _|  ___|  _  \ 
 \ V /| | | | | | | | | | | | | | |__ | | | |
  \ / | | | | | | | | | | | | | |  __|| | | |
  | | \ \_/ / |_| | | |/ / _| |_| |___| |/ / 
  \_/  \___/ \___/  |___/  \___/\____/|___/  
                                             """"")

def game_end():

    print_divider()
    print("You have completed the game!")
    print('''
 _________   ____  ____   ________     ________   ____  _____   ______    
|  _   _  | |_   ||   _| |_   __  |   |_   __  | |_   \|_   _| |_   _ `.  
|_/ | | \_|   | |__| |     | |_ \_|     | |_ \_|   |   \ | |     | | `. \ 
    | |       |  __  |     |  _| _      |  _| _    | |\ \| |     | |  | | 
   _| |_     _| |  | |_   _| |__/ |    _| |__/ |  _| |_\   |_   _| |_.' / 
  |_____|   |____||____| |________|   |________| |_____|\____| |______.'  
                                                                          ''')

def clear_screen():
    # prints 100 newlines to give the illusion of a cleared console.
    # Also makes the text generate from the bottom, which I think looks cooler
    print("\n"*100)

def print_divider():
    print("___________________________________________________________________________________________________________________________\n")
if __name__ == "__main__":
    
    main()
    print_divider()
	