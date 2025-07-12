# The provided code stub reads an integer, n, from input,
# For all non-negative integers i < n, print i^2.

n = int(input("Enter a number: "))
for i in range(0, n):
    print("Square values of non-negative integers:", i * i)