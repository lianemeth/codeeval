import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            l = test.replace("/n","").split(" ")
            i = int(l.pop())
            if i < len(l) + 1:
                print l[i * -1]
