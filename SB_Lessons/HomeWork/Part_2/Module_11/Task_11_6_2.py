# Задача 2. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость»
# (список из пяти элементов). Затем создайте список из десяти студентов
# (данные о студентах можете придумать или запросить у пользователя)
# и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.

class Student:

    def __init__(self, name, group, *args):
        self.name = name
        self.group = group
        self.grade = list(args)
        self.avg_score = sum(self.grade) / len(self.grade)

    def print_info(self):
        print(f'{self.name}, group: {self.group}, average score: {self.avg_score}')


stdnt1 = Student('aaa', 'q-1', 5, 5, 4, 5, 5)
stdnt2 = Student('bbb', 'r-6', 4, 3, 4, 5, 5)
stdnt3 = Student('ccc', 'u-4', 3, 4, 4, 5, 5)
stdnt4 = Student('ddd', 'o-2', 5, 3, 3, 3, 4)
stdnt5 = Student('eee', 'x-9', 5, 5, 5, 5, 3)

students_list = [stdnt1, stdnt2, stdnt3, stdnt4, stdnt5]
sorted_students = sorted(students_list, key=lambda stdnt: stdnt.avg_score)

for stdnt in sorted_students:
    stdnt.print_info()
