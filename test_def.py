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
# import sys
from datetime import date

# def date_input():
#     date_entry = input('Введите дату в формате YYYY-MM-DD : ', )
#     year, month, day = map(int, date_entry.split('-'))
#     date = datetime.date(year, month, day)
#     return date
#
# try:
#     date_input()
# except ValueError as error:
#     print('Введите дату через - ')
#
#
# x = date_input()
# print(x)

first_date = date(input('date: ',))
second_date = date(input('date: ',))
delta = second_date - first_date
print(delta)