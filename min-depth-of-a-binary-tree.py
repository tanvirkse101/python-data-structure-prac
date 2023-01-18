class Node:
    def __init__(self, d):
        self.data = d
        self.right = None
        self.left = None


def minDepth(root, level):
    if (root == None):
        return level
    level += 1
    return min(minDepth(root.left, level), minDepth(root.right, level))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Min. Depth: ", minDepth(root, 0))
# print("Root: ", root.data)
# print("Root: ", root.left.data)
# print("Root: ", root.right.data)
# print("Root: ", root.left.left.data)
# print("Root: ", root.left.right.data)
