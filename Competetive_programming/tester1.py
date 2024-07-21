'''
data structure ---------
class Node:

    def __init__(self,value):
        self.__value = value
        self.next = None



    def traverse(self):
        print(self.value)


temp1 = Node(10)

temp2 = Node(20)

temp3 = Node(30)

temp1.next= temp2
temp2.next=temp3


temp1.traverse()
'''
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance is ${self.__balance}.")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.__balance}.")
        else:
            print("Insufficient funds or invalid amount!")

    def get_balance(self):
        return self.__balance

# Create a BankAccount object
account = BankAccount("Alice", 1000)

# Accessing public attribute
print(f"Account holder: {account.account_holder}")

# Trying to access the private attribute directly (will raise an error)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError

# Using public methods to interact with private attribute
account.deposit(500)
account.withdraw(200)
print(f"testeing here == {account.}" )
print(f"Current balance: ${account.get_balance()}")

# Directly modifying the public attribute
account.account_holder = "Bob"
print(f"Updated account holder: {account.account_holder}")

# Trying to modify the private attribute directly (will raise an error)
# account.__balance = 5000  # Uncommenting this line will raise an AttributeError
