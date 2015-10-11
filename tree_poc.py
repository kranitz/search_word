import json


class Node:
    def __init__(self, value):
        self.data = value
        self.childrens = []
        self.its_word = False

    def add_child(self, child):
        self.childrens.append(child)

    def get_childrens(self):
        return self.childrens

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        for child in self.childrens:
            ret += child.__repr__(level+1)
        return ret
        # if tree is None:
        #     return ""
        # self.indented_traverse(tree.right, level+2)
        # print(' ' * level + tree.value)
        # self.indented_traverse(tree.left, level+1)

    def traverse(self, tree):
        if tree == None:
            return 0
        for node in tree.children:
            print(node.value)
            self.traverse(node)

            # def insert(self, data):
            #     """
            #     Insert new node with data
            #
            #     @param data node data object to insert
            #     """
            #     if self.data:
            #
            #                 self.left.insert(data)
            #         elif data > self.data:
            #             if self.right is None:
            #                 self.right = Node(data)
            #             else:
            #                 self.right.insert(data)
            #     else:
            #         self.data = data



words = ["al", "alma", "almafa"]

tree = {}

def make_tree(tree, word):
    if not word:
        tree['its_word'] = True
        return
    if word[0] not in tree:
        tree[word[0]] = {'its_word': False}
    make_tree(tree[word[0]], word[1:])
    # make_tree(new_node, word[1:])

    # if letter:
    #     new_node = Node(letter)
    #     tree.add_child(new_node)
    #     print(letter, "----")
    #     make_tree(new_node, word)


def print_indented_tree(tree, level=0):
    for key, value in tree.items():
        print(' ' * level + str(key))
        if isinstance(value, dict):
            print_indented_tree(value, level+1)
        else:
            print(' ' * (level+1) + str(value))

def main():
    # tree = Node("a", Node("l", Node("a", Node("a"))), Node("m", Node("f")))
    # tree = Node("grandmother", [
    #     Node("daughter", [
    #         Node("granddaughter"),
    #         Node("grandson")]),
    #     Node("son", [
    #         Node("granddaughter"),
    #         Node("grandson")])
    # ])
    root = Node("root")
    tmp = Node("")
    for w in words:
        print("------",w)
        make_tree(tree, w)
    # for letter in words[2]:
    #     newnode = Node(letter)
    #     tmp.add_child(newnode)
    # root.add_child(tmp)

    print(json.dumps(tree, indent=True))
    # print_indented_tree(tree)
    # make_tree(root, words[2])

    # for letter in words[2]:
    #     root.add_child(Node(letter))


    #
    #
    # make_tree(root, words[2])
    # root.traverse(root)

    # tree.add_child("asd")
    # tree.traverse(tree)

    # tree.indented_traverse(tree)

if __name__ == "__main__":
    main()
