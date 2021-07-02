import sys
from datetime import datetime, date

from to_do import add_task, read_alltask, print_task, read_list,\
    done_task,task_list, remove_task, edit_task, add_due,\
    undo_task, search_task, print_task, un_finished_task #,find_date_between #, date_input ,


task_description = sys.argv

if len(task_description) == 1:
    un_finished_task()

else:
    if task_description[1] == 'add':
        read_list()
        add_task()

    elif task_description[1] == 'all':
        read_alltask(task_list)

    elif task_description[1] == 'remove':
        read_list()
        remove_task(task_list)

    elif task_description[1] == 'edit':
        read_list()
        edit_task(task_list)

    elif task_description[1] == 'due':
        read_list()
        add_due()

    elif task_description[1] == 'done':
        read_list()
        done_task()

    elif task_description[1] == 'undo':
        read_list()
        undo_task()

    elif task_description[1] == 'search':
        read_list()
        search_task()


    # elif task_description[1] == 'created':
    #     read_list()
    #     find_date_between()
    #




# # C:\WINDOWS\system32>python C:\PyCharm\PythonHomeWorkKazan\todo.txt\todo.txt.py