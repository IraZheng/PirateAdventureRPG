###############################################################################
#Title: Pirate Adventure RPG
#Class: CS 30
#Assignment:
#Coder: Ira Zheng
#Version: 1.0
###############################################################################
'''Explain Program Here'''
###############################################################################
# Imports and Global Variables ------------------------------------------------
#map of the island
island_map = [["Tree", "Trap", "Camp", "Treasure"],
             ["Start", "Patrol", "Shovel", "Camp"],
             ["Patrol", "Trap", "Camp", "Key"]]
#x is column y is row on island_map
Player = {"posX": 0, "posY": 1, "inventory": 
          {"coconuts": 0, "hasShovel": False, "hasKey": False}}
#movement options
movement = "-Move north \n-Move south \n-Move east \n-Move west"
#encounters on the island
Encounters = {"Camp": {"Description": "Camp description", 
                       "Actions": "-Camp actions"}, 
              "Key": {"Description": "Key description", 
                      "Actions": "-Pick up the key"}, 
              "Patrol": {"Description": "Patrol description", 
                         "Actions": "-Patrol actions"}, 
              "Shovel": {"Description": "Shovel description", 
                         "Actions": "-Pick up the shovel"}, 
              "Start": {"Description": "Start description", 
                        "Actions": "-Start actions"}, 
              "Trap": {"Description": "Trap description", 
                       "Actions": "-Trap Actions"}, 
              "Treasure": {"Description": "Treasure description", 
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
            if Player["posY"] < (len(island_map) - 1):
                Player["posY"] += 1
                break
            else:
                print("Thats the end of the island, you can't go there!\n")
        elif moveChoice == "east":
            if Player["posX"] < (len(island_map[Player["posY"]]) - 1):
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
    while True:
        player_location = island_map[Player["posY"]][Player["posX"]]
        print(Encounters[player_location]["Description"])
        print(Encounters[player_location]["Actions"])
        print("-Move")
        choice = input("What do you do? \n-").lower()
        if choice == "move":
            print("Okay!\n")
            mapMove()
        #elif choice in Encounters[player_location]["Actions"]:
            #encounterActions()
        else:
            print("That's not a valid option!\n")


# Main ------------------------------------------------------------------------
mainMenu()