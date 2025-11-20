from collections import defaultdict

n, m = list(map(int, input('Enter the number of elements in lists a and b separated by space: ').split()))

a_list = []
b_list = []

for a in range(n):
    a_list.append(input('Enter element {} of list a: '.format(a + 1)))
    
for b in range(m):
    b_list.append(input('Enter element {} of list b: '.format(b + 1)))
    
final_dict = defaultdict()

for b in b_list:
    if b in a_list:
        final_dict[b] = [i + 1 for i, x in enumerate(a_list) if x == b]
        print(' '.join(map(str, final_dict[b])))
    else:
        print(-1)