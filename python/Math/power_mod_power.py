# You are given three integers a, b, and m.
# On the first line, print the result of pow(a, b).
# On the second line, print the result of pow(a, b, m).

a = int(input('Enter the first integer (a): '))
b = int(input('Enter the second integer (b): '))
m = int(input('Enter the third integer (m): '))

first = pow(a, b)
second = pow(a, b, m)

print('pow(a, b):', first)
print('pow(a, b, m):', second)