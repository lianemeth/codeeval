import sys
print(sum([int(i) for i in open(sys.argv[1]).readlines()]))
