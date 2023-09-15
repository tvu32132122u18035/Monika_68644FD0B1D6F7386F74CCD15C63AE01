class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self.__account_number= account_number
      self.__account_holder_name= account_holder_name 
      self.__account_balance= initial_balance 
  def deposit(self,amount):
     if amount>0:
       self.__account_balance+= amount 
       print("Deposited ₹{}. New balance: ₹{}".format(amount, self. __account_balance)) 
     else:
       print("Invalid deposit amount. Please deposit a positive amount.") 
  def withdraw(self,amount) :
     if amount>0and amount<=self.__account_balance:
       self.__account_balance-=amount 
       print("withdraw ₹{}. New balance: ₹{}".format(amount, self. __account_balance))
     else:
       print("Invalid withdraw amount or insufficient balance. ") 
  def display_balance(self):
      print (" account balance for{} (Account #{}):₹{}". format(self.__account_holder_name, self.__account_number, self.__account_balance))
account=BankAccount(account_number="56565772", account_holder_name="Monika", initial_balance=50000.0) 
account.display_balance()
account.deposit(500.0)
account.withdraw(2000.0)
account.display_balance() 

    
      
