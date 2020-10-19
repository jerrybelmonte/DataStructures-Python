# Convert Array Into Heap
# Author: jerrybelmonte
# Input: First line contains an integer n.
# Second line contains n integers separated by a space.
# Output: First line contains the total number of swaps.
# The following lines contain the swap operations on the array. 


def build_heap(data):
    """Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    n = len(data)

    parent = lambda i: (i - 1) // 2
    left_child = lambda i: 2 * i + 1
    right_child = lambda i: 2 * i + 2

    min_index = lambda i, j: j if j < n and data[j] < data[i] else i

    def heapify(i):
        ndx = i
        left = left_child(i)
        right = right_child(i)

        ndx = min_index(ndx, left)
        ndx = min_index(ndx, right)

        if i != ndx:
            swaps.append((i,ndx))
            data[i], data[ndx] = data[ndx], data[i]
            heapify(ndx)

    for i in range((n//2), -1, -1):
        heapify(i)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
