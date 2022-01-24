#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Создаёт словарь "студент" и возвращает его
def get_student():

    # Переменная для студента с оценкой хуже 4
    student_bad = False

    # Все оценки
    evaluations = []

    # Средняя оценка
    average_estimation = 0

    # Запросить данные о студенте.
    name = input("Фамилия и инициалы: ")
    group = input("Номер группы: ")

    # Ввод 5-ти оценок
    print("Введите 5 оценок через Enter:")
    for i in range(5):
        estimation = int(input())
        evaluations.append(estimation)

    # Проходит по оценкам
    for i, x in enumerate(evaluations):
        # Если оценки только 4 и 5, то он считается хорошим
        if evaluations[i] == 4 or evaluations[i] == 5:
            average_estimation += evaluations[i]
        else:
            # Иначе плохим
            student_bad = True
            break

    # Только хороший студент заносится в список
    if not student_bad:

        # Вычисляется средняя оценка
        average_estimation /= 5

        # Создать словарь.
        return {
            'name': name,
            'group': group,
            'average_estimation': average_estimation,
            'evaluations': evaluations,
        }
    else:
        return 0


# Выводит список студентов
def show_list(staff):
    if staff:

        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )

        print(line)

        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Ф.И.О.",
                "Группа",
                "Средняя оценка"
            )
        )

        print(line)

        # Вывести данные о всех студентах.
        for idx, student in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group', ''),
                    student.get('average_estimation', 0)
                )
            )

        print(line)

    else:
        print("Список пуст")


# Выводит справку о работе с программой
def show_help():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
