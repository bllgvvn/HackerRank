# You are given a set A and N number of other sets.
# These N number of sets have to perform some specific mutation operation on set A.
# Your task is to execute those operations and print the sum of the elements from set A.

a = int(input('Enter the number of elements in set A: '))
a_set = set(map(int, input('Enter the elements of set A: ').split()))
n = int(input('Enter the number of operations: '))

for _ in range(n):
    change = input('Enter the operation and the elements: ').split()
    change_set = set(map(int, input('Enter the elements for the operation: ').split()))
    
    if change[0] == 'update':
        a_set.update(change_set)
    elif change[0] == 'intersection_update':
        a_set.intersection_update(change_set)
    elif change[0] == 'difference_update':
        a_set.difference_update(change_set)
    elif change[0] == 'symmetric_difference_update':
        a_set.symmetric_difference_update(change_set)

print('Sum of elements in set A:', sum(a_set))