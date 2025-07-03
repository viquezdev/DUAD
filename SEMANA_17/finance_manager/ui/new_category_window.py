import PySimpleGUI as sg


def show_category_window(manager):
    list_combo=manager.categories

    layout = [
        [sg.Text("New Category",justification='center',expand_x=True)],
        [sg.Text("Category name: ",justification='left',expand_x=True),sg.Input(key="input")],
        [sg.Text("Existing categories: ",justification='left',expand_x=True),sg.Combo(list_combo,auto_size_text=True,readonly=True)],
        [sg.Button("Add Category")],
    ]
    window = sg.Window("Add New Category", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event=="Add Category":
            input_value=values["input"]
            if input_value!="":
                if input_value not in manager.categories:
                    manager.add_new_category(input_value)
                    sg.popup('Category was added successfully.')
                    window.close()
                else:
                    sg.popup('The Category already exists.')
            else:
                sg.popup('Required information is incomplete .')
    window.close()

