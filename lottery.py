import random

# database[0]がレア度:通常、database[1]がレア度:シークレット
database = [[1, 2, 3, 4, 5, 6],
            [11, 12, 13, 14, 15]]

def lottery():
    rnd = random.randint(1, 100)
    if 0 <= rnd < 90:
        result = random.choice(database[0])
    if 90 <= rnd < 100:
        result = random.choice(database[1])
    return result

print(lottery())