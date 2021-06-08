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
    list = []
    with open('todo.txt', 'r') as m:
        list = m.readlines()
        for line in m:
            list = line.strip('')
        return list

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

def done_task(find_num, index, value):# меняет стороку с заданым номером
    with open('todo.txt', 'a') as m:
        if int(task_description[2]) == int(index):
            index = str(index)
            result = find_num.replace(index,'x', 1) #(_,_,1) где 1 это порядок вхождения символа в строк
        m.write(result)
        print(result)

list = read_list()









