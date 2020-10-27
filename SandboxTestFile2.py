# same as above

import json
a = [1, 2, 3]
with open('test.txt', 'w') as f:
    f.write(json.dumps(a))
    f.write(json.dumps([1, 4, 6, 6]))

# Now read the file back into a Python list object
with open('test.txt', 'r') as f:
    a = json.loads(f.read())

print(a)
