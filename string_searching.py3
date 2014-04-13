import sys


def get_char(c):
    return ord(c) - 47


def bmh(b, a):
    '''Boyer-Moore-Horspool algorithm'''
    founds = []
    if not a or len(a) > len(b):
        return []
    bad_char = [len(a) for i in range(76)]
    for k in range(len(a) -1):
        bad_char[get_char(a[k])] = len(a) - k - 1
    k = len(a) - 1
    while k < len(b):
        j = len(a) - 1
        i = k
        while j >= 0 and (b[i] == a[j]):
            j -= 1
            i -= 1
        if j == -1 :
            founds.append(i + 1)
        k += bad_char[get_char(b[k])]
    return founds


def search(b, a):
    if a.replace('*','') == '':
        return True
    a = a.replace('\*','/') # change the escaped * for a special char
    b = b.replace('*','/')
    sub_patterns = [ x for x in a.split('*') if len(x) > 0]
    if len(sub_patterns) == 1:
        pos = bmh(b, sub_patterns[0])
        return len(pos) > 0
    else:
        sub_patterns.reverse()
        pos = bmh(b, sub_patterns[0])
        for patt in sub_patterns[1:]:
            new_pos = []
            for p in pos:
                new_pos.extend(bmh(b[:p], patt))
            if not new_pos:
                return False
            pos = new_pos
        return True


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for test in f:
            text, pattern = test.replace('\n','').split(',')
            result = search(text, pattern)
            print(str(result).lower())
