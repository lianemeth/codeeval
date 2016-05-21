import sys

def decimal_to_binary(n):
    bina = []
    if n == 0:
        return 0
    while n  > 0:
        bina.append(str(n % 2))
        n = n / 2
    bina.reverse()
    return "".join(bina)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as test_data:
        for test in test_data:
            n = int(test)
            print decimal_to_binary(n)
