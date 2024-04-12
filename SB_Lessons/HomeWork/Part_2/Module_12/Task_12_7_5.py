# Задача 5. Стек
# Что нужно сделать
# Мы уже говорили, что в программировании нередко необходимо создавать свои собственные структуры
# данных на основе уже существующих. Одной из таких базовых структур является стек.
# Стек — это абстрактный тип данных, представляющий собой список элементов, организованных
# по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
# Простой пример: стек из книг на столе. Единственной книгой, обложка которой видна, является
# самая верхняя. Чтобы получить доступ, например, к третьей снизу книге, нам нужно убрать все
# книги, лежащие сверху, одну за другой.
# Напишите класс, который реализует стек и его возможности (достаточно будет добавления
# и удаления элемента).
# После этого напишите ещё один класс — «Менеджер задач». В менеджере задач можно выполнить
# команду «новая задача», в которую передаётся сама задача (str) и её приоритет (int).
# Сам менеджер работает на основе стека (не наследование). При выводе менеджера в консоль
# все задачи должны быть отсортированы по следующему приоритету: чем меньше число, тем выше
# задача.
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать ДЗ", 2)
# print(manager)
# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду
# Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.

class Task:
    def __init__(self, position=None, text=None):
        self.task = {int(position): str(text)}

    def add_task(self, position=None, text=None):
        self.task[position] = text

    def delete_task(self, position):
        del self.task[position]

    def edit_task(self, position, new_text):
        self.task[position] = new_text

    def get_tasks(self):
        return self.task


class TaskManager:

    def __init__(self):
        self.task_list = []

    def new_task(self, position, text):
        task = Task(position, text)
        self.task_list.append(task)

    def __str__(self):
        sorted_tasks = []
        for task in self.task_list:
            sorted_tasks.append(task.get_tasks())
        # TODO настроить вывод каждой задачи в новой строке:
        #  COMPLETED: см. ../SB_Lessons/Part_2/Lesson_2_13/Stack_TaskManager.py
        return str(sorted(sorted_tasks, key=lambda x: list(x.keys())))


manager = TaskManager()
manager.new_task(4, 'make cleaning')
manager.new_task(4, 'wash dishes')
manager.new_task(1, 'relax')
manager.new_task(2, 'eat')
manager.new_task(2, 'do homework')
print(manager)
