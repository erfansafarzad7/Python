from typing import List


class BankAccount:
    """
    Bank account manager.
    """
    all_acc: List[int] = []
    last_num = 999

    def __init__(self, name: str) -> None:
        BankAccount.last_num += 1
        ln = BankAccount.last_num
        self.acc_num: int = ln
        BankAccount.all_acc.append(ln)
        self.name = name
        self.balance: float = 0


    def display(self) -> None:
        """
        Show account balance.
        :return:
        """
        print(25 * '-')
        print(f'"{self.name}" (id {self.acc_num}) \n\t Your Balance is {self.balance}')
        print(25 * '-')

    def deposit(self) -> None:
        """
        Increase account balance.
        :return:
        """
        amount = float(input('Enter deposit:'))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """
        Withdraw from bank account.
        :return:
        """
        amount = float(input('Enter withdraw:'))
        if self.balance > amount:
            self.balance -= amount
        else:
            print('\n\t*** insufficient Balance! ***\n')
        self.display()


def main():
    acc = BankAccount('main')
    print(20 * '*')
    print(f'(id {acc.acc_num})')
    print(20 * '*')

    while True:
        choice = int(input(' 1. balance\n 2. deposit\n 3. withdraw\n 4. Exit\n'))

        if choice == 1:
            acc.display()
        elif choice == 2:
            acc.deposit()
        elif choice == 3:
            acc.withdraw()
        elif choice == 4:
            break
        else:
            print('enter valid num')


if __name__ == '__main__':
    main()







