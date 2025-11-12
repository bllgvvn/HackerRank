# You are given a two lists A and B.
# Your task is to compute their cartesian product A x B.

from itertools import product

A = list(map(int, input('Enter elements of list A: ').split()))
B = list(map(int, input('Enter elements of list B: ').split()))

for i in list(product(A, B)):
    print(i, end=' ')