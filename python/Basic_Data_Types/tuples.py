# Given an integer, n, and n space-separated integers as input,
# create a tuple, t, of those n intergers.
# Then compute and print the result of hash(t).

n = int(input("Enter the number of integers: "))
integer_list = map(int, input("Enter the space-separated integers: ").split())
t = tuple(integer_list)
print("The hash of the tuple is:", hash(t))