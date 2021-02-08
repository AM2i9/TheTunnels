import inspect

class Room:

    def __init__(self,name,description):
        """
        A base 'Room' class. Every room in the game is built off of this class
        """
        self.name = name
        self.description = description
        self.actions = {}
        self.events = {}

    def enter(self,g):

        try:
            if self.events["on_enter"]:
                for func in self.events["on_enter"]:

                    func(g)
        except:
            pass
        finally:
            self.look()

    def look(self):
        """
        'Looks' around the room.
        """
        print(self.description)

    def get_actions(self):
        """
        Creates a string to display to the user of possible actions they can do 
        """

        actions = []
        action_string = ''

        for action in self.actions:

            nouns = []

            for noun in self.actions[action]:

                if noun == "*":
                    noun = "(1-9)"
                
                nouns.append(noun)

            action_string = action + ' ' + '/'.join(nouns)
            
            actions.append(action_string)
        
        return ', '.join(actions)

        

    def on_enter(self):

        def wrapper(func):
            if "on_enter" not in self.events:

                self.events["on_enter"] = []

            self.events["on_enter"].append(func)

        return wrapper

    def action(self,verb,noun=""):
        """
        Creates an action for the room.
        param verb: A string containing the verb that should trigger the action
        param noun: The name of an object in the room
        """
        # Decorator wrapper
        def wrapper(func):

            # Adds verb to a dict, which has another dict inside it with each noun

            if verb not in self.actions:

                self.actions[verb] = {}

            # The function the action is related to is stored to be run later when the player uses the action
            self.actions[verb][noun] = func

        return wrapper

    def del_action(self,verbs=()):
        """
        Removes actions based off inputted verbs
        """
        for verb in verbs:
            self.actions.pop(verb)

    def do_action(self,g,verb,noun):
        """
        Executes actions created by action()
        param g: Game object
        param verb: The verb inputted by the user
        param noun: The noun inputted by the user
        """

        # DEBUG COMMANDS
        if "debug" in verb:

            debug = verb.split('.')

            # Debug command to set room
            if debug[1] == "set_room":
                g.set_room(debug[2])
            return g

        # Sets verb and noun to lowercase, to make it easier to compare
        verb = verb.lower()
        noun = noun.lower()

        # Seperate the previous text from the current text
        print("___________________________________________________________________________________________________________________________\n")

        # Universal look and actions commands
        if verb == "look":
            self.look()
            return

        # Checks if verb is an actual action
        if verb in self.actions:

            v = self.actions[verb]

            # For passing variables later if the action can act upon anything
            arg_key = noun

            # If no noun, check if the verb can be on its own
            if noun == "":
                if "" not in v:
                    print(f"What do you want to {verb}?")
                    return

            # If the noun dosen't exist
            if noun not in v:
                # Check if the action can take any input
                if "*" in v:
                    arg_key = "*"
                else:
                    print(f'You cannot {verb} "{noun}"')
                    return

            # Checks if the function accepts a noun as a parameter and pass it
            if "noun" in inspect.getfullargspec(v[arg_key]).args:
                g = v[arg_key](g,noun)
            else:
                g = v[arg_key](g)

        else:
            print("I do not recognize that verb.")
