
num_of_students = int(input())

students = {}

for student in range(num_of_students):
    name = input()
    score = float(input())
    students[name] = score

unique_scores = sorted(set(students.values()))
second_lowest_students = []  
second_lowest = unique_scores[1]

for name, score in students.items():
    if score == second_lowest:  
        second_lowest_students.append(name)  


second_lowest_students.sort()

for student in second_lowest_students:
    print(student)