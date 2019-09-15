
class Node:
    def __init__(self, value, operator=False, left=None, right=None):
        self.value = value
        self.operator = operator
        self.left = left
        self.right = right

rootNode = Node(5)

print(rootNode)
