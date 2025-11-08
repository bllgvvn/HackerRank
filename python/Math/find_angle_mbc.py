import math

ab = int(input('Enter length of side AB: '))
bc = int(input('Enter length of side BC: '))

theta = math.degrees(math.atan2(ab, bc))

print('Angle MBC: ', round(theta), '\u00B0', sep='')