"""
File: atm.py
Project 8.4

This module defines the ATM class and its application.

Modifies the user interface so that it prints a message and shuts down
if the user fails at three consecutive logins.

Can be modified to run as a script after a bank has been saved.
"""
from bank import Bank, SavingsAccount

class ATM(object):
    """This class represents terminal-based ATM transactions."""

    def __init__(self, bank):
        self._account = None
        self._bank = bank
        self._methods = {}          # Jump table for commands
        self._methods["1"] = self._getBalance
        self._methods["2"] = self._deposit
        self._methods["3"] = self._withdraw
        self._methods["4"] = self._quit

    def run(self):
        """Logs in users and processes their accounts."""
        failureCount = 0
        while True:
            # Prompt user to enter name
            name= input("Please enter account name: ")
            self._account = self._bank.get(name)
            # Prompt user to enter PIN
            pin= input("Please enter the pin number: ")
            self._account = self._bank.get(pin)
            # If account was not found
            if(self._account == None):
                # Print "Error, unrecognized PIN"
                print("Error, unrecognized PIN")
                failureCount = failureCount +1
            # If account name does not match name
            elif(self._account.getName() != name):
                # Print "Error, unrecognized name"
                print("Error, unrecognized name")
                failureCount = failureCount + 1
            # If account is valid
            else:
                # Load account menu
                self._processAccount()
                break
            # If an invalid entry was made three times
            if(failureCount == 3):
                # Print "Shutting down and calling the cops!" and end program
                print("Shutting down and calling the cops!")
                break
    def _processAccount(self):
        """A menu-driven command processor for a user."""
        while True:
            print("1  View your balance")
            print("2  Make a deposit")
            print("3  Make a withdrawal")
            print("4  Quit\n")
            number = input("Enter a number: ")
            theMethod = self._methods.get(number, None)
            if theMethod == None:
                print("Unrecognized number")
            else:
                theMethod()
                if self._account == None:
                    break

    def _getBalance(self):
        print("Your balance is $", self._account.getBalance())

    def _deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self._account.deposit(amount)

    def _withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        message = self._account.withdraw(amount)
        if message:
            print(message)

    def _quit(self):
        self._bank.save()
        self._account = None
        print("Have a nice day!")

# Top-level functions
def main():
    """Instantiate an ATM and run it."""
    bank = Bank("bank.dat")
    atm = ATM(bank)
    atm.run()

def createBank(number = 0):
    """Saves a bank with the specified number of accounts.
    Used during testing."""
    bank = Bank()
    for i in range(number):
        bank.add(SavingsAccount('Name' + str(i + 1),
                                str(1000 + i),
                                100.00))
    bank.save("bank.dat")


# Creates a bank with the following names / PINS:
#Name1 = (Name1, 1000)
#Name2 = (Name2, 1001)
#Name3 = (Name3, 1002)
#Name4 = (Name4, 1003)
#Name5 = (Name5, 1004)
createBank(5)
main()

