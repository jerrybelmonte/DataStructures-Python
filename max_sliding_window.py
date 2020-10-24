# python3
# Store relevant items in a dequeue. Use a double-ended queue (dequeue)
# to store elements of the current window. At the same time, store only
# relevant elements: before adding a new element drop all smaller elements.
from collections import deque


def max_sliding_window(sequence, k):
    """
    :param sequence:
    :param k:
    :return:
    >>> max_sliding_window([2, 7, 3, 1, 5, 2, 6, 2], 4)
    [7, 7, 5, 6, 6]
    """
    maximums = []
    dq = deque()
    for i in range(k):
        while dq and sequence[list(dq)[-1]] <= sequence[i]:
            dq.pop()

        dq.append(i)

    for i in range(k, len(sequence)):
        max_ndx = dq.popleft()
        maximums.append(sequence[max_ndx])
        dq.appendleft(max_ndx)

        while dq and list(dq)[0] <= i - k:
            dq.popleft()

        while dq and sequence[list(dq)[-1]] <= sequence[i]:
            dq.pop()

        dq.append(i)

    maximums.append(sequence[dq.popleft()])
    return maximums


def max_sliding_window_naive(sequence, m):
    """
    >>> max_sliding_window_naive([2, 7, 3, 1, 5, 2, 6, 2], 4)
    [7, 7, 5, 6, 6]
    """
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

