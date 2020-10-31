import os
import random as r


def display_Map(world_map):  # Function to display the world map, parameter is the current explored map
    # os.system("cls")  # Clears previous text in the Terminal
    for i in world_map:
        output = ""  # For loop to access and print individual items in the map list
        for j in i:
            output += j + "  "
        print(output)  # Outputs the map in a square


def to_2d(world_map, n):
    return [world_map[i:i+n] for i in range(0, len(world_map), n)]  # slices the list in n sizes, where n is the length
# of the rows in the 2D map


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
    mapv1[center[0]][center[1]] = "H"  # sets the center of mapv1 to H

    areas = ["F", "M", "T"]  # list of the area's, excluding dungeon and final dungeon

    mapv2 = []  # initializing the list for the fully discovered map

    for row in mapv1:
        for element in mapv1:  # accesing each item to get correct amount of areas
            mapv2.append(r.choice(areas))  # making random areas

    for _ in range(4):
        mapv2[r.randint(0, len(mapv2) - 1)] = u"\U0001D403"  # setting the 4 dungeons at random points on map

    mapv2[r.randint(0, len(mapv2) - 1)] = u"\U0001D405"  # setting final dungeon at random point on map

    midPoint = (len(mapv2) - 1) // 2  # detemine midpoint of 1D array mapv2 using midpoint formula (x1 + x2) / 2 = mid
    # the formula is a little modified by just getting the length of the list

    for _ in range(1000):
        r.shuffle(mapv2)  # shuffles the world map a few times

    while mapv2[midPoint] == u"\U0001D403" or mapv2[midPoint] == u"\U0001D405":  # Making sure middle is not a dungeon
        r.shuffle(mapv2)

    mapv2[midPoint] = u"\U0001D5DB"  # Setting the center of the world map to H

    # constructing the non-flattened list, making the 1D list into 2D
    mapv3 = to_2d(mapv2, mapSize)

    del mapv2, areas, midPoint   # deleting unnecessary lists to free memory

    return mapv3

display_Map(gen_Map(3))
