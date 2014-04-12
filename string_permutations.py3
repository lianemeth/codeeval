import sys

def permutations(p , s, l):
    if len(s) == 0:
        l.append(p)
    else:
        for i in range(len(s)):
            permutations(p + s[i], s[:i]+s[i+1:], l)

if __name__ == '__main__':
    with open(sys.argv[1]) as tests:
        for test in tests:
            test = test.replace('\n', '')
            l = []
            permutations('', test, l)
            l.sort()
            print(','.join(l))

