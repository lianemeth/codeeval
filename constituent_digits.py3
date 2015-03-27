import sys


def constituent_digits_sum(str_number):
    return sum([int(i) for i in list(str_number)])


if __name__ == '__main__':
    with open(sys.argv[1]) as test_data:
        for test in test_data:
            test = test.replace('\n', '')
            print(constituent_digits_sum(test))
