class account:
    def __init__(self,amt,accno):
        self.ammnout = amt
        self.account_no = accno
    def debit(self,amt):
        self.ammnout -= amt
        print("Rs",amt,"is deducted" )
    def credit(self,amt):
        self.ammnout += amt
        print("Rs",amt,'is added')

obj = account(10,1233)
print("Current Balance: Rs",obj.ammnout)
obj.debit(2)
print("Current Balance: Rs",obj.ammnout)
print("Account no",obj.account_no)

obj1 = account(10,1233)
print("Current Balance: Rs",obj.ammnout)
obj1.credit(2)
print("Current Balance: Rs",obj.ammnout)
print("Account no",obj.account_no)