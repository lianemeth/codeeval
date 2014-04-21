import sys

def first_non_repeated(s):
    chars = set([])
    for i, char in enumerate(s):
        if char not in s[i+1:] and char not in chars:
            return char
        else:
            chars.add(char)

if __name__ == '__main__':
    with open(sys.argv[1]) as test_data:
        for test in test_data:
            test = test.replace('\n','')
            print(first_non_repeated(test))
