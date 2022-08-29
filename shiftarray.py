### Write your function here ###
output = []

def shift(array, steps):
    for x in range(steps):
        output = array.pop()
        array.insert(0, output)
    print(array)

shift(['andi', 'budi', 'charlie', 'doni'],2)