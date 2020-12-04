# Hash table using chaining scheme implementation.
# Author: jerrybelmonte


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, row_count: int):
        self.row_count = row_count
        self.rows = dict()
        for num in range(row_count):
            self.rows[num] = list()

    def _hash_func(self, s: str):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.row_count

    def add(self, s: str):
        """Inserts a string into the hash table if and only if no such string
        already exists in the hash table."""
        index = self._hash_func(s)
        if s not in self.rows[index]:
            self.rows[index].append(s)

    def remove(self, s: str):
        """Removes a string from the hash table if and only if the string
        already exists within the hash table."""
        index = self._hash_func(s)
        if s in self.rows[index]:
            ndx = self.rows[index].index(s)
            del self.rows[index][ndx]

    def find(self, s: str):
        """Returns True if the string exists within the hash table, otherwise
        returns false."""
        index = self._hash_func(s)
        return s in self.rows[index]

    def check(self, index: int):
        """Checks and returns the list at the given row index if the list is
        not empty, otherwise returns an empty string."""
        if self.rows[index]:
            return self.rows[index][::-1]
        return ""


def read_query():
    return Query(input().split())


def write_search_result(was_found):
    print('yes' if was_found else 'no')


def write_chain(chain):
    print(' '.join(chain))


def process_query(q_processor, query):
    if query.type == 'add':
        q_processor.add(query.s)
    elif query.type == 'del':
        q_processor.remove(query.s)
    elif query.type == 'find':
        write_search_result(q_processor.find(query.s))
    elif query.type == "check":
        chain = q_processor.check(query.ind)
        if chain:
            write_chain(chain)
        else:
            print(chain)


def process_queries(q_processor):
    n = int(input())
    for i in range(n):
        process_query(q_processor, read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    process_queries(proc)
