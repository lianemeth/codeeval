import sys

def get_expression(s):
    n_chars = len(s)
    if n_chars == 0:
        return s
    exps = [ s[0] ]
    for char in s[1:]:
        n_exps = len(exps)
        j = 0
        while j < n_exps:
            exp = exps[j]
            exps[j] = exp + '+' + char#+
            exps.append(exp + '-' + char)#-
            exps.append(exp + char)#''
            j += 1
    return exps

def calculate(exp):
    if len(exp) == 0:
        return 0
    # get first number
    j = 0
    number = ''
    while j < len(exp) and exp[j] != '+' and exp[j] != '-':
        number += exp[j]
        j += 1
    s = int(number)
    if j >= len(exp):
        # the expression was a literal number
        return s
    number = ''
    # now follow the rest of the expression
    signal = exp[j]
    j += 1
    while j < len(exp):
        if exp[j] in ('-', '+'):
            if signal == '-':
                s -= int(number)
            else:
                s += int(number)
            signal = exp[j]
            number = ''
        else:
            number += exp[j]
        j += 1
    if signal == '-':
        s -= int(number)
    else:
        s += int(number)
    return s

def is_ugly(number):
    return number % 2 == 0 or number % 3 == 0 or \
            number % 5 == 0 or number % 7 == 0

def count_ugly(s):
    expressions = get_expression(s)
    ugly_numbers = 0
    for expression in expressions:
        if is_ugly(calculate(expression)):
            ugly_numbers += 1
    return ugly_numbers


if __name__ == '__main__':
    with open(sys.argv[1]) as tests:
        for test in tests:
            test = test.replace('\n', '')
            print(count_ugly(test))
