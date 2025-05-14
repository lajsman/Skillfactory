import random

# Список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()

# Список предметов
classes = ['Математика', 'Русский язык', 'Информатика']

# Пустой словарь с оценками по каждому ученику и предмету
students_marks = {}

# Генерируем данные по оценкам
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for _ in range(3)]
        students_marks[student][class_] = marks

# Функция для вывода всех оценок по всем ученикам
def print_all_marks():
    for student in students:
        print(student)
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
        print()

# Функция для вывода среднего балла по всем предметам по каждому ученику
def print_average_marks():
    for student in students:
        print(student)
        for class_ in classes:
            marks_sum = sum(students_marks[student][class_])
            marks_count = len(students_marks[student][class_])
            print(f'{class_} - {marks_sum // marks_count}')
        print()

# Функция для добавления оценки
def add_mark():
    student = input('Введите имя ученика: ')
    class_ = input('Введите предмет: ')
    mark = int(input('Введите оценку: '))
    if student in students_marks and class_ in students_marks[student]:
        students_marks[student][class_].append(mark)
        print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
    else:
        print('ОШИБКА: неверное имя ученика или название предмета')

# Функция для удаления оценки
def remove_mark():
    student = input('Введите имя ученика: ')
    class_ = input('Введите предмет: ')
    mark = int(input('Введите оценку для удаления: '))
    if student in students_marks and class_ in students_marks[student]:
        if mark in students_marks[student][class_]:
            students_marks[student][class_].remove(mark)
            print(f'Оценка {mark} для {student} по предмету {class_} удалена')
        else:
            print('ОШИБКА: оценка не найдена')
    else:
        print('ОШИБКА: неверное имя ученика или название предмета')

# Функция для редактирования оценки
def edit_mark():
    student = input('Введите имя ученика: ')
    class_ = input('Введите предмет: ')
    old_mark = int(input('Введите старую оценку: '))
    new_mark = int(input('Введите новую оценку: '))
    if student in students_marks and class_ in students_marks[student]:
        if old_mark in students_marks[student][class_]:
            index = students_marks[student][class_].index(old_mark)
            students_marks[student][class_][index] = new_mark
            print(f'Оценка {old_mark} для {student} по предмету {class_} изменена на {new_mark}')
        else:
            print('ОШИБКА: старой оценки не найдено')
    else:
        print('ОШИБКА: неверное имя ученика или название предмета')

# Функция для добавления предмета
def add_class():
    new_class = input('Введите название нового предмета: ')
    if new_class not in classes:
        classes.append(new_class)
        for student in students:
            students_marks[student][new_class] = []
        print(f'Предмет {new_class} добавлен')
    else:
        print('ОШИБКА: предмет уже существует')

# Функция для удаления предмета
def remove_class():
    class_ = input('Введите название предмета для удаления: ')
    if class_ in classes:
        classes.remove(class_)
        for student in students:
            students_marks[student].pop(class_, None)
        print(f'Предмет {class_} удален')
    else:
        print('ОШИБКА: предмет не найден')

# Функция для редактирования предмета
def edit_class():
    old_class = input('Введите старое название предмета: ')
    new_class = input('Введите новое название предмета: ')
    if old_class in classes:
        index = classes.index(old_class)
        classes[index] = new_class
        for student in students:
            students_marks[student][new_class] = students_marks[student].pop(old_class)
        print(f'Предмет {old_class} изменен на {new_class}')
    else:
        print('ОШИБКА: предмет не найден')

# Функция для удаления ученика
def remove_student():
    student = input('Введите имя ученика для удаления: ')
    if student in students:
        students.remove(student)
        students_marks.pop(student, None)
        print(f'Ученик {student} удален')
    else:
        print('ОШИБКА: ученик не найден')

# Функция для редактирования имени ученика
def edit_student():
    old_name = input('Введите старое имя ученика: ')
    new_name = input('Введите новое имя ученика: ')
    if old_name in students:
        index = students.index(old_name)
        students[index] = new_name
        students_marks[new_name] = students_marks.pop(old_name)
        print(f'Имя ученика изменено с {old_name} на {new_name}')
    else:
        print('ОШИБКА: ученик не найден')

# Функция для вывода всех оценок по определенному ученику
def print_student_marks():
    student = input('Введите имя ученика: ')
    if student in students_marks:
        print(f'Оценки для {student}:')
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
    else:
        print('ОШИБКА: ученик не найден')

# Функция для вывода среднего балла по каждому предмету для определенного ученика
def print_student_avg_marks():
    student = input('Введите имя ученика: ')
    if student in students_marks:
        print(f'Средний балл для {student}:')
        for class_ in classes:
            marks_sum = sum(students_marks[student][class_])
            marks_count = len(students_marks[student][class_])
            print(f'{class_} - {marks_sum // marks_count}')
    else:
        print('ОШИБКА: ученик не найден')

# Главный цикл программы
def main():
    print('''Список команд:
    1. Добавить оценку ученика по предмету
    2. Удалить оценку ученика по предмету
    3. Редактировать оценку ученика по предмету
    4. Вывести средний балл по всем предметам по каждому ученику
    5. Вывести все оценки по всем ученикам
    6. Добавить новый предмет
    7. Удалить предмет
    8. Редактировать предмет
    9. Удалить ученика
    10. Редактировать имя ученика
    11. Вывести все оценки для определенного ученика
    12. Вывести средний балл по каждому предмету для определенного ученика
    13. Выход из программы
    ''')

    while True:
        command = int(input('Введите команду: '))
        if command == 1:
            add_mark()
        elif command == 2:
            remove_mark()
        elif command == 3:
            edit_mark()
        elif command == 4:
            print_average_marks()
        elif command == 5:
            print_all_marks()
        elif command == 6:
            add_class()
        elif command == 7:
            remove_class()
        elif command == 8:
            edit_class()
        elif command == 9:
            remove_student()
        elif command == 10:
            edit_student()
        elif command == 11:
            print_student_marks()
        elif command == 12:
            print_student_avg_marks()
        elif command == 13:
            break
        else:
            print('ОШИБКА: неверная команда')

if __name__ == "__main__":
    main()
