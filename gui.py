import functions
import FreeSimpleGUI as sg
import tkinter as tk

lable = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter to-do",key='task')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_file(),enable_events=True,
                      size=(45,10),key='task_list')
edit_button = sg.Button("Edit")

window = sg.Window('My To-do List', layout=[[lable],[input_box,add_button],
                                            [list_box,edit_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.read_file()
            new_task = values['task'] + "\n"
            todo_list.append(new_task)
            functions.write_file(todo_list)
            window['task_list'].update(values=todo_list)
        case "Edit":
            task_to_edit = values['task_list'][0]
            new_task = values['task'] + "\n"

            todo_list = functions.read_file()
            index = todo_list.index(task_to_edit)
            todo_list[index] = new_task
            functions.write_file(todo_list)
            window['task_list'].update(values=todo_list)
        case "task_list":
            window['task'].update(value=values['task_list'][0])

        case sg.WIN_CLOSED:
            break

window.close()
