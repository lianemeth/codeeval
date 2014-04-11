import sys

def unique(number_list):
    if len(number_list) == 0:
        return number_list
    new_list = []
    aux = number_list[0]
    new_list.append(aux)
    for i in number_list[1:]:
        if i != aux:
            new_list.append(i)
            aux = i
    return ','.join([str(k) for k in new_list])

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        number_list = [int(j) for j in test.split(',')]
        print(unique(number_list))
    test_cases.close()
