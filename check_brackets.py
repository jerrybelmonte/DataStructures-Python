# Check Brackets
# Author: jerrybelmonte
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, ch in enumerate(text):
        if ch in "([{":
            opening_brackets_stack.append(Bracket(ch, i + 1))

        if ch in ")]}":
            if not opening_brackets_stack:
                opening_brackets_stack.append(Bracket(ch, i + 1))
                break
            if are_matching(opening_brackets_stack[-1].char, ch):
                opening_brackets_stack.pop()
            else:
                opening_brackets_stack.append(Bracket(ch, i + 1))
                break

    return opening_brackets_stack


def main():
    text = input()
    mismatch = find_mismatch(text)

    if mismatch:
        print(mismatch.pop().position)
    else:
        print('Success')


if __name__ == "__main__":
    main()
