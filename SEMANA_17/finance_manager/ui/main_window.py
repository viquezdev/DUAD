import PySimpleGUI as sg
from finance_manager.ui.expense_window import show_expense_window
from finance_manager.ui.income_window import show_income_window
from finance_manager.ui.new_category_window import show_category_window
from finance_manager.logic.finance_manager import FinanceManager
from finance_manager.data.persistence import *


def show_main_window():
    
    manager=FinanceManager()
    if import_data_csv('manager.csv')==None:
        manager.transactions=[]
        manager.create_list_of_categories(manager.transactions)
        data_table_incomes_expenses=[]
    else:
        manager.transactions=import_data_csv('manager.csv')
        manager.create_list_of_categories(manager.transactions)
        data_table_incomes_expenses=[t.to_list() for t in import_data_csv('manager.csv')]
    data_table_headers=["Tittle","Amount","Category","Type Transaction"]          
    layout = [
        [sg.Text("INCOMES AND EXPENSES",justification='center',expand_x=True)],
        [sg.Table(data_table_incomes_expenses,data_table_headers,expand_x=True,justification='center',key="table_values"),sg.Button("Add Income"),sg.Button("Add Expense")],
        [sg.Button("Add New Category",expand_x=True)],
    ]
    window_main = sg.Window("Finance Manager", layout,finalize=True)
    row_colors = []
    for i, row in enumerate(manager.extract_attributes(manager.transactions)):
        if row[3] == 'income':
            row_colors.append((i, 'green'))  
        elif row[3] == 'expense':
            row_colors.append((i, 'red'))   
    window_main["table_values"].update(values=manager.extract_attributes(manager.transactions),row_colors=row_colors)
    while True:
        event, values = window_main.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add Income":
            show_income_window(manager,window_main)

        elif event == "Add Expense":
            show_expense_window(manager,window_main)

        elif event == "Add New Category":
            show_category_window(manager)
    window_main.close()

if __name__=="__main__":
    show_main_window()