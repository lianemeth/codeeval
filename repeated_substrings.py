import sys

def is_repeated(string, substring):
    is_repeated = len(string.replace(substring,"")) < len(string) - len(substring)
    return is_repeated and not substring.isspace()

def longest_repeated(string):
    max_so_far =  0
    index_so_far = 0
    max_string = "NONE"
    if string.isspace():
        return max_string
    for index in range(len(string)):
        sub_string = string[index_so_far:index]
        if is_repeated(string, sub_string):
            if len(sub_string) > max_so_far:
                max_so_far = len(sub_string)
                max_string = sub_string
        else:
            index_so_far = index
    return max_string

if __name__ == '__main__':
    with open(sys.argv[1]) as test_data:
        for line in test_data:
            print longest_repeated(line.replace("\n",""))
