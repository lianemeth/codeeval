import sys

def remove_characters(line):
    sentence, letters = line.split(', ')
    for letter in letters:
        sentence = sentence.replace(letter, '')
    return sentence

if __name__ == '__main__':
    with open(sys.argv[1]) as test_data:
        for test in test_data:
            test = test.replace('\n', '')
            print(remove_characters(test))
