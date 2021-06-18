import sys
from datetime import date
task_description = sys.argv
# note = str(input('Запланировать задачу: '))
# def due_task():
#     date_entry = input('Введите дату (н-р: 2017,7,1) - ', ) #убрать и сделать через sys add или еще что то
#     year, month, day = map(int, date_entry.split(','))
#     due = date(year, month, day)
#     return str(due)
# def read_file():
#     with open('todo.txt', 'r') as m:
#        input_task =  m.read().splitlines()
def read_list(): #читает список
    task_list = []
    with open('todo.txt', 'r') as m:
        task_list = m.read().splitlines()
        for line in m:
            task_list = line.strip('')
        return task_list

def add_task():
    with open('todo.txt', 'a') as m: #, encoding='utf-8'
        today = date.today().strftime('%Y-%m-%d') #запись в виде строки
        task = ' '.join(task_description[1:])
        rec_task = m.write(f'{today} {task[4:]} \n')
        return rec_task # можно было бы через f.seek() перенести курсор в начало,
        # но тогда при методе 'a' все удалится при последующей записи, что делать??????

def read_alltask(task_list):
    all_tasks = sorted(task_list, reverse=False)
    print('\nTODO:', '\n_____________________')
    for index, task in enumerate(all_tasks, 1):
        print(f'{index}: {task}')


def UnfinishedTask(): # чтение всех невыполненых заданий
    all_tasks = sorted(task_list, reverse=False)
    print('\nTODO:', '\n_____________________')
    for index, task in enumerate(all_tasks, 1):
        all_tasks = f'{index}: {task}'
        # дальше кусочек который нужно добавить что бы выводил только невыполненые
        key = 'x'
        if key not in all_tasks:
            print(all_tasks)

def read_addtask():
    task_list = read_list() #еще раз прочитывает глобальную переменную после исполнения файла
    print('\nTODO:', '\n_____________________')
    # print('\n'.join(task_list[:-1]))
    linenum = len(task_list)
    note = '- ДОБАВЛЕННО'
    for index, task in enumerate(task_list[:-1], 1):
        print(f'{index}: {task}')
    note_task(linenum, task, note)

def note_task(linenum, task, note):
    task_list = read_list()
    # linenum = int(task_deskription[2])
    task = task_list[linenum - 1]
    # note = task_deskription[1]  # как то связать с коммандами из строки ввода подписи
    print(f'{linenum}: {task} {note}')


# def find_task():
#     find_str = []
#     with open('todo.txt', 'r') as m:
#         find_str = m.readlines()
#         for line in m:
#             find_str = line.strip('')
#         # print(find_str)
#         print(find_str[3])
# find_task()

# def find_task(): #находит стороку по номеру
#     with open('todo.txt', 'r') as m:
#         find_str = m.readlines()
#         for line in m:
#             find_str = line.strip('')
#         x = int(note[2])
#         find_str.insert(0,'x')
#         print(find_str[x])

def done_task(task_list):
    linenum = int(task_description[2])
    done_str = task_list.pop(linenum - 1)  # -1 потому что иначе со второй строки читает
    print(done_str)
    done_str = done_str.replace(done_str, 'linenum ' + done_str, 1)
    with open('todo.txt', 'w') as m:
        task_list.append(done_str)
        m.write('\n'.join(task_list))

def remove_task(task_list):
    linenum = int(task_description[2])
    remove_str = task_list[linenum-1]
    print(f'{linenum}:{remove_str}')
    print(f'Вы хотите удалить задачу {linenum}? (y/n)')
    a = input()
    if a == 'y':
        remove_str = task_list.pop(linenum - 1)
        print('ЗАДАЧА УДАЛЕНА')
    else:
        print('ЗАДАЧА НЕ УДАЛЕНА')
    with open('todo.txt', 'w') as m:
        m.write('\n'.join(task_list))

def edit_task(task_list):
    linenum = int(task_description[2])
    edit_str = task_list[linenum - 1] # поиск по вхождению в список
    date_start = edit_str[:11]
    variable_str = edit_str[11:] # срез строки что б без даты
    new_str = ' '.join(task_description[3:])
    # variable_str = edit_str.replace(variable_str, new_str, 1)
    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = (f'{date_start}{new_str}')
        m.write('\n'.join(task_list)) # добавить вывод печати файла

def add_due():
    linenum = int(task_description[2])
    add_due = task_list[linenum - 1]
    print(add_due)
    date_entry = input('Введите дату завершения в формате г.м.д.(н-р: 2017.7.23) - ', )
    year, month, day = map(int, date_entry.split('.'))
    date_entry = date(year, month, day)
    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = (f'{add_due} due:{date_entry}')
        m.write('\n'.join(task_list))

def undo_task():
    linenum = int(task_description[2])
    undo_str = task_list[linenum - 1]
    if 'linenum' in undo_str:
        new_str = undo_str.replace('linenum','',1)
    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = f'{new_str[1:]}'
        m.write('\n'.join(task_list))
        print(new_str[1:], 'ВОССТАНОВЛЕНО')

def search_task():
    task = task_description[2]
    for i in task_list:
        if task in i:
            print(i)
            


task_list = read_list()
# print('_____Magic_____')









