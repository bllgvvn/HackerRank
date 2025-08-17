# Ms. Gabriel Williams is a botany professor at District College.
# One day, she asked her student Mickey to compute the average of all the plants
# with distinct heights in her greenhouse.

def average(array):
    distinct_height = set(arr)
    average_height = sum(distinct_height) / len(distinct_height)
    return round(average_height, 3)

if __name__ == '__main__':
    n = int(input('Enter the number of plants: '))
    arr = list(map(int, input('Enter the plants heights: ').split()))
    result = average(arr)
    print('Average height:', result)