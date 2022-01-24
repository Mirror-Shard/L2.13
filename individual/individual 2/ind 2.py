#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from paket import *

if __name__ == '__main__':

    # Список студентов.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:

        # Запросить команду из терминала.
        print("Команды - add, list, help, exit")
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        # Студент адд #################################
        if command == 'add':

            student = get_student()
            # Если возвращает 0 (условия записи студента не соблюдены)
            if student == 0:
                continue

            # Добавить словарь в список.
            students.append(student)

            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item['average_estimation'],
                              reverse=True)

        # Лист #######################################
        elif command == 'list':
            show_list(students)

        elif command == 'help':
            show_help()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
