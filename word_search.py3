import sys

MATRIX = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
        ]


def get_neighbours(matrix, pos):
    neighbours = []
    # up
    if pos[0] - 1 >= 0:
        neighbours.append((pos[0]-1, pos[1]))
    # down
    if pos[0] + 1 < len(matrix):
        neighbours.append((pos[0]+1, pos[1]))
    # left
    if pos[1] -1 >= 0:
        neighbours.append((pos[0], pos[1]-1))
    # right
    if pos[1] + 1 < len(matrix[0]):
        neighbours.append((pos[0], pos[1]+1))
    return neighbours


def has_word(matrix, word):
    # sane check parameters
    if len(word) == 0:
        return False
    # stack used for backtracking
    stack = []
    # positions that were already used
    positions = set([])
    first_letter = word[0]
    # find places where the first letter appears
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char == first_letter:
                # push all posibles start positions
                stack.append(((i,j), 0))
    # walk through the matrix backtracking when
    # necessary
    while len(stack) > 0:
        pos, jj = stack.pop()
        if jj == 0:
            # if we have to start again from scratch
            # we can reset the positions set
            positions = set([])
        positions.add(pos)
        neighbours = get_neighbours(matrix, pos)
        for p in neighbours:
            if p not in positions and matrix[p[0]][p[1]] == word[jj+1]:
                if len(word)-1 == jj+1:
                    return True
                stack.append((p, jj+1))
    return False


if __name__=='__main__':
    with open(sys.argv[1]) as test_data:
        for test in test_data:
            test = test.replace('\n','')
            print(has_word(MATRIX, test))
