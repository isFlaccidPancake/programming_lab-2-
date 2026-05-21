class BankAccount:
    def __init__(self, bank, account_number, accountholder, initial_balance = 0):
        self.bank= bank
        self.account_number= account_number
        self.accountholder= accountholder
        self.__balance= initial_balance
    def return_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance+= amount
    def withdraw(self, amount):
        if self.__balance<amount:
            self.__balance=0
            print('Insufficient funds')
        else:
            self.__balance-= amount
        return f'this amount of money was withdraw {amount}'
class AccountHolder:
    def __init__(self, id, firstname, lastname):
        self.id=id
        self.firstname= firstname
        self.lastname= lastname
        self.__bankaccounts= []
    def add_bankaccount(self,bankaccount):
        if bankaccount not in self.__bankaccounts:
            self.__bankaccounts.append(bankaccount)     
    def print_bankaccounts(self):
        print('Accounts of the account holder: '. self.id)
        for ba in self.__bankaccounts:
            print(ba.bank, ba.account_number, ba.return_balance())
        print()    
    def total_balance(self):
        return sum(ba.return_balance() for ba in self.__bankaccounts)
class Bank:
    __latest_account_id=0
    def __init__(self,name):
        self.name= name
        self.__accountholders=[]
        self.__accounts=[]
    def print_accountholders(self):
        print('account holders of the bank', self.name)
        for ah in self.__accountholders:
            print(ah.id,ah.firstname, ah.lastname)
        print()        
    def print_accounts(self):
        print('printing the accounts of the bank: ',self.name)
        for a in self.__accounts:
            print(a.account_number,a.accountholder.id, a.return_balance())
        print()
    def create_account(self, account_holder, initial_balance = 0):
        if isinstance(account_holder, AccountHolder):
            Bank.__latest_account_id+=1
            ba = BankAccount(self.name,Bank.__latest_account_id, account_holder.id, initial_balance)
            account_holder.add_bankaccount(ba)
            self.__accounts.append(ba)
            if account_holder not in self.__accountholders:
                self.__accountholders.append(account_holder)
            return ba
    '''Add also the following methods to the Bank class:
    • deposit(self, account, amount) deposits the amount to the account if the
    account exists in the bank
    • withdraw(self, account, amount) attempts to withdraw the amount from the
    account and prints a message with the withdrawn amount, if the account exists in the
    bank'''
    def deposit(self,account,amount):
        if account in self.__accounts:
            print('depositing money to the account: ', account.account_number)
            account.deposit(amount)
        else:
            print('account missing')
            print()
            return 
    def withdraw(self,accout,amount):
        if account in self.__accounts:
            print('withdrowing money from the account: ', account.account_number)
            w= account.withdraw(amount)
            print(w, 'euro withdrawn from the bank')
        else:
            print('account missing')
            print()
            return 
    


    
        
        
    
         
    
    