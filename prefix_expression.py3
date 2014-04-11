import sys

'''Calculate preffix expressions
input
* + 2 3 4
output
20
'''


def calculate_prefix(expression):
    number_queue = []
    operations = []
    operators = set(['+','/','*'])
    expression = expression.split(' ')
    i = 0
    symbol = expression[i]
    while symbol in operators and i < len(expression):
        symbol = expression[i]
        if symbol in operators:
            operations.insert(0,symbol)
        i += 1
    number_queue.append(symbol)
    while i < len(expression):
        symbol = expression[i]
        number_queue.append(float(symbol))
        i += 1
    number  = float(number_queue[0])
    del number_queue[0]
    for operator in operations:
        if operator == '+':
            number = number + number_queue[0]
        elif operator == '/':
            number = number / number_queue[0]
        elif operator == '*':
            number = number * number_queue[0]
        else:
            raise ValueError("'%s' not a valid operator"%operator)
        del number_queue[0]
    return int(number)

    

if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')
    for expression in test_cases:
        print(calculate_prefix(expression))
    test_cases.close()
