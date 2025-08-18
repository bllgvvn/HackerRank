# Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

M = int(input('Enter the number of elements in set M: '))
m_list = input('Enter the elements of set M: ')
m_list = m_list.split()
m_list = map(int, m_list)
m_set = set(m_list)

N = int(input('Enter the number of elements in set N: '))
n_list = input('Enter the elements of set N: ')
n_list = n_list.split()
n_list = map(int, n_list)
n_set = set(n_list)

first_half = m_set.difference(n_set)
second_half = n_set.difference(m_set)

whole_diff = sorted(first_half.union(second_half))

print('Symmetric differences:')
for i in whole_diff:
    print(i)