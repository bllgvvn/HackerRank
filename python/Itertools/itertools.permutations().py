from itertools import permutations

S, k = input('Enter the string and the length of permutations separated by a space: ').split()

for i in sorted(list(permutations(S, int(k)))):
    print(''.join(i))