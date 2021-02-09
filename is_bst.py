# Binary Search Tree Check
# Author: jerrybelmonte
import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


def is_binary_search_tree(tree):
    if tree:  # if the tree is not empty
        arr = []  # array to hold copy of bst
        copy_tree(tree, 0, arr)

        for i in range(1, len(tree)):
            if arr[i] <= arr[i - 1]:
                return False

    return True  # empty tree is considered correct


def copy_tree(tree, ndx, arr):
    if ndx != -1:
        if tree[ndx][1] != -1:  # left child
            copy_tree(tree, tree[ndx][1], arr)

        arr.append(tree[ndx][0])  # node value

        if tree[ndx][2] != -1:  # right child
            copy_tree(tree, tree[ndx][2], arr)


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
