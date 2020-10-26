def display_Map(worldMap):
    worldMap = [["+" for i in range(10)] for j in range(10)]

    for i in worldMap:
        str = ""
        for j in i:
            str += j + " "
        print(str)
