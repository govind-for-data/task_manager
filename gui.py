import functions
import FreeSimpleGUI as sg
import tkinter as tk

lable = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter to-do",key='task')
add_button = sg.Button("Add")

window = sg.Window('My To-do List', layout=[[lable],[input_box,add_button]])

while True:
    event, values = window.read()
    match event:
        case "Add":
            todo_list = functions.read_file()
            new_task = values['task'] + "\n"
            todo_list.append(new_task)
            functions.write_file(todo_list)
        case sg.WINDOW_CLOSED:
            break



window.close()
