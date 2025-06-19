class BankAccount:
    
    def __init__(self,balance):
        self.balance=balance
    

    def deposit_money(self,amount):
        if(amount>0):
            self.balance+=amount
            print(f"you deposit has been processed.New balance: {self.balance}")
        else:
            print("Deposit failed. The amount must be positive.")


    def withdraw_money(self,amount):
        if(amount<=0):
            print("Withdrawal failed. Amount must be positive.")
        elif(self.balance>=amount):
            self.balance-=amount
            print(f"you withdraw has been processed.New balance: {self.balance}")
        else:
            print("Withdraw failed.Not enough founds in the account")


class SavingsAccount(BankAccount):
    def __init__(self,balance, min_balance):
        super().__init__(balance)
        self.min_balance=min_balance
    

    def withdraw_money(self,amount):
        if(amount<=0):
            print("Withdrawal failed. Amount must be positive.")
        elif((self.balance-amount)>=self.min_balance):
            self.balance-=amount
            print(f"Your withdrawal has been processed. New balance: {self.balance}")
        else:
            print("Withdraw failed.You must maintain the minimum required balance")
    
diego_account=SavingsAccount(5000,500)
diego_account.deposit_money(-3000)
diego_account.withdraw_money(5000)
print(diego_account.balance)
diego_account.withdraw_money(-5000)