# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

a = set(map(int, input('Enter the elements of set A: ').split()))
flag = 0
for i in range(int(input('Enter the number of other sets: '))):
    b = set(map(int, input('Enter the elements of other sets: ').split()))
    if a.issuperset(b):
        continue
    else:
        print('False')
        flag = 1
        break
        
if flag == 0:
    print('True')