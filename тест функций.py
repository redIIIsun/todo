# def replase_str():
#     with open ('todo.txt', 'r') as f:
#         old_data = f.read()
#     new_data = old_data.replace('еще какая нибудь строка','что нибудь тут лежит предположим', 1 )
#     with open ('todo.txt', 'w') as f:
#         f.write(new_data)
#     print(new_data)
# replase_str()


# def todo_task(find_num, index, value):#тут в () по хорошему должен вызываться список find_task
#     with open('todo.txt', 'a') as m:
#         if int(note[2]) == int(index):
#             index = str(index)
#             result = find_num.replace(index,'x', 1)
#     with open('todo.txt', 'a') as f:
#         f.write(result)
#         print(result)

#про методы строк можно подробно посотереть тут https://pythonru.com/osnovy/stroki-python
def add_due():
    linenum = int(task_description[2])
    add_due = task_list[linenum - 1]
    print(add_due)
    date_entry = input('Введите дату завершения в формате г.м.д.(н-р: 2017.7.23) - ', )
    date_format = '%d-%m-%Y'
    date_entry = datetime.strptime(date_entry, date_format)
    # year, month, day = map(int, date_entry.split('.'))
    # date_entry = date(year, month, day)
    with open('todo.txt', 'w') as m:
        task_list[linenum - 1] = (f'{add_due} due:{date_entry}')
        m.write('\n'.join(task_list))