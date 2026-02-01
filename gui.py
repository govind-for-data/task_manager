import functions
import FreeSimpleGUI as sg
import tkinter as tk

lable = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window('My To-do List', layout=[[lable],[input_box,add_button]])
window.read()
window.close()
