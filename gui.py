import functions
import FreeSimpleGUI as sg
import tkinter as tk
from datetime import datetime

lable = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter to-do", key='task')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_file(), enable_events=True,
                      size=(45, 10), key='task_list')
edit_button = sg.Button("Edit")

window = sg.Window('My To-do List', layout=[[lable], [input_box, add_button],
                                            [list_box, edit_button]])

def with_timestamp(task: str) -> str:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    return f"{timestamp} - {task}\n"

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.read_file()
            new_task = with_timestamp(values['task'])
            todo_list.append(new_task)
            functions.write_file(todo_list)
            window['task_list'].update(values=todo_list)
        case "Edit":
            if not values['task_list']:
                continue
            task_to_edit = values['task_list'][0]
            new_task = with_timestamp(values['task'])

            todo_list = functions.read_file()
            index = todo_list.index(task_to_edit)
            todo_list[index] = new_task
            functions.write_file(todo_list)
            window['task_list'].update(values=todo_list)
        case "task_list":
            if not values['task_list']:
                continue
            selected = values['task_list'][0].rstrip('\n')
            if ' - ' in selected:
                selected = selected.split(' - ', 1)[1]
            window['task'].update(value=selected)

        case sg.WIN_CLOSED:
            break

window.close()
