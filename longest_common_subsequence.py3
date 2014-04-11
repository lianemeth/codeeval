import sys

'''
# slow recursive version:
def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    x_m, y_n, x_m1, y_n1 = x[0], y[0], x[1:], y[1:]
    if x_m == y_n:
        return x_m + lcs(x_m1, y_n1)
    else:
        return max(lcs(x, y_n1), lcs(y, x_m1), key=len)
    '''

def lcs(a, b):
    # initiate a length_table with zeros
    length_table = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j,y in enumerate(b):
            if x == y:
                # case 1
                length_table[i+1][j+1] = length_table[i][j] + 1
            else:
                #case 2 and 3
                length_table[i+1][j+1] = max(length_table[i+1][j],
                        length_table[i][j+1])
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if length_table[x][y] == length_table[x-1][y]:
            x -=1
        elif length_table[x][y] == length_table[x][y-1]:
            y -= 1
        else:
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.replace('\n','')
        a,b = test.split(';')
        print(lcs(a,b))
    test_cases.close()
