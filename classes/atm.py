class Money:
    def __init__(self, value, count, money_type) -> None:
        self.value = value
        self.count = count
        self.money_type = money_type
    def __str__(self) -> str:
        format_width = 10
        return (
                f"|{str(self.value).ljust(format_width)[:format_width]}|" + \
                f"{str(self.money_type).ljust(format_width)[:format_width]}|" + \
                f"{str(self.count).ljust(format_width)[:format_width]}|"
            )

class Atm:
    def __init__(self) -> None:
        # create atm contents
        # sorted list.
        self.atm_content = [
            Money(500, 10, 'bill'), # atm has 10 500 bills(banknote) 
            Money(200, 10, 'bill'),
            Money(100, 10, 'bill'),
            Money(50, 10, 'bill'),
            Money(20, 10, 'bill'),
            Money(10, 10, 'bill'),
            Money(5, 10, 'bill'),
            Money(2, 10, 'coin'),
            Money(1, 10, 'coin')
        ]
    # return list of money to withdraw
    def withdraw(self, quantity):
        # create Money list effectively.
        withdrawal_result = []
        for money in self.atm_content:
            if(quantity >= money.value and money.count > 0):
                # atm_content list is ordered list. So if statement looks from top to bottom.
                num_bills_coins = min(quantity // money.value, money.count)
                withdrawal_result.append(Money(money.value, num_bills_coins, money.money_type))
                quantity = quantity - (num_bills_coins * money.value)
        # If the ATM does not have enough money to fulfill the request
        if quantity > 0:
            raise ValueError("The ATM machine has not enough money, please go to the nearest atm machine.")
        else:
            # remove money from atm content
            for money in withdrawal_result:
                self.subtract_money(money)
            return withdrawal_result
    def display_content(self):
        # it will use for monitoring content by user
        clm_width = 10
        # justify string left(ljust()), [:width] describes first width character will shown
        print(
            f"|{'Value'.ljust(clm_width)[:clm_width]}" + \
            f"|{'Type'.ljust(clm_width)[:clm_width]}" + \
            f"|{'Quantity'.ljust(clm_width)[:clm_width]}|"
        )
        print(f"|{'-' * clm_width}|{'-' * clm_width}|{'-' * clm_width}|")
        for money in self.atm_content:
            print(money)
    def subtract_money(self, money:Money):
        for content in self.atm_content:
            if money.value == content.value and money.money_type == content.money_type:
                content.count -= money.count
                break
    def check_balance(self):
        return sum(money.count * money.value for money in self.atm_content)