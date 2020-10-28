import os
import random as r

dungeon_count = 0
switch = {
        1: "D",
        2: "F",
        3: "M",
        4: "T"
    }


def area_switch(case):
    return switch[case]


def determine_Area():
    global dungeon_count, switch

    area = area_switch(r.randint(1, 4))
    if area == "D" and dungeon_count != 4:
        dungeon_count += 1
    elif area == "D" and dungeon_count == 4:
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

    mapv1 = [["+" for _ in range(mapSize)] for _ in range(mapSize)]
    # Creating the map as a list, _ means that no var is needed

    mapv2 = mapv1.copy()
    mapv1[center[0]][center[1]] = "H"

    for index, i in enumerate(mapv1):
        for index2, j in enumerate(i):
            area = determine_Area()
            if area is None:
                area = determine_Area()
                mapv2[index][index2] = area

    mapv2[center[0]][center[1]] = "H"
    return [mapv1, mapv2]


display_Map(gen_Map(2)[0])
