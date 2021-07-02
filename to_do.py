import sys
from datetime import datetime, date

task_description = sys.argv

def read_list(): #читает список из файла
    task_list = []
    with open('todo.txt', 'r') as m:
        task_list = m.read().splitlines()
        for line in m:
            task_list = line.strip('')
        return task_list

def add_task(): # ввод задачи в файл
    with open('todo.txt', 'a') as m: #, encoding='utf-8'
        today = date.today().strftime('%Y-%m-%d') #запись в виде строки
        task = ' '.join(task_description[1:])
        task = task[4:]
        m.write(f'{today} {task.capitalize()} \n')
        linenum = len(read_list())+1
        task = '\n'.join(task_list)
        note = '- ДОБАВЛЕННО'
    print_task(linenum, task, note)


def read_alltask(task_list): # выводит все задачи в файле
    all_tasks = sorted(task_list, reverse=False)
    print('\nTODO:', '\n_____________________')
    for index, task in enumerate(all_tasks, 1):
        print(f'{index}: {task}')

def done_task(): # задача по введеному номеру строки завершена
    linenum = int(task_description[2])
    task = task_list.pop(linenum - 1)  # -1 потому что иначе со второй строки читает
    print(task)
    task = task.replace(task, 'x ' + task, 1)
    with open('todo.txt', 'w') as m:
        task_list.append(task)
        m.write('\n'.join(task_list))
    note = '- ЗАВЕРШЕНО'
    print_task(linenum, task, note)


def remove_task(task_list): # удаление или нет задачи по введеному номеру строки
    linenum = int(task_description[2])
    task = task_list[linenum-1]
    print(f'{linenum}:{task}')
    print(f'Вы хотите удалить задачу {linenum}? (y/n)')
    a = input()
    if a.lower() == 'y':
        task = task_list.pop(linenum - 1)
        print('ЗАДАЧА УДАЛЕНА')
    elif a.lower() == 'n':
        print('ЗАДАЧА НЕ УДАЛЕНА')
    with open('todo.txt', 'w') as m:
        m.write('\n'.join(task_list))
    
def edit_task(task_list): # редактирование задачи по введеному номеру строки
    linenum = int(task_description[2])
    task = task_list[linenum - 1] # поиск по вхождению в список
    date_start = task[:11]
    variable_str = task[11:] # срез строки что б без даты
    new_str = ' '.join(task_description[3:])
    # variable_str = task.replace(variable_str, new_str, 1)
    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = (f'{date_start}{new_str}')

        m.write('\n'.join(task_list)) # добавить вывод печати файла
        # print('\n'.join(task_list))
    note = '- ИЗМЕНЕНО'
    print_task(linenum, task, note)


def date_input(date_entry):
    while True:
        try:
            year, month, day = map(int, date_entry.split('-'))
            date_in = date(year, month, day)
            return date_in
        except ValueError as error:
            print('Внимание!!!! введите дату через - ','\n')
            date_entry = input('Введите дату в формате YYYY-MM-DD : ', )

def add_due(): # добавить дату окончания к задаче по номеру строки
    linenum = int(task_description[2])
    task = task_list[linenum - 1]
    print(task)
    date_entry = task_description[3]
    date_in = date_input(date_entry)

    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = (f'{task} due:{date_in}')
        m.write('\n'.join(task_list))
    note = '- ИЗМЕНЕН СРОК'
    print_task(linenum, task, note)

def undo_task(): # снять отметку о выполнении в задаче по номеру
    linenum = int(task_description[2])
    task = task_list[linenum - 1]
    if 'x ' in task:
        new_str = task.replace('x','',1)
        print(new_str)
    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = f'{new_str[1:]}'
        m.write('\n'.join(task_list))
    note = 'ВОССТАНОВЛЕНО'
    print_task(linenum, task, note)

def search_task(): # поиск задачи по ключевому слову
    task = task_description[2]
    for i in task_list:
        if task in i:
            print(i)

def un_finished_task(): # чтение всех невыполненых заданий
    all_tasks = sorted(task_list, reverse=False)
    print('\nTODO:', '\n_____________________')
    for index, task in enumerate(all_tasks, 1):
        all_tasks = f'{index}: {task}'
        # дальше кусочек который нужно добавить что бы выводил только невыполненые
        key = 'x'
        if key not in all_tasks:
            print(all_tasks)
            
def print_task(linenum, task, note): # вывод на экран невыполненых задач с пояснением к изменению
    task_list = read_list()
    # task_list = sorted(task_list, reverse = False)
    print('\nTODO:', '\n_____________________')
    for index, task in enumerate(task_list, 1):
        if linenum == index:
            print(f'{linenum}: {task} {note}', end='\n')
        else:
            if 'x' in task:
                continue
            print(f'{index}: {task}')





# def find_date_between():
#     task_description[3] = date_one
#     date_one = date_input()
#     task_description[4] = date_two
#     date_two = date_input()
#       while date_one <= i <= date_two:
#         for i in task_list:
#
#             print(i)


task_list = read_list()
# print('_____Magic_____')









