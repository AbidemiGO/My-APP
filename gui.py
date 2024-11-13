
import functions
import FreeSimpleGUI as sg
import time


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key= "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key = "todos", enable_events = True, size = (45,10))
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
window = sg.Window("My To-Do App", layout = [[label],
                                             [input_box, add_button], [list_box, edit_button, complete_button],
                                             [exit_button]],
                                            font= ("Helvetica",20))
while True:
    event, values = window.read()
    #window["clock"].update(value = time.strftime("%b,%d,%Y,%H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            newly_todo = values["todo"] + "\n"
            todos.append(newly_todo)
            functions.write_todos(todos)
            window["todos"].update(values="todos")
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                newly_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = newly_todo
                functions.write_todos(todos)
                window["todos"].update(values = "todos")
            except IndexError:
                sg.popup("please select an item first.", font = ("Helvetica", 20))

        case "complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values="todos")
                window["todo"].update(value="")
            except IndexError:
                sg.popup("please select an item first.", font = ("Helvetica", 20))


        case "Exit":
            break

        case "todos":
             window["todo"].update(value= values["todos"][0])


        case sg.WIN_CLOSED:
            break
window.close()





