from abc import ABC, abstractmethod
class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def show_details(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
class Employee(Person):
    def __init__(self, emp_id, name, phone, role):
        super().__init__(name, phone)
        self.emp_id = emp_id
        self.role = role
    def show_details(self):
        print("Employee Details")
        print("Employee ID:", self.emp_id)
        super().show_details()
        print("Role:", self.role)
class Customer(Person):
    def __init__(self, cust_id, name, phone, address):
        super().__init__(name, phone)
        self.cust_id = cust_id
        self.address = address
    def show_details(self):
        print("Customer Details")
        print("Customer ID:", self.cust_id)
        super().show_details()
        print("Address:", self.address)
class Account(ABC):
    def __init__(self, acc_no, customer, pin, balance=0):
        self.acc_no = acc_no
        self.customer = customer
        self.__pin = pin
        self.__balance = balance
    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited: Rs.", amount)
            print("Updated Balance: Rs.", self.__balance)
        else:
            print("Invalid deposit amount")
    @abstractmethod
    def withdraw(self, amount):
        pass
    def account_details(self):
        print("Account Details")
        print("Account No:", self.acc_no)
        self.customer.show_details()
        print("Balance: Rs.", self.__balance)
class SavingsAccount(Account):
    def __init__(self, acc_no, customer, pin, balance=0):
        super().__init__(acc_no, customer, pin, balance)
        self.min_balance = 500
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif self.get_balance() - amount < self.min_balance:
            print("Withdrawal denied: Minimum balance Rs.500 required")
        else:
            new_balance = self.get_balance() - amount
            self._Account__balance = new_balance
            print("Withdrawn: Rs.", amount)
            print("Updated Balance: Rs.", self.get_balance())
class CurrentAccount(Account):
    def __init__(self, acc_no, customer, pin, balance=0):
        super().__init__(acc_no, customer, pin, balance)
        self.overdraft_limit = -20000
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif self.get_balance() - amount < self.overdraft_limit:
            print("Withdrawal denied: Overdraft limit exceeded")
        else:
            new_balance = self.get_balance() - amount
            self._Account__balance = new_balance
            print("Withdrawn: Rs.", amount)
            print("Updated Balance: Rs.", self.get_balance())

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.employees = {}
        self.customers = {}
    def create_employee(self):
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        phone = input("Phone: ")
        role = input("Role: ")
        emp = Employee(emp_id, name, phone, role)
        self.employees[emp_id] = emp
        print("Employee added")
    def create_customer(self):
        cust_id = input("Customer ID: ")
        name = input("Name: ")
        phone = input("Phone: ")
        address = input("Address: ")
        cust = Customer(cust_id, name, phone, address)
        self.customers[cust_id] = cust
        print("Customer added")
    def create_account(self):
        acc_no = input("Account Number: ")
        cust_id = input("Customer ID: ")
        if cust_id not in self.customers:
            print("Customer not found")
            return
        customer = self.customers[cust_id]
        pin = input("Set 4-digit PIN: ")
        balance = float(input("Initial Deposit: "))
        print("1. Savings Account")
        print("2. Current Account")
        choice = int(input("Choice: "))
        if choice == 1:
            acc = SavingsAccount(acc_no, customer, pin, balance)
        elif choice == 2:
            acc = CurrentAccount(acc_no, customer, pin, balance)
        else:
            print("Invalid choice")
            return
        self.accounts[acc_no] = acc
        print("Account created")
    def login(self):
        acc_no = input("Account Number: ")
        if acc_no not in self.accounts:
            print("Account not found")
            return None
        acc = self.accounts[acc_no]
        entered_pin = input("Enter PIN: ")
        if acc.verify_pin(entered_pin):
            return acc
        else:
            print("Incorrect PIN")
            return None
    def deposit_money(self):
        acc = self.login()
        if acc:
            amt = float(input("Amount: "))
            acc.deposit(amt)
    def withdraw_money(self):
        acc = self.login()
        if acc:
            amt = float(input("Amount: "))
            acc.withdraw(amt)
    def view_account(self):
        acc = self.login()
        if acc:
            acc.account_details()
    def show_all_employees(self):
        for emp in self.employees.values():
            emp.show_details()
            print()
    def show_all_customers(self):
        for cust in self.customers.values():
            cust.show_details()
            print()
    def run(self):
        while True:
            print("1. Add Employee")
            print("2. Add Customer")
            print("3. Create Account")
            print("4. Deposit")
            print("5. Withdraw")
            print("6. View Account")
            print("7. Show Employees")
            print("8. Show Customers")
            print("9. Exit")
            choice = input("Choice: ")
            if choice == "1":
                self.create_employee()
            elif choice == "2":
                self.create_customer()
            elif choice == "3":
                self.create_account()
            elif choice == "4":
                self.deposit_money()
            elif choice == "5":
                self.withdraw_money()
            elif choice == "6":
                self.view_account()
            elif choice == "7":
                self.show_all_employees()
            elif choice == "8":
                self.show_all_customers()
            elif choice == "9":
                break
            else:
                print("Invalid choice")
bank = BankSystem()
bank.run()