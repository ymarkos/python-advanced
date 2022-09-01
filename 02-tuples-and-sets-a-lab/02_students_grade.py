n = int(input())
students_strings_list = [input() for _ in range(n)]

students_grade = {}
for student_string in students_strings_list:
    student, grade_string = student_string.split()
    grade = float(grade_string)
    if student not in students_grade:
        students_grade[student] = []
    students_grade[student].append(grade)


def average(values):
    return sum(values)/len(values)


for student, grades in students_grade.items():
    grades_formatted = ' '.join(f'{grade:.2f}'for grade in grades)
    average_grade = average(grades)
    average_grd_formatted = f'{average_grade:.2f}'
    print(f'{student} -> {grades_formatted} (avg: {average_grd_formatted})')