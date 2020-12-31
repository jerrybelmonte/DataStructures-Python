# Longest Common Substring
import sys
from random import randint
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


# Find a string w of maximal length that is a substring of both s and t.
# Special case of the edit distance problem (only insertions and deletions).
# Can be solved in time O(|s| * |t|) using dynamic programming.
# Goal is to use hashing to solve it in almost linear time.
def binary_search(s, t, prime1, rand1, prime2, rand2):
	# Use binary search to find the length of the longest common substring.
	answer = Answer(0, 0, 0)
	left, right = 0, min(len(s), len(t))
	while left <= right:
		mid = (left + right)//2
		# Precompute hash values of all substrings of length k of s and t.
		hash_s = precompute_hashes(s, mid, prime1, rand1, prime2, rand2)
		hash_t = precompute_hashes(t, mid, prime1, rand1, prime2, rand2)
		# Store hash values of all substrings of length k of the string s.
		dict_s = {h: i for i, h in enumerate(hash_s)}
		dict_t = {h: i for i, h in enumerate(hash_t)}
		# Go through all substrings of length k of the string t and check
		# whether the hash values of this substring are present.
		matching_hashes = dict_s.keys() & dict_t.keys()
		if matching_hashes and mid > 0:
			h = list(matching_hashes)[0]
			i, j = dict_s[h], dict_t[h]
			answer = Answer(i, j, mid)
			left = mid + 1
		else:
			right = mid - 1
	return answer


def precompute_hashes(string, length, prime1, rand1, prime2, rand2):
	# Use two hash functions to reduce the probability of a collision
	n = len(string)
	m = n - length
	substr = string[m:n]
	hashes = [None]*(m + 1)
	hashes[m] = poly_hash(substr, prime1, rand1, prime2, rand2)
	num1, num2 = 1, 1
	for _ in range(1, length + 1):
		num1, num2 = (num1*rand1) % prime1, (num2*rand2) % prime2
	for i in range(m - 1, -1, -1):
		h1, h2 = hashes[i + 1]
		c1, c2 = ord(string[i]), ord(string[i + length])
		x1, x2 = c1 - num1*c2, c1 - num2*c2
		hashes[i] = (rand1*h1 + x1) % prime1, (rand2*h2 + x2) % prime2
	return hashes


def poly_hash(substr, prime1, rand1, prime2, rand2):
	hash_value1, hash_value2 = 0, 0
	for c in reversed(substr):
		hash_value1 = (hash_value1*rand1 + ord(c)) % prime1
		hash_value2 = (hash_value2*rand2 + ord(c)) % prime2
	return hash_value1, hash_value2


def solve(s, t):
	prime1, prime2 = 1000000007, 1000000009
	rand1, rand2 = randint(31, prime1 - 1), randint(31, prime2 - 1)
	return binary_search(s, t, prime1, rand1, prime2, rand2)


for line in sys.stdin.readlines():
	a, b = line.split()
	ans = solve(a, b)
	print(ans.i, ans.j, ans.len)
