import sys


class BinarySearchTree:

    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


    def add(self, item):
        tree = self
        while tree:
            aux = tree
            if item < tree.item:
                tree = tree.left
            else:
                tree = tree.right
        newtree = BinarySearchTree(item)
        if item < aux.item:
            aux.left = newtree
        else:
            aux.right = newtree
        
    def lowest_common_ancestor(self, item1, item2):
        tree = self
        aux = self
        while tree:
            if item1 < tree.item and item2 < tree.item:
                aux = tree
                tree = tree.left
            elif item1 > tree.item and item2 > tree.item:
                aux  = tree
                tree = tree.right
            else:
                return tree


if __name__ == '__main__':
    tree = BinarySearchTree(30)
    tree.add(8)
    tree.add(52)
    tree.add(3)
    tree.add(20)
    tree.add(10)
    tree.add(29)
    with open(sys.argv[1]) as test_cases:
        for test in test_cases:
            a,b = test.split(' ')
            a,b = int(a),int(b)
            print(tree.lowest_common_ancestor(a,b).item)
