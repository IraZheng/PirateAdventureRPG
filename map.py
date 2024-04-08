###############################################################################
# Map Module
###############################################################################
#for map table
from tabulate import tabulate

#map export file
mapFile = 'map.txt'

def mapExport(map):
    '''Exports the map to an external file'''
    try:
        with open(mapFile, "w") as file:
            file.write(tabulate(map, tablefmt = "fancy_grid"))
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