import os
class Account:
    def __init__(self,acc_no,name,pin,balance,created):
        self.acc_no=acc_no
        self.name=name
        self.pin=pin
        self.balance=balance
        if(not(created)):
            self.create()



    def create(self):
        data=[self.acc_no,self.name,"#"+self.pin,"$"+self.balance]
        data=",".join(data)
        with open("Data.txt","a+") as Data:
            Data.write(data +"\n")


    def update(self,value,op):

            with open("Temp.txt","a+") as Temp:
                with open("Data.txt","r") as Data:

                    for line in Data:
                        data=line.split(",")

                        if self.acc_no ==data[0] and self.name==data[1]:
                            if(op=="d"):
                                data[3]="$"+str(int(data[3][1:])+value)
                                Temp.write(",".join(data)+"\n")
                            if(op=="w"):
                                if(int(data[3][1:])-value>=0):
                                    data[3]="$"+str(int(data[3][1:])-value)
                                    Temp.write(",".join(data)+"\n")
                                else:
                                    Temp.write(line)
                                    print("Invalid withdrawal amount")
                        else:
                            Temp.write(line)
            os.remove("Data.txt")
            os.rename('Temp.txt','Data.txt')




    def operation(self):
        while(True):

            print("What would you like to do")
            inp=input("1.Withdraw\n2.Deposit\n3.CheckBalance\n4.Exit\n")

            if(inp=="1" or inp.casefold()=="Withdraw".casefold()):
                value=int(input("Give amount to be Withdrawn:"))
                self.update(value,"w")
                balance=self.access(self.acc_no,self.pin)
                if(balance !="T.T"):
                    print("Your  Balance:"+balance)
                else:
                    print("Error While Accessing")



            elif(inp=="2" or inp.casefold()=="Deposit".casefold()):
                value=int(input("Give amount to be Deposit:"))
                self.update(value,"d")
                balance=self.access(self.acc_no,self.pin)
                if(balance !="T.T"):
                    print("Your Balance:"+balance)
                else:
                    print("Error While Accessing")


            elif(inp=="3" or inp.casefold()=="CheckBalance".casefold()):
                balance=self.access(self.acc_no,self.pin)
                if(balance !="T.T"):
                    print("Your Balance:"+balance)
                else:
                    print("Error While Accessing")


            elif(inp=="4" or inp.casefold()=="Exit".casefold()):
                print("THANK YOU \"" +self.name.upper()+"\" FOR USING OUR SERVICE")
                break

            else:
                print("Invalid operation")




    def access(self,acc,pin):
        with open("Data.txt") as Data:
           for line in Data:
               data=line.split(",")
               data_acc=data[0]
               data_pin=data[2]
               if(data_acc ==acc and data_pin==pin):
                   return data[3]

        return "T.T"


#obj=Account("1223","hero","1222","9999",False)
