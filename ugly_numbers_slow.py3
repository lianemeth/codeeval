import sys

def remove_ending_plus(exp):
    j = len(exp) - 1
    while exp[j] == '+' or exp[j] == '-':
        j -= 1
    return exp[:j+1]


def remove_trailing_zero(exp):
    '''eval('010') will be interpreted as a octal 10 which is dec 08'''
    if len(exp) > 0 and exp[0] == '0':
        j = 0
        while j < len(exp) and exp[j] == '0':
            j += 1
        if j < len(exp):
            exp = exp[j:]
    return exp


def get_expression(p, s, l):
    if len(s) == 0:
        p = remove_ending_plus(p)
        l.add(p)
    else:
        for i in range(len(s)):
            x = remove_trailing_zero(s[i:])
            p = remove_trailing_zero(p)
            get_expression(x+'+'+p, s[:i], l)
            get_expression(x+'-'+p, s[:i], l)


def is_ugly(number):
    return number % 2 == 0 or number % 3 == 0 or \
            number % 5 == 0 or number % 7 == 0


def count_ugly(s):
    expressions = set([])
    get_expression('', s, expressions)
    ugly_numbers = 0
    for expression in expressions:
        if is_ugly(eval(expression)):
            ugly_numbers += 1
    return ugly_numbers


if __name__ == '__main__':
    with open(sys.argv[1]) as tests:
        for test in tests:
            test = test.replace('\n', '')
            print(count_ugly(test))
