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



def print_task():
    task_list = read_list()
    task_list = sorted(task_list, reverse=False)
    print('\nTODO:', '\n_____________________')
    linenum = int(task_deskription[2])
    task = task_list.pop(linenum - 1)
    note = task_deskription[1]
    for index, task in enumerate(task_list, 1):
        note_in = ''
        if linenum == index:
            note_in = note
        key = 'x'
        if key not in task:
            note_task(index, task, note_in)


def note_task(linenum, task, note_in):
    note = ''
    if note_in == 'done':
        note = '- ЗАВЕРШЕНО'
    elif note_in == 'due':
        note = '- ИЗМЕНЕН СРОК'
    elif note_in == 'undo':
        note = '- ВОССТАНОВЛЕНО'
    elif note_in == 'edit':
        note = '- ИЗМЕНЕНО'
    print(f'{linenum}: {task} {note}', end='\n')




print_task()

# res = datetime.strptime('%Y-%m-%dT')
# print(res)

task_list = read_list()


