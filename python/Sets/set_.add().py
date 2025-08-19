# The first line contains an integer n, the total number of country stamps.
# The next n lines contains the name of the country where the stamp is from.
# Find the total number of distinct country stamps.

n = int(input('Enter the number of countries: '))
country_stamps = set()

for i in range(n):
    country_stamps.add(input('Enter the name of the country: '))

print('Number of distinct countries:', len(country_stamps))