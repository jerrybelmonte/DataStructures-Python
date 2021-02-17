# Binary Tree Traversals
# author: jerrybelmonte
import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]

    def read(self):
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order(self):
        result = []
        self._in_order_recursive(result, 0)
        return result

    def _in_order_recursive(self, arr, ndx):
        if ndx != -1:
            # visit the left subtree first
            if self.left[ndx] != -1:
                self._in_order_recursive(arr, self.left[ndx])

            # add the key value of the current node
            arr.append(self.key[ndx])

            # visit the right subtree last
            if self.right[ndx] != -1:
                self._in_order_recursive(arr, self.right[ndx])

    def pre_order(self):
        result = []
        self._pre_order_recursive(result, 0)
        return result

    def _pre_order_recursive(self, arr, ndx):
        if ndx != -1:
            # add the key value of the current node first
            arr.append(self.key[ndx])

            # visit the left subtree second
            if self.left[ndx] != -1:
                self._pre_order_recursive(arr, self.left[ndx])

            # visit the right subtree last
            if self.right[ndx] != -1:
                self._pre_order_recursive(arr, self.right[ndx])

    def post_order(self):
        result = []
        self._post_order_recursive(result, 0)
        return result

    def _post_order_recursive(self, arr, ndx):
        if ndx != -1:
            # visit the left subtree first
            if self.left[ndx] != -1:
                self._post_order_recursive(arr, self.left[ndx])

            # visit the right subtree next
            if self.right[ndx] != -1:
                self._post_order_recursive(arr, self.right[ndx])

            # add the key value of the current node last
            arr.append(self.key[ndx])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


threading.Thread(target=main).start()
