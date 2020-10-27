import json


def load():
    retval = []
    with open('original_map_save.txt', 'r') as f:
        retval.append(json.loads(f.read()))

    with open('discovered_map_save.txt', 'r') as f:
        retval.append((json.loads(f.read())))

    return retval


print(load()[0])
print(load()[1])
