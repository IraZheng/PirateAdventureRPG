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
#map.py module
import map

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
Encounters = {"Camp": {"Description": "\nYou have entered a pirate camp", 
                       "Actions": ["Fight the pirates"], 
                       "Completed1": False}, 
              "Key": {"Description": "\nSomething shiny catches your eye\n" + 
                      "After closer inspection, you find that it's a key", 
                      "Actions": ["Pick up the key"], 
                      "Completed1": False}, 
              "Patrol": {"Description": "\nYou encounter patrolling pirates", 
                         "Actions": ["Fight the pirates"], 
                         "Completed1": False}, 
              "Shovel": {"Description": "\nYou find a shovel on the ground", 
                         "Actions": ["Pick up the shovel"], 
                        "Completed1": False}, 
              "Start": {"Description": "\nThis is where you washed up", 
                        "Actions": ["Start actions"], 
                        "Completed1": False}, 
              "Trap": {"Description": "\nYou fall into a pit full of spikes", 
                       "Actions": ["Disable trap"], 
                       "Completed1": False}, 
              "Treasure": {"Description": "\nOn the ground is a big red X", 
                           "Actions": ["Dig", "Unlock"], 
                           "Completed1": False, 
                           "Completed2": False},
              "Tree": {"Description": "\nOn the sandy shore, " + 
                       "you spot a coconut tree", 
                       "Actions": ["Pick a coconut"], 
                       "Completed1": False}
             }


# Functions -------------------------------------------------------------------
def move():
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
    global Encounters
    #print("Passed the check")
    #print(room)
    #print(action)
    if room == "Camp":
        if action == "fight the pirates":
            print("You beat the pirates")
    elif room == "Key":
        if action == "pick up the key":
            Player["inventory"]["hasKey"] = True
            #already picked up the key
            Encounters["Key"]["Completed1"] = True
            print("You have picked up the key")
    elif room == "Patrol":
        if action == "fight the pirates":
            print("You beat the pirates")
    elif room == "Shovel":
        if action == "pick up the shovel":
            Player["inventory"]["hasShovel"] = True
            #already picked up shovel
            Encounters["Shovel"]["Completed1"] = True
            print("You have picked up the shovel")
    elif room == "Start":
        pass
    elif room == "Trap":
        if action == "disable trap":
            print("Trap disabled!")
            #how do I disable one trap without disabling the other?
    elif room == "Treasure":
        if action == "dig":
            #Completed1 checks if you have already dug 
            #Completed2 checks if you have already unlocked
            if not Encounters["Treasure"]["Completed1"]:
                if Player["inventory"]["hasShovel"]:
                    print("You have dug up the treasure")
                    Encounters["Treasure"]["Completed1"] = True
                else:
                    print("You do not have a shovel")
            else:
                print("You have already dug up the treasure")
        elif action == "unlock":
            if Encounters["Treasure"]["Completed1"]:
                if not Encounters["Treasure"]["Completed2"]:
                    if Player["inventory"]["hasKey"]:
                        print("You have unlocked the treasure")
                        Encounters["Treasure"]["Completed2"] = True
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


def printInv():
    """prints player's inventory"""
    print("\nIn your inventory, you have:")
    print(f'-{Player["inventory"]["coconuts"]} coconuts')
    if Player["inventory"]["hasShovel"]:
        print("-A shovel")
    else:
        print("-No shovel")
    if Player["inventory"]["hasKey"]:
        print("-A key")
    else:
        print("-No key")


def mainMenu():
    """
    Main menu, this will probably do more later so this 
    is a placeholder docstring
    """
    while True:
        playerLocation = islandMap[Player["posY"]][Player["posX"]]
        print(Encounters[playerLocation]["Description"])
        print("What do you do?")
        for action in range(len(Encounters[playerLocation]["Actions"])):
            if (not Encounters[playerLocation][f'Completed{action + 1}']):
                print(f'-{Encounters[playerLocation]["Actions"][action]}')
        print("-Inventory\n-Move\n-Map\n-Quit")
        #takes user's choice
        choice = input("-").lower()
        if choice == "move":
            print("Okay!\n")
            move()
        elif choice.capitalize() in Encounters[playerLocation]["Actions"]:
            encounterActions(choice, playerLocation)
        elif choice == "inventory":
            printInv()
        elif choice == "map":
            map.viewMap()
        elif choice == "quit":
            print("\nYou have quit your adventure")
            break
        else:
            print("That's not a valid option!")


def intro():
    '''prints an intro'''
    print("After a massive hurricane, you are seperated from your crew")
    print("You wash up on a pirate infested island")
    print("You realise that there is treasure on the island and " + 
          "decide to steal it")


# Main ------------------------------------------------------------------------
intro()
map.mapExport(islandMap)
mainMenu()