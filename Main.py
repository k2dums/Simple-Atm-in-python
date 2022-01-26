from Account import Account
from Atm import Atm
class Main:

    while(True):
        inp=input("Give Operation \n 1:Create Account 2.Use Atm \n")
        if(inp=="1" or inp.casefold()=="Create Account".casefold()):
            accno=input("Give your new Account Number:")
            name=input("Give your Name:")
            pin=input("Give your pin:")
            balance=input("Give your balance:")
            account=Account(accno,name,pin,balance,False)

        elif(inp=="2" or inp.casefold()=="Use Atm".casefold()):
            accno=input("Give your  Account Number:")
            pin=input("Give your pin:")
            atm=Atm(accno,pin)
            #print("MAIN CLASS")
            #print(atm.acc_obj)
            if(atm.acc_obj!=None):
                acc=atm.acc_obj
                acc.operation()
