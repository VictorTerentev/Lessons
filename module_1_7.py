grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_and_average = {}

students_list = list(students)
students_list.sort()

i = 0
j = 0
ave = 0
count = 0
while i < grades.__len__():
    while j < grades[i].__len__():
        ave += grades[i][j]
        count +=1
        j +=1
    student_and_average.update({students_list[i]: ave / count})
    j = 0
    ave = 0
    count = 0
    i += 1

print(student_and_average)