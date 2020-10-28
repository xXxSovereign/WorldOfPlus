# same as above
import random as r

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for _ in range(2):
    for row in x:
        r.shuffle(row)
    r.shuffle(x)

print(x)