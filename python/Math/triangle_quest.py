# You are given a positive integer N. Print a numerical triangle of height N - 1 like the one below:
# For example, if N = 5, the output should be:
# 1
# 22
# 333
# 4444

# Use no more than two lines.

for i in range(1, int(input('Enter a positive integer: ').strip())):
    print((pow(10, i) // 9) * i)