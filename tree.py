
nodes = {"/":"+", "0":"x", "00":"3", "01":"4", "1":"5"}

def draw_tree(dict_of_values):
    output = nodes["/"]


    pass








class Node:
    def __init__(self, value, left_child=None, right_child=None, label=""):
        self.value = value
        self.operator = True if type(value) == "string" else False

        self.left_child = left_child
        self.right_child = right_child

    def add_child(self, child_to_add, position):
        if position in ["left", "l", "0", 0]:
            self.left_child = child_to_add

        elif position in ["right", "r", "1", 1]:
            self.right_child = child_to_add


root = Node(input("Enter a root node value:\n>>> "))

nodes = {"/": root}

while 1:
    what_to_do = input("\nAdd a child node?\nl - left\nr - right\n[nothing] - leave this as a leaf node\n>>> ")
