class bank:
    def __init__(self,accn,nam,accty):
        self.acn=accn
        self.nam=nam
        self.accty=accty
        self.bal=0
    def showamt(self):
            print("Account Holder Name:",self.nam)
            print("Account Number:",self.acn)
            print("Account Type",self.accty)
            print("Your Balance Amount:",self.bal)
    def dep(self,d1):
                self.bal=self.bal+d1
                return self.bal
    def withd(self,w1):
                self.bal=self.bal-w1
                return self.bal
n=input("Enter your name:")
a=int(input("Enter your account number:"))
t=input("Enter your account type:")
o=bank(a,n,t)
o.showamt()
while(True):
    print("Menu")
    print("\n1.Deposit")
    print("\n2.Withdraw")
    c=int(input("Enter your choice:"))
    if(c==1):
        d=int(input("Enter the amount to deposit:"))
        print("Your total Balance Amount is:",o.dep(d))
    elif(c==2):
        w=int(input("Enter the amount to be withdraw:"))
        if(w>d):
            print("Insufficient Balance.")
        else:
            print("your total balance is:",o.withd(w))
    else:
        print("Enter the valid choice")
