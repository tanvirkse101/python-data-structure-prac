class Node:
    def __init__(self, key, l=None, r=None):
        self.left = l
        self.right = r
        self.val = key


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printInorder(root)
