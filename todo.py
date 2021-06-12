import sys
from datetime import date

from to_do import add_task, read_alltask, read_addtask, read_list, done_task, task_list, remove_task, edit_task, add_due


task_description = sys.argv

if task_description[1] == 'add':
    add_task()
    read_addtask()

elif task_description[1] == 'all':
    print(read_alltask())

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
    done_task(task_list)

# if task_description[0] == 'todo.txt.py':
#     print('Показать не завершенные, но это еще нужно придумать', read_task())

# # C:\WINDOWS\system32>python C:\PyCharm\PythonHomeWorkKazan\todo.txt\todo.txt.py