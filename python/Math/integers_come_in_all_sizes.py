# Read four numbers a, b, c, and d, and print te result of pow(a, b) + pow(c, d).

a = int(input('Enter the first integer (a): '))
b = int(input('Enter the second integer (b): '))
c = int(input('Enter the third integer (c): '))
d = int(input('Enter the fourth integer (d): '))

cal =  pow(a, b) + pow(c, d)
print('Result: ', cal)