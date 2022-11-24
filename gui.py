import functions
import PySimpleGUI as sg

label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_buttom = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_buttom]])
window.read()
window.close()