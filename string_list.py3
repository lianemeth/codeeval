import sys

def possible_strings(m, letters):
    symbols = set(letters)
    l = []

    def string_list(pre, n, set_symbols):
        if n == 0:
            l.append(pre)
        else:
            for s in set_symbols:
                string_list(pre + s, n - 1, set_symbols)
    
    string_list('', m, symbols)
    l.sort()
    return ','.join([str(i) for i in l])

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for data in f:
            data = data.replace('\n', '')
            n, letters = data.split(',')
            print(possible_strings(int(n), letters))
