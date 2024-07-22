import functions
import FreeSimpleGUI as sg
import time

sg.theme('DarkTeal12')
label_clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip='Enter todo here', key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(30, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')
window = sg.Window('My ToDo App', layout=[[label_clock],
                                          [label],
                                          [input_box, add_button],
                                          [list_box, edit_button, complete_button],
                                          [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

        # Only update the clock if the window is still open
    if window:
        window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))

    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a item first", font=('Helvetica', 14))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=' ')
            except IndexError:
                sg.popup("Please select one item first", font=('Helvetica', 14))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
