import sys
from datetime import date
task_description = sys.argv
# task = str(input('Запланировать задачу: '))
# def due_task():
#     date_entry = input('Введите дату (н-р: 2017,7,1) - ', ) #убрать и сделать через sys add или еще что то
#     year, month, day = map(int, date_entry.split(','))
#     due = date(year, month, day)
#     return str(due)
def read_list(): #читает список
    task_list = []
    with open('todo.txt', 'r') as m:
        task_list = m.read().splitlines()
        for line in m:
            task_list = line.strip('')
        return task_list

def add_task():
    with open('todo.txt', 'a') as f: #, encoding='utf-8'
        today = date.today().strftime('%Y-%m-%d') #запись в виде строки
        s = ' '.join(task_description[1:])
        a = f.write(f'{today} {s[4:]} \n')
        return a
#
def read_alltask():
    with open('todo.txt', 'r') as m:
       input_task =  m.read().splitlines() #читает список без последнего знака в строке
       d = 0
       print('\nTODO:', '\n_____________________')
       for i in input_task[0:]:# range список без последней строки
           d += 1
           print(f'{d} {i}', end='\n')

def read_addtask():
    with open('todo.txt', 'r') as m:
       input_task =  m.read().splitlines() #читает список без последнего знака в строке
       d = 0
       print('\nTODO:', '\n_____________________')
       for i in input_task[0:-1]:# range список без последней строки
           d += 1
           print(f'{d} {i}', end='\n')
       print(d+1,input_task[-1],'- Добавлено', end = '\n')

# def find_task():
#     find_str = []
#     with open('todo.txt', 'r') as m:
#         find_str = m.readlines()
#         for line in m:
#             find_str = line.strip('')
#         # print(find_str)
#         print(find_str[3])
# find_task()

def find_task(): #находит стороку по номеру
    with open('todo.txt', 'r') as m:
        find_str = m.readlines()
        for line in m:
            find_str = line.strip('')
        x = int(task_description[2])
        find_str.insert(0,'x')
        print(find_str[x])

def done_task(task_list):
    x = int(task_description[2])
    done_str = task_list.pop(x - 1) # -1 потому что иначе со второй строки читает
    print(done_str)
    done_str = done_str.replace(done_str, 'x ' + done_str, 1)
    with open('todo.txt', 'w') as m:
        task_list.append(done_str)
        m.write('\n'.join(task_list))

task_list = read_list()









