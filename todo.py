import sys
# from datetime import datetime, date

from to_do import add_task, read_alltask, read_list,\
    done_task, task_list, remove_task, edit_task, add_due,\
    undo_task, search_task, un_finished_task, find_date_between, find_date_before,\
    find_date_after, find_due_between, find_due_before, find_due_after


task_description = sys.argv

if len(task_description) == 1:
    un_finished_task()

else:
    if task_description[1] == 'add':
        read_list()
        add_task()

    elif task_description[1] == 'all':
        read_alltask()

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


    elif task_description[1] == 'created' and task_description[2] == 'between':
        read_list()
        find_date_between()

    elif task_description[1] == 'created' and task_description[2] == 'before':
        read_list()
        find_date_before()

    elif task_description[1] == 'created' and task_description[2] == 'after':
        read_list()
        find_date_after()

    elif task_description[1] == 'between' and task_description[2] == 'due':
        read_list()
        find_due_between()

    elif task_description[1] == 'before' and task_description[2] =='due':
        read_list()
        find_due_before()
    elif task_description[1] == 'after' and task_description[2] == 'due':
        read_list()
        find_due_after()