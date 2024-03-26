###############################################################################
#Title: Pirate Adventure RPG
#Class: CS 30
#Assignment:
#Coder: Ira Zheng
#Version: 3.0
###############################################################################
'''A pirate adventure game?'''
###############################################################################
# Imports and Global Variables ------------------------------------------------
#cool edit no way
#for map table
from tabulate import tabulate

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
                       "Actions": ["Fight the pirates"], 
                       "Completed1": False}, 
              "Key": {"Description": "Something shiny catches your eye\n" + 
                      "After closer inspection, you find that it's a key", 
                      "Actions": ["Pick up the key"], 
                      "Completed1": False}, 
              "Patrol": {"Description": "You encounter patrolling pirates", 
                         "Actions": ["Fight the pirates"], 
                         "Completed1": False}, 
              "Shovel": {"Description": "You find a shovel on the ground", 
                         "Actions": ["Pick up the shovel"], 
                        "Completed1": False}, 
              "Start": {"Description": "This is where you washed up", 
                        "Actions": ["Start actions"], 
                        "Completed1": False}, 
              "Trap": {"Description": "You fall into a pit full of spikes", 
                       "Actions": ["Disable trap"], 
                       "Completed1": False}, 
              "Treasure": {"Description": "On the ground is a big red X", 
                           "Actions": ["Dig", "Unlock"], 
                           "Completed1": False, 
                           "Completed2": False},
              "Tree": {"Description": "On the sandy shore, " + 
                       "you spot a coconut tree", 
                       "Actions": ["Pick a coconut"], 
                       "Completed1": False}
             }
#booleans for treasure room
hasDug = False
hasUnlocked = False
#map export file
mapFile = 'map.txt'


# Functions -------------------------------------------------------------------
def mapExport():
    '''Exports the map to an external file'''
    try:
        with open(mapFile, "w") as file:
            file.write(tabulate(islandMap, tablefmt = "fancy_grid"))
    except:
        print("Unable to export map")
    else:
        print("You have a map")
    finally:
        print("Maybe that will help")


def viewMap():
    '''Prints the map from an external file'''
    try:
        with open(mapFile, "r") as file:
            print(file.read())
    except:
        print("Unable to read map")
    else:
        print("Nice map")
    finally:
        print("Maybe that will help")


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


def encounterActions(action, room):
    '''lets the player do different things in different encounters'''
    global Player
    global hasDug
    global hasUnlocked
    #print("Passed the check")
    #print(room)
    #print(action)
    if room == "Camp":
        if action == "fight the pirates":
            print("You beat the pirates")
    elif room == "Key":
        if action == "pick up the key":
            Player["inventory"]["hasKey"] = True
            print("You have picked up the key")
    elif room == "Patrol":
        if action == "fight the pirates":
            print("You beat the pirates")
    elif room == "Shovel":
        if action == "pick up the shovel":
            Player["inventory"]["hasShovel"] = True
            print("You have picked up the shovel")
    elif room == "Start":
        pass
    elif room == "Trap":
        if action == "disable trap":
            print("Trap disabled!")
    elif room == "Treasure":
        if action == "dig":
            if not hasDug:
                if Player["inventory"]["hasShovel"]:
                    print("You have dug up the treasure")
                    hasDug = True
                else:
                    print("You do not have a shovel")
            else:
                print("You have already dug up the treasure")
        elif action == "unlock":
            if hasDug:
                if not hasUnlocked:
                    if Player["inventory"]["hasKey"]:
                        print("You have unlocked up the treasure")
                        hasUnlocked = True
                    else:
                        print("You do not have a key")
                else:
                    print("You have already unlocked the treasure")
            else:
                print("You have not dug up the treasure yet")
    elif room == "Tree":
        if action == "pick a coconut":
            Player["inventory"]["coconuts"] += 1
            print(f'You have {Player["inventory"]["coconuts"]} coconuts')


def mainMenu():
    """
    Main menu, this will probably do more later so this 
    is a placeholder docstring
    """
    while True:
        playerLocation = islandMap[Player["posY"]][Player["posX"]]
        print(Encounters[playerLocation]["Description"])
        print("What do you do?")
        for action in Encounters[playerLocation]["Actions"]:
            if (not Encounters[playerLocation]
                [f'Completed{len(Encounters[playerLocation]["Actions"])}']):
                print(f"-{action}")
        print("-Inventory\n-Move\n-Map\n-Quit")
        #takes user's choice
        choice = input("-").lower()
        if choice == "move":
            print("Okay!\n")
            mapMove()
        elif choice.capitalize() in Encounters[playerLocation]["Actions"]:
            encounterActions(choice, playerLocation)
        elif choice == "inventory":
            print("In your inventory, you have:")
            print(f'-{Player["inventory"]["coconuts"]} coconuts')
            if Player["inventory"]["hasShovel"]:
                print("-A shovel")
            else:
                print("-No shovel")
            if Player["inventory"]["hasKey"]:
                print("-A key")
            else:
                print("-No key")
        elif choice == "map":
            viewMap()
        elif choice == "quit":
            print("You have quit your adventure")
            break
        else:
            print("That's not a valid option!\n")


def intro():
    '''prints an intro'''
    print("After a massive hurricane, you are seperated from your crew")
    print("You wash up on a pirate infested island")
    print("You realise that there is treasure on the island and " + 
          "decide to steal it")


# Main ------------------------------------------------------------------------
intro()
mapExport()
mainMenu()