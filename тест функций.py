def replase_str():
    with open ('todo.txt', 'r') as f:
        old_data = f.read()
    new_data = old_data.replace('еще какая нибудь строка','xxxxxxxxxx', 1 )
    with open ('todo.txt', 'a') as f:
        f.write(new_data)
    print(new_data)
replase_str()


# def todo_task(find_num, index, value):#тут в () по хорошему должен вызываться список find_task
#     with open('todo.txt', 'a') as m:
#         if int(task_description[2]) == int(index):
#             index = str(index)
#             result = find_num.replace(index,'x', 1)
#     with open('todo.txt', 'a') as f:
#         f.write(result)
#         print(result)