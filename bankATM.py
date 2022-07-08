class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount", amount)


def main():
    Card_number = input("enter your card numbers:- ")
    pin_number  = input("enter your pin numbers:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("select your work")
    print("1.Check Balance   2.Withdraw Money")
    work = input("enter work number :- ")

    if (work == 1):
        new_user.check_balance()
    elif (work == 2):
        amount = input("enter the amount:- ")
        new_user.withdrawl(amount)
    
if __name__ == "__main__":
    main()