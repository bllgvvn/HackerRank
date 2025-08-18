# Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

M = int(input('Enter the number of elements in set M: '))
m_list = input('Enter the elements of set M: ')
m_set = set(map(int, m_list.split()))

N = int(input('Enter the number of elements in set N: '))
n_list = input('Enter the elements of set N: ')
n_set = set(map(int, n_list.split()))

first_half = m_set.difference(n_set)
second_half = n_set.difference(m_set)

whole_diff = sorted(first_half.union(second_half))

print('Symmetric differences:')
for i in whole_diff:
    print(i)