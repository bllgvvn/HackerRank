# You are given a complex z. Your task is to convert it to polar coordinates.

import cmath

def polar_coordinates(z):
    r = abs(z)
    phase = cmath.phase(z)

    return r, phase

z = complex(input('Enter the complex number: ').strip())

r, theta = polar_coordinates(z)

print('Value of r: ', r)
print('Value of theta: ', theta)