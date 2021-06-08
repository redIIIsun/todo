# import sys
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


def find_task():
    find_str = []
    with open('todo.txt', 'r') as m:
        find_str = m.readlines()
        for line in m:
            find_str = line.strip('')
        # print(find_str)
        print(find_str[3])
find_task()
