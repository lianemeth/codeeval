import sys

def detecting_cycles(l):
    for i in range(len(l)-1):
        j = i+1
        while j < len(l):
            if l[j] == l[i]:
                if l[i:j] == l[j:j+(j-i)]:
                    return ' '.join(l[i:j])
            j += 1
    return ' '.join(l)


if __name__ == '__main__':
    with open(sys.argv[1]) as test_data:
        for test in test_data:
            test = test.replace('\n','')
            print(detecting_cycles(test.split(' ')))
