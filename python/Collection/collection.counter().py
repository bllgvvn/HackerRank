from collections import Counter

num_of_shoes = int(input('Enter the number of shoes:' ))
list_of_sizes = list(map(int, input('Enter the shoe sizes: ').split()))
num_of_customers = int(input('Enter the number of customers: '))

counter_of_sizes = Counter(list_of_sizes)

total = 0
for customer in range(num_of_customers):
    size, price = list(map(int, input('Enter the size and price: ').split()))
    if size in counter_of_sizes.keys():
        if counter_of_sizes[size] > 0:
            total += price
            counter_of_sizes[size] -= 1
            
print('Total earning: ', total)