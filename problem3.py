import sys
import numbers


# create individual nodes that live in tree
class Node(object):
    def __init__(self, value=None, frequency=None):
        self.value = value
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, value):
        self.left_child = value

    def set_right_child(self, value):
        self.right_child = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left_child != None

    def has_right_child(self):
        return self.right_child != None


# create tree structure to hold root node
class Tree:
    def __init__(self, node=None):
        self.root = Node(node)

    def get_root(self):
        return self.root

    def set_root(self, value):
        self.root = value


def create_tree(data):

    if type(data) is not str:
        return -1

    if len(data) < 1:
        return -1

    character_dict = {}

    for character in data:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    huffman_tree = Tree()
    nodes_to_add = []

    while len(character_dict) > 0:
        nodes_to_add.append(Node(min(character_dict), character_dict[min(character_dict)]))
        character_dict.pop(min(character_dict), None)

    while(len(nodes_to_add) > 1):
        combo_node = Node(nodes_to_add[0].frequency + nodes_to_add[1].frequency, nodes_to_add[0].frequency + nodes_to_add[1].frequency)
        combo_node.set_left_child(nodes_to_add[0])
        combo_node.set_right_child(nodes_to_add[1])
        nodes_to_add.pop(1)
        nodes_to_add.pop(0)
        nodes_to_add.append(combo_node)
    huffman_tree.set_root(nodes_to_add[0])

    return huffman_tree


# stack keeps track of tree nodes as they are traversed to create huffman coding values
class Stack:
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

#Keep track of state when visiting all nodes in tree
class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True


def huffman_encoding(tree):

    if tree == -1:
        return -1

    encoding_dictionary = {}
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    encoding_dictionary[node.value] = '0'

    while node:
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()

            encoding_dictionary[node.get_left_child().value] = str(encoding_dictionary[node.value]) + '0'

            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()

            encoding_dictionary[node.get_right_child().value] = str(encoding_dictionary[node.value]) + '1'

            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    # List of keys to be deleted from dictionary
    keys_to_delete = list()

    # Iterate over the dict and put to be deleted keys in the list
    for key in encoding_dictionary:
        if isinstance(key, (int, float)):
            keys_to_delete.append(key)

    # Iterate over the list and delete corresponding key from dictionary
    for key in keys_to_delete:
        if key in encoding_dictionary:
            del encoding_dictionary[key]

    return encoding_dictionary


def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node is not None:
            # visit
            visit_order.append(node.get_value())
            # traverse left
            traverse(node.get_left_child())
            # traverse right
            traverse(node.get_right_child())

    traverse(root)
    return visit_order


def encode_string(string):
    character_dictionary = huffman_encoding(create_tree(string))
    output_data = []
    for character in string:
        output_data.append(character_dictionary[character])

    return output_data


def huffman_decoding(output_data, character_dict):

    #check for correct inputs
    if type(character_dict) is not int and len(character_dict) < 1:
        return -1

    if type(character_dict) is int:
        return -1

    output_string = ''

    key_list = list(character_dict.keys())
    value_list = list(character_dict.values())

    for number in output_data:
        output_string += key_list[value_list.index(number)]

    return output_string


print(huffman_encoding(create_tree('ssrf')))
print(encode_string('ssrf'))
print(huffman_encoding(create_tree('kibbles')))
print(huffman_encoding(create_tree('jonathanlivingstonseagull')))

#edge case - works with single character string
huffman_tree = huffman_encoding(create_tree('AAAAAAA'))
print(huffman_tree)
print(huffman_decoding(['0', '0', '0', '0', '0', '0', '0'], huffman_tree))

#edge case - works with single empty string
huffman_tree2 = huffman_encoding(create_tree(''))
print(huffman_tree2)
print(huffman_decoding(['0', '0', '0', '0', '0', '0', '0'], huffman_tree2)) #returns rsr

#edge case - returns -1 if type is not string
print(huffman_encoding(create_tree(9324893)))

huffman_tree1 = huffman_encoding(create_tree('ssrf'))

print(huffman_decoding(['011', '00', '011', '010'], huffman_tree1)) #returns rsrf
