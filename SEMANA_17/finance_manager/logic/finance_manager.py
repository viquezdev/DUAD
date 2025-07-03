from finance_manager.logic.transaction import Transaction
from finance_manager.logic.category import Category


class FinanceManager:
    
    def __init__(self):
        self.transactions=[]
        self.categories=Category()
    

    def add_new_category(self,new_category):
        if new_category not in self.categories:
            self.categories.append(new_category)
        return self.categories
    

    def add_income(self,title,amount,category):
        transaction=Transaction('income',title,amount,category)
        self.transactions.append(transaction)
        
    
    def add_expense(self,title,amount,category):
        transaction=Transaction('expense',title,amount,category)
        self.transactions.append(transaction)
        

    def extract_attributes(self,list_of_transactions):
        return [[t.title, t.amount, t.category,t.transaction_type] for t in list_of_transactions]
    

    def create_list_of_categories(self,list_of_transactions):
        list_categories=[]
        for obj in list_of_transactions:
            list_categories.append(obj.category)
        self.categories=list_categories
        

