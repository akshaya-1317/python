#create account class with 2 attributes - balance & acc number
#create methods for debit, credit and printing the balance.

#class
#constructor
#methods
#object




class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print(amount,"was debited")
        print("total balance = ", self.get_balance())

    def credit(self, camt):
        self.balance += camt
        print(camt,"was Credited")
        print("total balance = ", self.get_balance())


    def get_balance(self):
        return self.balance


acc1 = Account(500000, 123)
print(acc1.balance)
print(acc1.accno)
acc1.debit(200)
acc1.credit(1000)