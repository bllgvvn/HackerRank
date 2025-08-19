# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s.
# All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove, and/or discard commands followed by their associated value.

n = int(input('Enter the number of elements in the set: '))
s = set(map(int, input('Enter the elements of the set: ').split()))
N = int(input('Enter the number of commands: '))

for _ in range(N):
    command = input().split()
    if command[0] == 'remove':
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass
        
    elif command[0] == 'pop':
        try:
            s.pop()
        except KeyError:
            pass

    elif command[0] == 'discard':
        s.discard(int(command[1]))

print('Sum of the remaining set:', sum(s))