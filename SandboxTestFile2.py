# same as above

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for index, i in enumerate(x):
    for index2, j in enumerate(i):
        print("[{}][{}] = {}".format(index, index2, j))
