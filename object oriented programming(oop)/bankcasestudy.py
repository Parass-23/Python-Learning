class bankaccount:
    def __init__(self,name,curbalance):
        self.name=name
        self.curbalance=curbalance

    def deposit(self,amount):
        self.curbalance+=amount

    def withdrawal(self,amount):
        if amount> self.curbalance:
            print("insuffisient balance")
        else:
            self.curbalance-=amount

    def showbalance(self):
        print(self.curbalance)

bank1=bankaccount("paras",100)

bank1.withdrawal(60000)
bank1.showbalance()


