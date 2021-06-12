import sys
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
task_description = sys.argv

# def read_list():
#     list = []
#     with open('todo.txt', 'r') as m:
#         list = m.read().splitlines()
#         for line in m:
#             list = line.strip('')
#         return list
#
# def done_task(list):
#     x = int(task_description[1]) #поменять в [] на +1
#     done_str = list.pop(x)
#     print(done_str)
#     done_str = done_str.replace(done_str, 'x ' + done_str, 1)
#     with open('todo.txt', 'w') as m:
#         list.append(done_str)
#         m.write('\n'.join(list))


# def remove_task(list):
#     read_list()
#     if task_description[1] == 'remove':
#         x = int(task_description[2])
#         print(type(list))
#         # remove_str = list.pop(x) # поменять в [] на +1
#         # print(remove_str)


#
# list = read_list()
# done_task(list)
# remove_task(list)

task_list = read_list()


# find_str = find_str.insert(0, 'x')