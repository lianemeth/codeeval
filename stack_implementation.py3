import sys


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack[-1]
        del self.stack[-1]
        return item

    def is_empty(self):
        return len(self.stack) == 0


def print_alternate(numbers):
    l = []
    stack = Stack()
    for item in numbers:
        stack.push(item)
    while not stack.is_empty():
        l.append(stack.pop())
        if not stack.is_empty():
            stack.pop()
    print(' '.join(l))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            print_alternate(test.replace('\n', '').split(' '))
