import PySimpleGUI as sg
from finance_manager.data.persistence import *

def show_income_window(manager,window_main):
    list_combo=manager.categories
    layout = [
        [sg.Text("INCOME",justification='center',expand_x=True)],
        [sg.Text("Title: ",justification='left',expand_x=True),sg.Input(key="title")],
        [sg.Text("Amount: ",justification='left',expand_x=True),sg.Input(key="amount")],
        [sg.Text("Choose a category: ",justification='left',expand_x=True),sg.Combo(list_combo,auto_size_text=True,readonly=True,key="combo_value")],
        [sg.Button("Add Income")],
    ]
    window_income = sg.Window("Add Income", layout,modal=True)
    while True:
        event, values = window_income.read()
        if event == sg.WIN_CLOSED:
            break
        if event=="Add Income":
            if manager.categories==[]:
                sg.popup('You need to add a Category first .')
            elif values["title"]!="" and values["amount"]!="" and values["combo_value"]!="":
                if not values["amount"].isdigit():
                    sg.popup('Amount must no be text .')
                else:
                    manager.add_income(values["title"],values["amount"],values["combo_value"])
                    export_data_to_csv('manager.csv',manager.transactions,["transaction_type","title","amount","category",])
                    sg.popup('Income was added successfully.')
                    row_colors = []
                    for i, row in enumerate(manager.extract_attributes(manager.transactions)):
                        if row[3] == 'income':
                            row_colors.append((i, 'green'))  
                        elif row[3] == 'expense':
                            row_colors.append((i, 'red')) 
                        
                    window_main["table_values"].update(values=manager.extract_attributes(manager.transactions),row_colors=row_colors)
                    window_income.close()
            else:
                sg.popup('Required information is incomplete .')
    window_income.close()

