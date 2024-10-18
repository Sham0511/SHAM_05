class ATM_Machine:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def home_screen(self):
        print("|--------------------------------------------------|")
        print("***********WELCOME***********|")
        print("|****1.VIEW YOUR BALANCE*****|")
        print("|****2. AMOUNT DEPOSIT********|")
        print("|****3.MONEYWITHDRAWAL*****|")
        print("|****4.      CHANGE PIN   *********|")
        print("|****5.*********EXIT*************|")
        print("|--------------------------------------------------|")

    def deposit(self, amount):
        self.balance += amount
        print(f"YOUR BALANCE AFTER DEPOSIT = {self.balance}")

    def withdrawal(self, amount):
        if self.balance < amount:
            print("**** INSUFFICIENT BALANCE ****")
        else:
            self.balance -= amount
            print(f"YOUR BALANCE AFTER WITHDRAWAL = {self.balance}")

    def get_balance(self):
        return self.balance

    def validate_pin(self, pin):
        return self.pin == pin

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN CHANGED SUCCESSFULLY")


def main():
    atms = [
        ATM_Machine(175482, 1505),
        ATM_Machine(59782, 1511),
        ATM_Machine(45894, 1234),
        ATM_Machine(25687, 5678),
        ATM_Machine(78412, 1909),
    ]

    print("**** WELCOME TO ABC BANK OF INDIA ****")
    print()

    entered_pin = int(input("ENTER YOUR PIN = "))

    selected_atm = None
    for atm in atms:
        if atm.validate_pin(entered_pin):
            selected_atm = atm
            break

    if selected_atm is None:
        print("INVALID PIN ENTRY")
        return

    selected_atm.home_screen()
    option = 0
    while option != 5:
        option = int(input("ENTER YOUR OPTION = "))
        if option == 1:
            print(f"BALANCE = {selected_atm.get_balance()}")
        elif option == 2:
            amount = int(input("ENTER THE AMOUNT = "))
            selected_atm.deposit(amount)
        elif option == 3:
            amount = int(input("ENTER THE AMOUNT = "))
            selected_atm.withdrawal(amount)
        elif option == 4:
            new_pin = int(input("ENTER YOUR NEW PIN = "))
            selected_atm.change_pin(new_pin)
        elif option == 5:
            print("THANK YOU! VISIT AGAIN.")
        else:
            print("INVALID OPTION! PLEASE TRY AGAIN.")


if __name__ == "__main__":
    main()
