# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.
# Output total number of students who have subscribed to the English or the French newspaper but not both.

eng = int(input('Enter the number of students who have subscribed to the English newspaper: '))
eng_students = set(map(int, input('Enter the roll numbers of students who have subscribed to the English newspaper: ').split()))
fre = int(input('Enter the number of students who have subscribed to the French newspaper: '))
fre_students = set(map(int, input('Enter the roll numbers of students who have subscribed to the French newspaper: ').split()))

not_both = eng_students.symmetric_difference(fre_students)
print('Total number of students who have subscribed to the English or the French newspaper but not both:', len(not_both))