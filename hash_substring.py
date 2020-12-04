# Find Pattern In Text
# Rabin-Karp's algorithm implementation.
# Author: jerrybelmonte
from random import randint


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(s, prime, number):
    hash_value = 0
    for i in range(len(s) - 1, -1, -1):
        hash_value = (hash_value*number + ord(s[i])) % prime
    return hash_value


def precomputed_hashes(text, size, prime, number):
    n = len(text)
    substr = text[n - size:n]
    hashes = [None] * (n - size + 1)

    value = 1
    for _ in range(1, size + 1):
        value = (value * number) % prime

    hashes[n - size] = poly_hash(substr, prime, number)
    for i in range(n - size - 1, -1, -1):
        hashes[i] = (
            number*hashes[i + 1] + ord(text[i]) - value*ord(text[i + size])
        ) % prime

    return hashes


def rabin_karp(pattern, text):
    size = len(pattern)
    prime = 1000000007
    rand_num = randint(1, prime - 1)

    poly_hash_val = poly_hash(pattern, prime, rand_num)
    computed_hash = precomputed_hashes(text, size, prime, rand_num)

    result = []
    for i in range(len(text) - size + 1):
        if poly_hash_val != computed_hash[i]:
            continue
        if text[i:i + size] == pattern:
            result.append(i)

    return result


if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))
