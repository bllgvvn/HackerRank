# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the elements of the list in order.
# remove e: Remove the first occurrence of integer e from the list.
# append e: Insert integer e at the end of the list.
# sort: Sort the list in ascending order.
# pop: Remove and return the last element of the list.
# reverse: Reverse the order of the list.
# Initialize your list and read in the value of n followed by n lines of commands.

N = int(input("Enter number of commands: "))
my_list = []
    
for iteration in range(N):
    user_input = input("Enter command: ").split()

    if user_input[0] == 'insert':
        my_list.insert(int(user_input[1]), int(user_input[2]))
    elif user_input[0] == 'print':
        print(my_list)
    elif user_input[0] == 'append':
        my_list.append(int(user_input[1]))
    elif user_input[0] == 'remove':
        my_list.remove(int(user_input[1]))
    elif user_input[0] == 'pop':
        my_list.pop()
    elif user_input[0] == 'sort':
        my_list.sort()
    elif user_input[0] == 'reverse':
        my_list.reverse()
