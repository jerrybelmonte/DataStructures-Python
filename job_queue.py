# Parallel Processing
from collections import namedtuple
from heapq import heapify, heappop, heappush

AssignedJob = namedtuple('AssignedJob', ['worker', 'started_at'])


def assign_jobs(n_workers: int, jobs: list):
    """
    Uses n independent threads to process a given list of jobs.

    :param n_workers: number of threads
    :param jobs: list of job query times
    :return: list of ith thread and time started

    >>> assign_jobs(2, [1, 2, 3, 4, 5])
    [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]
    """
    pq = [(0, w) for w in range(n_workers)]
    heapify(pq)
    result = []

    for job in jobs:
        worker = heappop(pq)
        result.append(AssignedJob(worker[1], worker[0]))
        heappush(pq, (worker[0] + job, worker[1]))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
