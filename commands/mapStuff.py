def display_Map(worldMap):

    for i in worldMap:
        str = ""
        for j in i:
            str += j + " "
        print(str)


def gen_Map():
    return [["+" for i in range(10)] for j in range(10)]
