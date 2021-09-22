# консольное приложениe для ведения списка задач - todo
___________________________________
Приложение сохраняет задачи в файле todo.txt в той же папке, где находится исполняемый модуль приложения.
#### Приложение поддерживает следующие команды:
* :white_check_mark: `todo.py` - показать незавершенные задачи
* :white_check_mark: `todo.py all` - показать все задачи (включая завершенные)
* :white_check_mark: `todo.py add <task description> [due:<date>]` - добавить задачу с описание <task description> (и дополнительно можно добавить срок выполнения <date>)
* :white_check_mark: `todo.py remove <n>` - удалить задачу с номером <n>
* :white_check_mark: `todo.py edit <n> <new task description>` - редактировать задачу с номером <n>: установить новое описание <new task description>
* :white_check_mark: `todo.py due <n> <date>` - установить срок выполнения <date> для задачи <n>
* :white_check_mark: `todo.py done <n>` - пометить задачу как выполненную
* :white_check_mark: `todo.py undo <n>` - снять отметку о выполнении
* :white_check_mark: `todo.py search <sting>` - поиск задач по тексту <string>
  
#### Реализация поиска по датам:
* :white_check_mark: `created between <date> <date>`  - поиск по дате создания между указанными датами
* :white_check_mark: `created before <date>` - поиск по дате создания до указанной даты
* :white_check_mark: `created after <date>` - поиск по дате создания после указанной даты
* :white_check_mark: `due between <date> <date>`  - поиск по дате выполнения между указанными датами
* :white_check_mark: `due before <date>` - поиск по дате выполнения до указанной даты 
* :white_check_mark: `due after <date>` - поиск по дате выполнения после указанной даты
____________________________
## Формат файла todo.txt:
* Поле завершенности: "x" (выставляется автоматически после выполнения команды done)
* Дата создания задачи: "2019-11-23" (автоматически при создании)
* Описание задачи
* Срок задачи: "due:2019-12-23" (не обязательное)
