class Transaction:
    
    def __init__(self,transaction_type,title,amount,category):
        self.transaction_type=transaction_type
        self.title=title
        self.amount=amount
        self.category=category
    

    def to_list(self):
        return [self.title, self.amount, self.category, self.transaction_type]

    


