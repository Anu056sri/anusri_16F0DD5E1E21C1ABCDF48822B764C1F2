class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0 :
      self.__account_balance +=amount
      print("The deposit is₹{}. THE new balance is₹{}.".format(amount,self.__account_balance))
    else:
      print("The deposit amount is invalid")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -=amount
      print("The withdraw is₹{}. The new balance is₹{}.".format(amount,self.__account_balance))
    else:
      print("The deposit amount is invalid")

  def display_balance(self):
    print("Account balance for {} (Account #{}: {}".format(
      self.__account_holder_name,self.__account_number,
      self.__account_balance))

account = BankAccount(account_number="7789123389",
                      account_holder_name="Anusri",
                      initial_balance=5000.0)

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()