# Is it a binary search tree? Hard version.
# Author: jerrybelmonte
import sys
import threading

sys.setrecursionlimit(10 ** 8)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def is_binary_search_tree(tree):
    if not tree:  # empty tree is bst
        return True

    # if the tree is not empty
    return check_bst_left(tree, 0, -sys.maxsize, sys.maxsize)


def check_bst_left(tree, ndx, min_val, max_val):
    if ndx == -1:  # node does not have child nodes
        return True

    value = tree[ndx][0]  # key value of the node
    if value < min_val or value >= max_val:
        return False  # violates rules for bst

    left_is_bst = check_bst_left(tree, tree[ndx][1], min_val, value)
    right_is_bst = check_bst_right(tree, tree[ndx][2], value, max_val)
    return left_is_bst and right_is_bst


def check_bst_right(tree, ndx, min_val, max_val):
    if ndx == -1:  # node does not have child nodes
        return True

    value = tree[ndx][0]  # key value of the node
    if value < min_val or value > max_val:
        return False  # violates rules for bst

    left_is_bst = check_bst_left(tree, tree[ndx][1], min_val, value)
    right_is_bst = check_bst_right(tree, tree[ndx][2], value, max_val)
    return left_is_bst and right_is_bst


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
