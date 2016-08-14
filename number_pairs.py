import sys

def number_pairs(li, x):
    lo = 0
    hi = len(li) - 1
    pairs = []
    while lo < hi:
        y = li[lo] + li[hi]
        if y > x:
            hi = hi - 1
        elif y < x:
            lo = lo + 1
        else:
            pairs.append(
                    (str(li[lo]), 
                     str(li[hi])))
            lo = lo + 1
    if pairs:
        print ";".join([",".join(p) for p in pairs])
    else:
        print "NULL"


with open(sys.argv[1]) as f:
    for line in f:
        li, x = line.split(";")
        x = int(x)
        li = map(lambda i: int(i), li.split(","))
        number_pairs(li, x)
