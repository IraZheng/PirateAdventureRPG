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
movement = "-Move north \n-Move south \n-Move east \n-Move west \n"
#encounters on the island
Encounters = {"Camp": {"Description": "Camp description", 
                       "Actions": "Camp actions"}, 
              "Key": {"Description": "Key description", 
                      "Actions": "Key actions"}, 
              "Patrol": {"Description": "Patrol description", 
                         "Actions": "Patrol actions"}, 
              "Shovel": {"Description": "Shovel description", 
                         "Actions": "Shovel actions"}, 
              "Start": {"Description": "Start description", 
                        "Actions": "Start actions"}, 
              "Trap": {"Description": "Trap description", 
                       "Actions": "Trap Actions"}, 
              "Treasure": {"Description": "Treasure description", 
                           "Actions": "Treasure actions"},
              "Tree": {"Description": "Tree description", 
                       "Actions": "Tree actions"}
             }


# Functions -------------------------------------------------------------------
def mapMove(choice):
    global Player
    #for map movement
    if choice == "north":
        if Player["posY"] > 0:
            Player["posY"] -= 1
        else:
            print("Thats the end of the island, you can't go there!")
    elif choice == "south":
        if Player["posY"] < (len(island_map) - 1):
            Player["posY"] += 1
        else:
            print("Thats the end of the island, you can't go there!")
    elif choice == "east":
        if Player["posX"] < (len(island_map[Player["posY"]]) - 1):
            Player["posX"] += 1
        else:
            print("Thats the end of the island, you can't go there!")
    elif choice == "west":
        if Player["posX"] > 0:
            Player["posX"] -= 1
        else:
            print("Thats the end of the island, you can't go there!")


def mainMenu():
    while True:
        player_location = island_map[Player["posY"]][Player["posX"]]
        actions = movement + Encounters[player_location]["Actions"]
        print(Encounters[player_location]["Description"])
        print(actions)
        choice = input("What do you do? \n-")
        if choice in ["north", "south", "east", "west"]:
            mapMove(choice)


# Main ------------------------------------------------------------------------
mainMenu()