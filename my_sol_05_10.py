import csv

with open("Corp_Summary.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ";"
    file_reader = csv.reader(r_file, delimiter=";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0

def department_hierarchy():
    dep_names = []  # лист с названиями всех департаментов
    d_groups = dict()  # словарь, где ключи - департаменты, а значения - лист с командами
    for row in file_reader:
        if row[1] not in dep_names:
            dep_names.append(row[1])
            d_groups[row[1]] = [row[2]]
        else:
            if row[2] not in d_groups[row[1]]:
                groups = d_groups[row[1]].append(row[2])
                d_groups[row[1]] = groups
    return d_groups

def hierarchy_print(dep_hier: dict):
    print('Иерархия команд:')
    for key in dep_hier:
        print(f' Департамент {key}:')
        for group in dep_hier[key]:
            print(f' --{group}')
    return

def department_report():
    dep_names = []  # лист с названиями всех департаментов
    d_groups = dict()  # словарь, где ключи - департаменты, а значения - лист с кол-вом человек, общей зп и командами
    for row in file_reader:
        if row[1] not in dep_names:
            dep_names.append(row[1])
            d_groups[row[1]] = [0, int(row[5]), int(row[5]), int(row[5]), row[2]]
        else:
            if row[2] not in d_groups[row[1]]:
                groups = d_groups[row[1]].append(row[2])
                groups[0] += 1  # счётчик работников
                groups[1] += int(row[5])  # увеличиваем суммарную зп
                if int(row[5]) > groups[3]:  # если зп больше макс, то меняем макс
                    groups[3] = int(row[5])
                if int(row[5]) < groups[2]:  # если зп меньше мин, то меняем мин
                    groups[2] = int(row[5])
                d_groups[row[1]] = groups
            else:
                groups = d_groups[row[1]]
                groups[0] += 1  # счётчик работников
                groups[1] += int(row[5])  # увеличиваем суммарную зп
                if int(row[5]) > groups[3]:  # если зп больше макс, то меняем макс
                    groups[3] = int(row[5])
                if int(row[5]) < groups[2]:  # если зп меньше мин, то меняем мин
                    groups[2] = int(row[5])
                d_groups[row[1]] = groups
                d_groups[row[1]] = groups
    return d_groups

def dep_report_print(dep_rep: dict):
    print('Отчёт по департаментам:')
    for key in dep_rep:
        print(f' Департамент {key}:')
        print(
            f' --Количество человек: {dep_rep[key[0]]}; \n --Средняя зарплата: {dep_rep[key[1]] / dep_rep[key[0]]}; \n, --Минимальная зарплата {dep_rep[key[2]]}; \n --Максимальная зарплата {dep_rep[key[3]]}')
        print('  Список команд:')
        for i in range(2, len(dep_rep[key])):
            print(f'  --{dep_rep[key][i]}')

print('Какой функцией Вы хотите воспользоваться?')
print('1. Вывести иерархию команд')
print('2. Вывести сводный отчёт по департаментам')
print('3. Сохранить сводный отчёт')
print('Введите номер функции')
if input() == '1':
    hierarchy_print(department_hierarchy())
elif input() == '2':
    dep_report_print(department_report())
else:
    with open('sw_data_new.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(department_report())
