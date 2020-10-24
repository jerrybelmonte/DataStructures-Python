# Maximum In Sliding Window
# Author: jerrybelmonte
# Stores relevant items in a dequeue. Uses a double-ended queue (dequeue)
# to store elements of the current window. At the same time, stores only
# relevant elements: before adding a new element it drops all smaller elements.
from collections import deque


def max_sliding_window(sequence, k):
    """
    Gets the maximum elements in the sliding window.

    :param sequence: the sequence of elements
    :param k: the size of the sliding window
    :return: the list with the maximums
    >>> max_sliding_window([2, 7, 3, 1, 5, 2, 6, 2], 4)
    [7, 7, 5, 6, 6]
    """
    maximums = []
    dq = deque()

    for i in range(k):  # the initial k elements in the window
        while dq and sequence[dq[-1]] <= sequence[i]:
            dq.pop()  # pop smaller elements than the current from the end
        dq.append(i)  # add the current element to the deque

    for i in range(k, len(sequence)):
        maximums.append(sequence[dq[0]])  # element at 0th index is the maximum

        while dq and dq[0] <= i - k:  # i - k is the current window
            dq.popleft()  # pop maximums not in the window

        while dq and sequence[dq[-1]] <= sequence[i]:
            dq.pop()  # pop smaller elements than the current element
        dq.append(i)  # add the current element

    maximums.append(sequence[dq.popleft()])  # add the last maximum
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window(input_sequence, window_size))
