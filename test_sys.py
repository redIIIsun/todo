import sys

# import dateutil.parser
# from datetime import datetime
from to_do import read_list, task_list
#
# a = sys.argv
# print(a)
# if a[1] == 'add':
#     has_due = False
#     if 'due' in a[-1]:
#         has_due = True
#         due = a[-1]
#         date = due[4:]
#         print( 'Дедлайн', date)
#     if has_due:
#         str1 = ' '.join(a[2:-1])
#         print(str1)
#     else:
#         str1 = ' '.join(a[2:])
#     print(str1)
task_deskription = sys.argv

# def read_list():
#     list = []
#     with open('todo.txt', 'r') as m:
#         list = m.read().splitlines()
#         for line in m:
#             list = line.strip('')
#         return list
#
# def done_task(list):
#     x = int(note[1]) #поменять в [] на +1
#     done_str = list.pop(x)
#     print(done_str)
#     done_str = done_str.replace(done_str, 'x ' + done_str, 1)
#     with open('todo.txt', 'w') as m:
#         list.append(done_str)
#         m.write('\n'.join(list))


# def remove_task(list):
#     read_list()
#     if note[1] == 'remove':
#         x = int(note[2])
#         print(type(list))
#         # remove_str = list.pop(x) # поменять в [] на +1
#         # print(remove_str)


#
# list = read_list()
# done_task(list)
# remove_task(list)


def print_task():
    task_list = read_list()
    task_list = sorted(task_list, reverse=False)
    print('\nTODO:', '\n_____________________')
    linenum = int(task_deskription[2])
    task = task_list.pop(linenum - 1)
    note = task_deskription[1]
    note_task(linenum, task, note)  # как ее вставить что бы она на место возвращала строку???
    for index, task in enumerate(task_list, 1):
        unf_task = f'{index}: {task}'
        # print(unf_task)
        key = 'x'
        if key not in unf_task:
            print(unf_task)
    note_task(linenum, task, note)

def note_task(linenum, task, note):
    task_list = read_list()
    task_list = sorted(task_list, reverse=False)
    # print('\nTODO:', '\n_____________________')
    # for index, task in enumerate(task_list, 1):
        # unf_task = f'{index}: {task}'
        # # print(unf_task)
        # key = 'x'
        # if key not in unf_task:
        #     # print(unf_task)

    if task_deskription[1] == 'done':
        note = '- ЗАВЕРШЕНО'
        print(f'{linenum}: {task} {note}', end='\n')
    elif task_deskription[1] == 'due':
        note = '- ИЗМЕНЕН СРОК'
        print(f'{linenum}: {task} {note}', end='\n')
    elif task_deskription[1] == 'undo':
            note = '- ВОССТАНОВЛЕНО'
            print(f'{linenum}: {task} {note}', end='\n')
    elif task_deskription[1] == 'edit':
            note = '- ИЗМЕНЕНО'
            print(f'{linenum}: {task} {note}', end='\n')

print_task()

# res = datetime.strptime('%Y-%m-%dT')
# print(res)

task_list = read_list()


