import math 
import sys

def double_square(n):
    if n == 0:
        return 1
    max_x = int(math.sqrt(n))
    s = set([])
    for y in range(1, max_x + 1, 1):
        x = math.sqrt(n - y ** 2)
        if x not in s and x.is_integer():
            s.add(y)
    return len(s)


with open(sys.argv[1]) as f:
    lines = f.readlines()
    for line in lines[1:]:
        print double_square(int(line))
