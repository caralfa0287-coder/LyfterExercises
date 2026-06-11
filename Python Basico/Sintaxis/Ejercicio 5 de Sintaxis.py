counter_of_grades = 1
approved_grades = 0
disapproved_grades = 0
approved_grades_average = 0
disapproved_grades_average = 0
total_grades_average = 0
grades = []
print("Ingrese la cantidad de notas:")
number_of_grades = int(input())
while counter_of_grades <= number_of_grades:
    print("Ingrese la nota número " + str(counter_of_grades) + ":")
    grade = int(input())
    grades.append(grade)
    if grade >= 70:
        approved_grades += 1
        approved_grades_average += grade
    else:
        disapproved_grades += 1
        disapproved_grades_average += grade
    counter_of_grades += 1
total_grades_average = approved_grades_average + disapproved_grades_average
if approved_grades == 0:
    approved_grades_average = ("Sin Datos")
else:
    approved_grades_average = approved_grades_average / approved_grades

if disapproved_grades == 0:
    disapproved_grades_average = ("Sin Datos")
else:
    disapproved_grades_average = disapproved_grades_average / disapproved_grades
total_grades_average = total_grades_average / number_of_grades
print("Cantidad de notas aprobadas: " + str(approved_grades))
print("Promedio de notas aprobadas: " + str(approved_grades_average))
print("Cantidad de notas desaprobadas: " + str(disapproved_grades))
print("Promedio de notas desaprobadas: " + str(disapproved_grades_average))
print("Promedio total de notas: " + str(total_grades_average))
