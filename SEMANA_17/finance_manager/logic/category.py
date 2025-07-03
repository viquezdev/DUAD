class Category:
    
    def __init__(self,initial_categories=None):
        if initial_categories is None:
            initial_categories=[]
        self.categories=initial_categories
    

    def add_new_category(self,new_category):
        if new_category not in self.categories:
            self.categories.append(new_category)
        
        
    def get_categories(self):
        return self.categories
