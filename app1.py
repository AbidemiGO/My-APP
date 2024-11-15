
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1} . {item}'

            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input('Enter a new_todo: ')

            todos = functions.get_todos()

            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('Invalid value is entered')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todos.pop(index)
            todo_to_remove = todos[index].strip('\n')

            functions.write_todos(todos)

            message = f'Todo {todo_to_remove} was removed '
            print(message)
        except IndexError:
            print('You entered invalid number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')


print('bye!')










