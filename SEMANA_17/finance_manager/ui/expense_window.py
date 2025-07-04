import PySimpleGUI as sg
from finance_manager.data.persistence import *

def show_expense_window(manager,window_main):
    list_combo=manager.categories
    layout = [
        [sg.Text("EXPENSE",justification='center',expand_x=True)],
        [sg.Text("Title: ",justification='left',expand_x=True),sg.Input(key="title")],
        [sg.Text("Amount: ",justification='left',expand_x=True),sg.Input(key="amount")],
        [sg.Text("Choose a category: ",justification='left',expand_x=True),sg.Combo(list_combo,auto_size_text=True,readonly=True,key="combo_value")],
        [sg.Button("Add Expense")],
    ]
    window_expense = sg.Window("Add Expense", layout,modal=True)
    while True:
        event, values = window_expense.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Add Expense":
            if not manager.categories:
                sg.popup("You need to add a category first.")
            
            elif values["title"] and values["amount"] and values["combo_value"]:
                try:
                    amount = float(values["amount"])
                    if amount < 0:
                        sg.popup("Amount must be a positive number.")
                    else:
                        input_value = str(values["title"]).strip()
                        manager.add_expense(input_value, amount, values["combo_value"])
                        export_data_to_csv(
                            'manager.csv',
                            manager.transactions,
                            ["transaction_type", "title", "amount", "category"]
                        )
                        sg.popup("Expense was added successfully.")
                        
                        attributes = manager.extract_attributes(manager.transactions)
                        row_colors = [
                            (i, "green") if row[3] == "income" else (i, "red")
                            for i, row in enumerate(attributes)
                            if row[3] in ("income", "expense")
                        ]
                        
                        window_main["table_values"].update(values=attributes, row_colors=row_colors)
                        window_expense.close()

                except ValueError:
                    sg.popup("Amount must be a valid number.")
            
            else:
                sg.popup("Required information is incomplete.")
    window_expense.close()

