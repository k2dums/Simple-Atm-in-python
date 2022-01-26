from Account import Account
class Atm(Account):

    def __init__(self,acc_no,pin):
        self.acc_no=acc_no
        self.pin="#"+pin
        self.acc_obj=self.Validate()
        if(self.acc_obj != None):
          pass
          #print("ACCOUNT C")
          #print(self.acc_obj)
        else:
            print("Excessive attempt")


    def Validate(self):
        attempt=1
        found=False
        with open("Data.txt") as Data:
            while(attempt<=3):

                if(attempt>1):
                    print("ATTEMPT "+str(attempt))
                    self.acc_no=input("Give account number:")
                    self.pin="#"+input("Give pin:")


                Data.seek(0,0)
                for line in Data:
                    data=line.split(",")
                    data_acc=data[0]
                    data_pin=data[2]
                    if(data_acc ==self.acc_no and data_pin==self.pin):
                        print("Welcome "+data[1])
                        acc_obj=Account(data[0],data[1],data[2],data[3],True)
                        found=True
                        break
                #end for line in Data
                if(found):
                    break
                else:
                    attempt+=1

                #End of while attempt<=3
                #End of open (Data.txt)


        if found:
            return acc_obj
        else:
            return None

    #End of Validate() function


#atm=Atm("xxx","1111x")
#acc_obj=atm.Validate()
