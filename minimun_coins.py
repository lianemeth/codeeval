import sys

def mininum_coins(value):
    coins_5 = value / 5
    value = value - (coins_5 * 5)
    coins_3 = value / 3
    value = value - (coins_3 * 3)
    return coins_5 + coins_3 + value

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        print mininum_coins(int(line))

