# You are given a positive integer N.
# Your task is to print a palidromic triangle of size N.

for i in range(1,int(input('Enter the size of the palindromic triangle: '))+1): 
    print(pow((pow(10, i) // 9), 2))