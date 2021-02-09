# Substring equality
# Author: jerrybelmonte
from random import randint


class Solver:
    def __init__(self, s: str):
        self.s = s.strip()
        self._prime_7 = 1000000007
        self._prime_9 = 1000000009
        self._rand_num = randint(1, self._prime_9)
        self.xl_m1 = self._get_x_powers(self._prime_7)
        self.xl_m2 = self._get_x_powers(self._prime_9)
        self.h1, self.h2 = self._compute_hashes()

    def _get_x_powers(self, prime):
        def compute_x(x1, x2, p):
            return ((x1 % p) * (x2 % p)) % p

        n = len(self.s)  # length of the string
        x = self._rand_num

        x_powers = [0] * (n + 1)  # allocate the array
        x_powers[0], x_powers[1] = 1, x

        for i in range(2, n + 1):
            x_powers[i] = compute_x(x_powers[i - 1], x, prime)

        return x_powers

    def _compute_hashes(self):
        def compute_h(h, m, x1, x2):
            return (x1 * h + x2) % m

        n = len(self.s)  # length of the string
        num = self._rand_num

        p1, p2 = self._prime_7, self._prime_9
        hashes_1, hashes_2 = [0] * (n + 1), [0] * (n + 1)

        for i in range(1, n + 1):
            ch = ord(self.s[i - 1])
            hashes_1[i] = compute_h(hashes_1[i - 1], p1, num, ch)
            hashes_2[i] = compute_h(hashes_2[i - 1], p2, num, ch)

        return hashes_1, hashes_2

    def precompute_hash(self, ndx, size, number):
        def precompute(h1, h2, x, p):
            return (h1 - x * h2) % p

        if number == 1:
            return precompute(self.h1[ndx + size],
                              self.h1[ndx],
                              self.xl_m1[size],
                              self._prime_7)
        else:
            return precompute(self.h2[ndx + size],
                              self.h2[ndx],
                              self.xl_m2[size],
                              self._prime_9)

    def ask(self, fst, snd, size):
        hash1a = self.precompute_hash(fst, size, 1)
        hash1b = self.precompute_hash(snd, size, 1)
        hash2a = self.precompute_hash(fst, size, 2)
        hash2b = self.precompute_hash(snd, size, 2)
        return hash1a == hash1b and hash2a == hash2b


if __name__ == '__main__':
    s = input()
    q = int(input())
    solver = Solver(s)
    for _ in range(q):
        a, b, l = map(int, input().split())
        print("Yes" if solver.ask(a, b, l) else "No")
