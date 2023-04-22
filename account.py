class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up account object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to add funds to account
        :param amount: Amount of dollars to add
        :return: Boolean representing success of deposit or lack thereof
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to take funds out of account
        :param amount: Amount of dollars to remove
        :return: Boolean representing success of withdrawal or lack thereof
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to retrieve the private value of balance on account
        :return: Balance in dollars
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to retrieve the private value of name on account
        :return: Name of account
        """
        return self.__account_name
