# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is a subset of set B, print True.
# If set A is not a subset of set B, print False.

t = int(input('How many test cases? '))

for test in range(t):
    a_total = int(input('Enter the number of elements in set A: '))
    a_set = set(map(int, input('Enter the elements of set A: ').split()))

    b_total = int(input('Enter the number of elements in set B: '))
    b_set = set(map(int, input('Enter the elements of set B: ').split()))

    if a_set.issubset(b_set):
        print("True")
    else:
        print("False")