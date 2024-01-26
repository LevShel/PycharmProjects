student_str = input('Enter space-separated information about student.\n'
     'Name, Surname, City, College, Graduates: '
                    )

student_info = student_str.split()
student = dict()
student['Name: '] = student_info[0]
student['Surname: '] = student_info[1]
student['City: '] = student_info[2]
student['College: '] = student_info[3]
student['Graduates: '] = []
for i_grade in student_info[4:]:
    student['Graduates: '].append(int(i_grade))

for each in student:
    print(each, student[each])