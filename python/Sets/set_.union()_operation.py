# The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
# The second line contains n space-separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space-separated roll numbers of those students.
# Output the total number of students who have at least one subscription.

n = int(input('Enter the number of students who have subscribed to the English newspaper: '))
n_students = set(map(int, input('Enter the roll numbers of the students: ').split()))
b = int(input('Enter the number of students who have subscribed to the French newspaper: '))
b_students = set(map(int, input('Enter the roll numbers of the students: ').split()))

union = n_students.union(b_students)
print('Total number of students with at least one subscription:', len(union))