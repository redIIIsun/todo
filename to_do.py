import sys
from datetime import datetime, date

task_description = sys.argv


def read_list():    #   читает список из файла
    with open('todo.txt', 'r') as m:
        task_list = m.read().splitlines()
        for line in m:
            task_list = line.strip('')
        return task_list


def add_task():    # ввод задачи в файл
    with open('todo.txt', 'a') as m:     #  encoding='utf-8'
        today = date.today().strftime('%Y-%m-%d')   # запись в виде строки
        task = ' '.join(task_description[1:])
        task = task[4:]
        m.write(f'{today} {task.capitalize()} \n')
        linenum = len(read_list())+1
        task = '\n'.join(task_list)
        note = '- ДОБАВЛЕННО'
    print_task(linenum, task, note)


def done_task():     # задача по введеному номеру строки завершена
    linenum = int(task_description[2])
    task = task_list.pop(linenum - 1)  # -1 потому что иначе со второй строки читает
    print(task)
    note = '- ЗАВЕРШЕНО'
    task = task.replace(task, 'x ' + task, 1)
    with open('todo.txt', 'w') as m:
        task_list.append(task)
        m.write('\n'.join(task_list))
    print('\nTODO:', '\n_____________________')
    for index, tasks in enumerate(task_list, 1):
        if linenum == index:
            print(f'{index}: {task}' + note, end = '\n')
        else:
            if task in tasks:
                continue
            print(f'{index}: {tasks} ', end = '\n')


def read_all_task():   # выводит все задачи в файле
    task_list = read_list()
    all_tasks = sorted(task_list, reverse=False)
    print('\nTODO:', '\n_____________________')
    for index, task in enumerate(all_tasks, 1):
        print(f'{index}: {task} ', end='\n')


def remove_task(task_list):   # удаление или нет задачи по введеному номеру строки
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

    
def edit_task(task_list):   # редактирование задачи по введеному номеру строки
    linenum = int(task_description[2])
    task = task_list[linenum - 1]  # поиск по вхождению в список
    date_start = task[:11]
    variable_str = task[11:]   # срез строки без даты
    new_str = ' '.join(task_description[3:])
    # variable_str = task.replace(variable_str, new_str, 1)
    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = (f'{date_start}{new_str}')

        m.write('\n'.join(task_list))   # добавить вывод печати файла
    note = '- ИЗМЕНЕНО'
    print_task(linenum, task, note)


def date_input(date_entry):   # преобразованние введенной даты
    while True:
        try:
            year, month, day = map(int, date_entry.split('-'))
            date_in = date(year, month, day)
            return date_in
        except ValueError as error:
            print('Внимание!!!! введите дату через - ','\n')
            date_entry = input('Введите дату в формате YYYY-MM-DD : ', )


def add_due():   # добавить дату окончания к задаче по номеру строки
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
        newstr = task.replace('x','',1)
        print(newstr)
    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = f'{newstr[1:]}'
        m.write('\n'.join(task_list))
    note = 'ВОССТАНОВЛЕНО'
    print_task(linenum, task, note)


def search_task():   # поиск задачи по ключевому слову
    task = task_description[2]
    for index, tasks in enumerate(task_list, 1):
        if task in tasks:
            print(f'{index}: {tasks}')


def read_unfinished_task():  # чтение всех невыполненых заданий
    print('\nTODO:', '\n_____________________')
    for index, task in enumerate(read_list(), 1):
        all_tasks = f'{index}: {task}'
        if 'x' not in task[0]:
            print(all_tasks)

            
def print_task(linenum, task, note):  # вывод на экран невыполненых задач с пояснением к изменению
    task_list = read_list()
    print('\nTODO:', '\n_____________________')
    for index, task in enumerate(task_list, 1):
        if linenum == index:
            print(f'{linenum}: {task} {note}', end='\n')
        else:
            if 'x' in task[0] :
                continue
            print(f'{index}: {task}')


def find_date_between():   # поиск между двумя датами создания
    date_entry = task_description[3]
    date_one = date_input(date_entry)
    date_entry = task_description[4]
    date_two = date_input(date_entry)
    for index, task in enumerate(task_list, 1):
        if task[0:10] in task and task[0] != 'x':
            date_entry = task[0:10]
            date_find = datetime.strptime(date_entry, "%Y-%m-%d").date()
            if date_one <= date_find <= date_two:
                if str(date_find) in task:
                    print(f'{index}: {task}')


def find_date_before():  #   поиск по дате создания до введенной даты
    date_entry = task_description[3]
    date_one = date_input(date_entry)
    for index, task in enumerate(task_list, 1):
        if task[0:10] in task and task[0] != 'x':
            date_entry = task[0:10]
            date_find = datetime.strptime(date_entry, "%Y-%m-%d").date()
            if date_find <= date_one:
                print(f'{index}: {task}')


def find_date_after():  #  поиск по дате создания после введенной даты
    date_entry = task_description[3]
    date_one = date_input(date_entry)
    for index, task in enumerate(task_list, 1):
        if task[0:10] in task and task[0] != 'x':
            date_entry = task[0:10]
            date_find = datetime.strptime(date_entry, "%Y-%m-%d").date()
            if date_find >= date_one:
                print(f'{index}: {task}')


def find_due_between(): # поиск по дате выполнения между указанными датами
    date_entry = task_description[3]
    date_one = date_input(date_entry)
    date_entry = task_description[4]
    date_two = date_input(date_entry)
    for index, task in enumerate(task_list, 1):
        if 'due' in task and task[0] != 'x':
            due_entry = task[-10:]
            date_find = datetime.strptime(due_entry, "%Y-%m-%d").date()
            if date_one <= date_find <= date_two:
                if str(date_find) in task:
                    print(f'{index}: {task}')


def find_due_before(): #  поиск по дате выполнения до указанной даты
    date_entry = task_description[3]
    date_one = date_input(date_entry)
    for index, task in enumerate(task_list, 1):
        if 'due' in task and task[0] != 'x':
            due_entry = task[-10:]
            date_find = datetime.strptime(due_entry, "%Y-%m-%d").date()
            if date_find <= date_one:
                if str(date_find) in task:
                    print(f'{index}: {task}')


def find_due_after(): # поиск по дате выполнения после указанной даты
    date_entry = task_description[3]
    date_one = date_input(date_entry)
    for index, task in enumerate(task_list, 1):
        if 'due' in task and task[0] != 'x':
            due_entry = task[-10:]
            date_find = datetime.strptime(due_entry, "%Y-%m-%d").date()
            if date_find >= date_one:
                if str(date_find) in task:
                    print(f'{index}: {task}')



task_list = read_list()







