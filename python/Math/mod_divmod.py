a = int(input('Enter first integer: ').strip())
b = int(input('Enter second integer: ').strip())

int_div = a // b
mod = a % b

print('Integer Division:', int_div)
print('Modulus:', mod)
print('Divmod:', divmod(a, b))