# The included code stub will read an integer, a, from input.
# Without using any string methods, try to print the following:
# 123...n

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i, end="")