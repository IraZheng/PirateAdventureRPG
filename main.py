###############################################################################
#Title: Pirate Adventure RPG
#Class: CS 30
#Assignment:
#Coder: Ira Zheng
#Version: 1.0
###############################################################################
'''A pirate adventure game?'''
###############################################################################
# Imports and Global Variables ------------------------------------------------
#map of the island
islandMap = [["Tree", "Trap", "Camp", "Treasure"],
             ["Start", "Patrol", "Shovel", "Camp"],
             ["Patrol", "Trap", "Camp", "Key"]]
#x is column y is row on island_map
Player = {"posX": 0, "posY": 1, "inventory": 
          {"coconuts": 0, "hasShovel": False, "hasKey": False}}
#movement options
movement = "-Move north \n-Move south \n-Move east \n-Move west"
#encounters on the island
Encounters = {"Camp": {"Description": "You have entered a pirate camp", 
                       "Actions": "-Camp actions"}, 
              "Key": {"Description": "Something shiny catches your eye\n" +
                      "After closer inspection, you find that it's a key", 
                      "Actions": "-Pick up the key"}, 
              "Patrol": {"Description": "You encounter patrolling pirates", 
                         "Actions": "-Patrol actions"}, 
              "Shovel": {"Description": "You find a shovel on the ground", 
                         "Actions": "-Pick up the shovel"}, 
              "Start": {"Description": "This is where you washed up", 
                        "Actions": "-Start actions"}, 
              "Trap": {"Description": "You fall into a pit full of spikes", 
                       "Actions": "-Trap Actions"}, 
              "Treasure": {"Description": "On the ground is a big red X", 
                           "Actions": "-Treasure actions"},
              "Tree": {"Description": "On the sandy shore, " + 
                       "you spot a coconut tree", 
                       "Actions": "-Pick a coconut"}
             }


# Functions -------------------------------------------------------------------
def mapMove():
    """Allows players to move through the map"""
    global Player
    while True:
        print("Which direction do you move?")
        #prints movement variable
        print(movement)
        print("-Back")
        #default input is a string so I can use .lower()
        moveChoice = input("-").lower()
        #for map movement
        if moveChoice == "north":
            if Player["posY"] > 0:
                Player["posY"] -= 1
                break
            else:
                print("Thats the end of the island, you can't go there!\n")
        elif moveChoice == "south":
            if Player["posY"] < (len(islandMap) - 1):
                Player["posY"] += 1
                break
            else:
                print("Thats the end of the island, you can't go there!\n")
        elif moveChoice == "east":
            if Player["posX"] < (len(islandMap[Player["posY"]]) - 1):
                Player["posX"] += 1
                break
            else:
                print("Thats the end of the island, you can't go there!\n")
        elif moveChoice == "west":
            if Player["posX"] > 0:
                Player["posX"] -= 1
                break
            else:
                print("Thats the end of the island, you can't go there!\n")
        elif moveChoice == "back":
            break
        else:
            print('Please choose "north", "south", "east", "west" or "back"\n')


def mainMenu():
    """Main menu, this will probably do more later so this 
    is a placeholder docstring
    """
    #prints an introduction
    print("After a massive hurricane, you are seperated from your crew")
    print("You wash up on a pirate infested island")
    print("You realise that there is treasure on the island and " + 
          "decide to steal it")
    while True:
        playerLocation = islandMap[Player["posY"]][Player["posX"]]
        print(Encounters[playerLocation]["Description"])
        print("What do you do?")
        print(Encounters[playerLocation]["Actions"])
        print("-Move\n-Quit")
        #takes user's choice
        choice = input("-").lower()
        if choice == "move":
            print("Okay!\n")
            mapMove()
        #elif choice in Encounters[player_location]["Actions"]:
            #encounterActions()
        elif choice == "quit":
            print("You have quit your adventure")
            break
        else:
            print("That's not a valid option!\n")


# Main ------------------------------------------------------------------------
mainMenu()