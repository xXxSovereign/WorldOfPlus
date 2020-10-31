import os
import random as r
import numpy as np

# global variables used in functions, they must be up here to be accessable throught this program
dungeon_count = 0
switch = {
    1: u"\U0001D403",  # UTF-8 Encoding for 𝐃
    2: "F",
    3: "M",
    4: "T"
}


def Shuffle(map):
    return ["placeholder", "value"]


def area_Switch(case):
    return switch[case]  # this function is used this way to get around a problem with scope and other problems


def determine_Area():
    global dungeon_count, switch

    area = area_Switch(r.randint(1, 4))
    if area == u"\U0001D403" and dungeon_count != 4:
        dungeon_count += 1
    elif area == u"\U0001D403" and dungeon_count == 4:
        area = None
        switch[1] = "F"
    return area


def display_Map(world_map):  # Function to display the world map, parameter is the current explored map
    # os.system("cls")  # Clears previous text in the Terminal
    for i in world_map:
        output = ""  # For loop to access and print individual items in the map list
        for j in i:
            output += j + " "
        print(output)  # Outputs the map in a square


def gen_Map(size):
    # Determine map size off of user input "size" and center of the map

    if size == 0:
        mapSize = 3
        center = [1, 1]
    elif size == 1:
        mapSize = 7
        center = [3, 3]  # Middle of square will be: [3][3]
    elif size == 2:
        mapSize = 11  # Middle: [5][5]
        center = [5, 5]
    elif size == 3:
        mapSize = 15  # Middle: [7][7]
        center = [7, 7]

    mapv1 = [["+" for _ in range(mapSize)] for _ in range(mapSize)]
    # Creating the map as a list, _ means that no var is needed

    mapv2 = mapv1.copy()
    mapv1[center[0]][center[1]] = "H"  # sets the center of mapv1 to H

    # This loops through all the +'s in mapv1, and copies the position using enumerate, to the map the Area's onto mapv2
    for index, i in enumerate(mapv1):  # Access each list in mapv1
        for index2, j in enumerate(i):  # access each item in each list in mapv1
            area = determine_Area()  # generate a radnom area
            if area is None:
                area = determine_Area()  # This whole block is used in conjunction with determine_Area() to block >4 D's
            mapv2[index][index2] = area  # sets the index in mapv2 to the area

    mapv2[center[0]][center[1]] = "H"

    mapv1 = [["+" for _ in range(mapSize)] for _ in range(mapSize)]
    mapv1[center[0]][center[1]] = "H"

    # Shuffling mapv2 to fix Dungeons only appearing near the top
    mapv3 = Shuffle(mapv2)

    # Making the entire map's center H

    return [mapv1, mapv2]


display_Map(gen_Map(3)[1])
