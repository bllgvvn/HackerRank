# Given the names and grades of student in class of N students, 
# store them in a nested list and find the names of students with the second lowest grade.
# If there are multiple students with the same second lowest grade,
# order their names alphabetically and print each name on a new line.

def sort_students(names_scores):
    scores = []
    for student in names_scores:
        scores.append(student[1])
        
    sorted_scores = sorted(set(scores))
    second_lowest = sorted_scores[1]

    names_second_lowest = []
    for student in names_scores:
        if student[1] == second_lowest:
            names_second_lowest.append(student[0])
    names_second_lowest = sorted(names_second_lowest)

    for name in names_second_lowest:
        print("The second lowest student is:", name)


names_scores = []
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))
    names_scores.append([name, score])
sort_students(names_scores)