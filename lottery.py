import random

# database[0]がレア度:通常、database[1]がレア度:シークレット
#database = [["001"],
#            ["101", "101", "101"]]
database = [["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012", "013", "014", "015", "016"],
            ["101", "102", "103"]]

def lottery():
    rnd = random.randint(0, 99)
    if 0 <= rnd < 85:
        result = random.choice(database[0])
    if 85 <= rnd < 100:
        result = random.choice(database[1])
    return result