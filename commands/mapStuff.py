import os
import random as r


def display_Map(world_map):  # Function to display the world map, parameter is the current explored map
    os.system("cls")  # Clears previous text in the Terminal
    for i in world_map:
        output = ""  # For loop to access and print individual items in the map list
        for j in i:
            output += j + " "
        print(output)  # Outputs the map in a square


def gen_Map(size):
    # Determine map size off of user input "size"

    if size == 1:
        mapSize = 7
        center = [3, 3]  # Middle of square will be: [3][3]
    elif size == 2:
        mapSize = 11  # Middle: [5][5]
        center = [5, 5]
    elif size == 3:
        mapSize = 15  # Middle: [7][7]
        center = [7, 7]

    mapv1 = [["+" for _ in range(mapSize)] for _ in range(mapSize)]  # Creating the map as a list, _ means that no var                               # is needed

    mapv2 = mapv1.copy()
    dungeon_count = 0

    for index, i in enumerate(mapv1):
        for index2, j in enumerate(i):
            print("[{}][{}] = {}".format(index, index2, j))

    return [mapv1, mapv2]


display_Map(gen_Map(1)[0])
