class Node(object):
    def __init__(self):
        self.children = []
        self.meta_data = []

    def add_child(self, node):
        self.children.append(node)

    def add_meta_data(self, data):
        self.meta_data.append(data)


def parse_input():
    integers = []

    with open('input.txt') as f:
        for line in f:
            for word in line.split():
                integers.append(int(word))

    return integers


def generate_tree(integers, index):
    parent = Node()

    children = integers[index]
    meta_data = integers[index + 1]
    index += 2

    for _ in range(children):
        child, index = generate_tree(integers, index)
        parent.add_child(child)

    for _ in range(meta_data):
        parent.add_meta_data(integers[index])
        index += 1

    return parent, index


def calculate_tree_sum(node):
    total = sum(node.meta_data)

    for child in node.children:
        total += calculate_tree_sum(child)

    return total


def calculate_tree_value(node):
    value = 0

    if len(node.children) == 0:
        return sum(node.meta_data)

    for index in node.meta_data:
        if index - 1 < len(node.children):
            value += calculate_tree_value(node.children[index - 1])

    return value


if __name__ == '__main__':
    integers = parse_input()
    tree, _ = generate_tree(integers, 0)
    tree_sum = calculate_tree_sum(tree)
    tree_value = calculate_tree_value(tree)

    print(tree_sum)
    print(tree_value)
