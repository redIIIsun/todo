import sys
from datetime import date

from to_do import add_task, read_alltask, read_addtask, find_task, done_task

task_description = sys.argv

if task_description[1] == 'add':
    add_task()
    read_addtask()

elif task_description[1] == 'all':
    print(read_alltask())

elif task_description[1] == 'done':
    a, b, c = find_task()
    done_task(a, b, c)


# elif task_description[1] == 'remove':


# if task_description[0] == 'todo.txt.py':
#     print('Показать не завершенные, но это еще нужно придумать', read_task())

# # C:\WINDOWS\system32>python C:\PyCharm\PythonHomeWorkKazan\todo.txt\todo.txt.py