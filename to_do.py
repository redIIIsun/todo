import sys
from datetime import date
task_description = sys.argv
# task = str(input('Запланировать задачу: '))
# def due_task():
#     date_entry = input('Введите дату (н-р: 2017,7,1) - ', ) #убрать и сделать через sys add или еще что то
#     year, month, day = map(int, date_entry.split(','))
#     due = date(year, month, day)
#     return str(due)

def add_task():
    with open('todo.txt', 'a') as f: #, encoding='utf-8'
        today = date.today().strftime('%Y-%m-%d') #запись в виде строки
        s = ' '.join(task_description[1:])
        a = f.write(f'{today} {s[4:]} \n')
        return a
# def add_task():
#     with open('todo.txt', 'a', encoding='utf-8') as f:
#         today = date.today().strftime('%Y-%m-%d') #запись в виде строки
#         return f.write(f'{today} {task} \n')
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


def find_task(): #находит стороку по номеру
    # find_num = []
    with open('todo.txt', 'r') as m:
        s = m.readlines()
        for index,value in enumerate(s,1): #(s,1) замена порядкового намера с 0 на 1
            if int(index) == int(task_description[2]):
                print(s[int(task_description[2]) - 1]) # использовать как срез в прочитанном списке и убрать вообще эту функцию
                
                find_num = (f'{index} {value}')
                return find_num, index, value

def done_task(find_num, index, value):# меняет стороку с заданым номером
    with open('todo.txt', 'a') as m:
        if int(task_description[2]) == int(index):
            index = str(index)
            result = find_num.replace(index,'x', 1) #(_,_,1) где 1 это порядок вхождения символа в строку

        m.write(result)
        print(result)









# def read_task():
#     with open('todo.txt', 'r', encoding='utf-8') as m:
#        list =  m.read().splitlines() #читает список без последнего знака в строке
#        d = 0
#        print('\nTODO:', '\n_____________________')
#        for i in list[0:-1]: # range список без последней строки
#           d += 1
#           print(f'{d} {i}', end='\n')
#        print(d+1,list[-1],end='- Добавлено')




# def search_task():
#     d = {}
#     with open('todo.txt', 'r', encoding='utf-8') as file:  # открывает файл с правильной кодировкой
#         your_data = file.readlines()
#     for kwargs in your_data:
#         key = kwargs.split(':')[0].strip()    #.split(':')[1] разбивает строку на : и принимает второй элемент (значение)
#         value = kwargs.split(':')[1].strip()    #.strip() удаляет значение из первого пробела
#         d[key] = value
#     return d
# print(search_task())
# add_task()
# read_task()

    # print((s + 1), ': ',b , ' - ДОБАВЛЕНО')
    # print('\n', 'TODO:' '\n', '__________________', '\n')
    # print(a =+ 1, ': ', ' - ДОБАВЛЕНО')


