import json


def save(save_data, save_data2):

    with open('original_map_save.txt', 'w') as f:
        f.write(json.dumps(save_data))

    with open('discovered_map_save.txt', 'w') as f:
        f.write(json.dumps(save_data2))


save([1,3,4,5,6], [["1",'1','45'], ['3','+','+']])
