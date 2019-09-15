
class Node:
    def __init__(self, value, left_child=None, right_child=None, label=""):
        self.value = value
        self.operator = True if type(value) == string else False

        self.left_child = left_child
        self.right_child = right_child

    def add_child(self, child_to_add, position):
        if position in ["left", "l", "0", 0]:
            self.left_child = child_to_add

        elif position in ["right", "r", "1", 12]:
            self.right_child = child_to_add


root = Node(input("Enter a root node value"))

while 1:
