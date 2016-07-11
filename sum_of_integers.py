import sys

def sum_of_integers(li):
    if not li:
        return 0
    max_so_far = max_ending_here = li[0]
    for item in li[1:]:
        max_ending_here = max(max_ending_here + item, item)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as test_data:
        for test in test_data:
            l = [int(i) for i in test.split(",")]
            print sum_of_integers(l)
