# Given the participant's score list, find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

def runner_up(arr_students):
    arr_students = list(arr_students)
    arr_students.sort(reverse=True)
    for score in range(len(arr_students)):
        if arr_students[score] != arr_students[score + 1]:
            runner_up = arr_students[score + 1]
            break
        else:
            continue
    print("Runner-up score: ", runner_up)

n = int(input("Enter number of scores: "))
arr = map(int, input("Enter scores: ").split())
runner_up(arr)
