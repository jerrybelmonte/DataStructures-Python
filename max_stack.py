# Stack With Maximum
# Author: jerrybelmonte
import sys


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def push(self, value):
        self.__stack.append(value)

        if not self.__max_stack:
            self.__max_stack.append(value)
        elif value >= self.__max_stack[-1]:
            self.__max_stack.append(value)

    def pop(self):
        assert (len(self.__stack))
        value = self.__stack.pop()

        assert (len(self.__max_stack))
        if value == self.__max_stack[-1]:
            self.__max_stack.pop()

    def max(self):
        assert (len(self.__max_stack))
        return self.__max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0
