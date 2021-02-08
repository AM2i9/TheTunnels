from base.Room import Room
from base.Boss import Boss
from base.Item import Item
from rooms.storage import sword
from rooms.bottomlessPit import health_potion
import random
import time

# The first room of the game

name = "Final Room"
description = ""

finalRoom = Room(name,description)

# The final boss
bird_boss = Boss("Bird","A bird that found its home in the final chamber of this underground structure. You appear to have angered it.",100,20,)

# Key to the exit
key = Item("Key","A small, golden looking key. There is really only one door this could go to.")

# On enter event
@finalRoom.on_enter()
def on_enter(g):

    print("Entering the room, it appears the same as any other room.")
    print("A large room, with torches lining the edges.")
    print("But, at the end of the room opposite of the door, there is a pedastal, with a small key atop it.")

@finalRoom.action('go',"back")
def go_back(g):

    if g.player.boss_defeated:
        g.set_room("final_entrance")
        return

    if g.player.angered_bird:
        print("The bird is blocking the exit of the room, there is no way to escape.")
        return

    if g.player.looking_at_bird:
        print("You are too interested in what this bird is doing here that you do not feel the desire to leave the room.")
        return
    
    g.set_room("final_entrance")
    
# The sequence begins
@finalRoom.action('take',"key")
def pickup_key(g):
    """
    Action to pick up the key, also the trigger for the bossfight sequence
    """

    # No duplicate keys
    if key in g.player.inventory:
        print("You already have the key.")
        return

    # Checks if the sequence has started yet
    if not g.player.looking_at_bird:

        print("You begin to walk towards the key to retrieve it. You are halfway across the room, when you hear a loud chirp from your\nleft.")
        print("You stop, and turn to look. The owner of the chirp appears to be a small white bird, standing on a small twig on the floor\nof the room.")
        g.player.looking_at_bird = True

        @finalRoom.action('attack',"bird")
        def attack_bird(g):
            """
            action to attack the bird, both to start the fight and for during it
            """
            
            # Adding potion functionality, to not leave the entire battle up to random
            if health_potion in g.player.inventory:

                @finalRoom.action('use','potion')
                def use_potion(g):

                    g.player.inventory.pop(g.player.inventory.index(health_potion))
                    print("You use the health potion you found earlier, restoring 30 health.")
                    g.player.heal(30)
                    finalRoom.del_action(('use',))

            if not g.player.angered_bird:
                print("You begin to walk toward the bird, to attempt to shoo it off. The bird does not move as you approach.")
                print("You attempt to take a swing at the bird with your hand, and you are suprised as the bird disappears.")

                # Gonna create some dramatic tension here with some delay
                time.sleep(4)

                print("Your body stiffens as you hear a chirp from behind you.")

                time.sleep(4)

                print("You feel a shadow begin to loom over you, as you slowly turn around to face a incredibly large version of the previously\nsmall bird.")

                g.player.angered_bird = True

                time.sleep(4)

                print("The bird pecks at you, and you move out of the way just in time for it to come down, but its beak hits your foot, dealing\n10 damage to your health.")

                # If you want bossfight music, I highly suggest this: https://www.youtube.com/watch?v=NBFuzr_GnqQ

                if sword in g.player.inventory:
                    print("You pull the sword that you found earlier out and get ready to fight.")

                g.player.damage(10)

                # Check commands for checking the birds health and status, and for the player too
                @finalRoom.action('check',"bird")
                def check_bird(g):
                    boss = bird_boss
                    print(f"Check:\n---------------------\n{boss.name}\nHealth:{boss.health}\nAttack:{boss.damage}\n{boss.desc}")

                @finalRoom.action('check',"self")
                def check_self(g):
                    player = g.player
                    
                    # Getting the names of the items instead of the objects
                    inventory = []

                    for item in player.inventory:
                        inventory.append(item.name)

                    inv = ', '.join(inventory)
                    print(f"Check:\n---------------------\n{player.name}\nHealth:{player.health}\nInventory:{inv}")
            
            else:

                # Attack messages.
                attack_sucess = [
                    "You take a swing at the bird, and manage to hit it across the face.",
                    "The sword hits the leg of the bird as it tries to dodge.",
                    "The blade hits the birds wing as it attempts to fly back.",
                    "The bird attempts to dodge the attack, but it is unsucessful as the blade makes its way across its chest."
                ]

                attack_fail = [
                    "You take a swing at the bird, only for the sword to be stopped by its beak.",
                    "The bird makes a thrust with its wing, moving out of the way of your attack.",
                    "The bird jumps in the air, sucessfullying avoiding your underhanded swing.",
                    "You take a swing, but overshoot and miss the bird completly."
                ]

                bird_attacks = [
                    {"message": "The bird comes down at your with its beak, dealing 20 damage as you narrowly avoid it.","damage": 20},
                    {"message": "The bird makes a massive thrust of wind with its wings, throwing you back into the wall, dealing 20 damage.","damage": 20},
                    {"message": "The bird swings at you with its wing, hitting you and making you fall to the ground, dealing 5 damage.","damage": 5},
                    {"message": "The bird jumps in the air, and on its impact with the ground it creates a strong shake, causing you to lose your footing\nand fall, dealing 5 damage","damage": 5},
                ]
                
                # Checks if the player found the weapon from the storage area
                if sword in g.player.inventory:
                    
                    # Randomly decides wether the player manages to hit the bird or not
                    hit_chance = random.randint(1,10)

                    if hit_chance < 5:

                        print(random.choice(attack_sucess))
                        print(f"You deal {hit_chance * 10} damage to the bird.")

                        bird_boss.dmg(hit_chance * 10)
                        
                        # Checks if boss has been defeated
                        if bird_boss.health == 0:
                            boss_defeated(g)
                            return

                    else:

                        # Randomly chooses an attack from the bird
                        print(random.choice(attack_fail))

                        bird_attack = random.choice(bird_attacks)

                        print(bird_attack["message"])
                        g.player.damage(bird_attack["damage"])

                        # Checks if player has died
                        if g.player.health == 0:
                            return 

                else:

                    # You cannot combat the bird without a weapon
                    print("You attempt to take a swing at the bird with your fists, but you are unsucessful as you are thrown back but the birds wings.")
                    print("The birds beak swings down at you as you lay hopelessly on the ground, killing you.")
                    g.player.health = 0
                    return

    elif g.player.boss_defeated:
        
         # After defeating the boss you can finally take the key
        print("You walk forward to the pedastal, and take the key from the top.")
        g.player.pickupItem(key)
        finalRoom.del_action(('take',))
    
    elif g.player.angered_bird:

        print("You cannot take the key, as there is a large bird currently blocking you from doing so.")
    else:

        print("You want to continue to take the key and leave, but your eyes stay locked on the bird with curiosity.")

def boss_defeated(g):
    """
    Run when the boss is defeated
    """

    finalRoom.del_action(("attack",))

    print("This attack appears to have been the final one. You watch as the bird collapses, and begins to shrink. It shrinks back to\nits normal size, now laying in the middle of the room.")
    g.player.boss_defeated = True