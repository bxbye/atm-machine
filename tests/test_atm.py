import os
import sys
current_script_path = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(current_script_path))
sys.path.append(project_dir)# add parent directory of classes
import unittest
from classes.atm import Atm

class TestAtm(unittest.TestCase):
    def setUp(self) -> None:
        # This method is called before each test method.
        # You can use it to set up any common resources or create an instance of the class to be tested.
        self.atm = Atm()
    def test_withdraw_434(self):
        result = self.atm.withdraw(434)
        self.assertEqual(result[0].value, 200)
        self.assertEqual(result[0].count, 2)
        self.assertEqual(result[1].value, 20)
        self.assertEqual(result[1].count, 1)
        self.assertEqual(result[2].value, 10)
        self.assertEqual(result[2].count, 1)
        self.assertEqual(result[3].value, 2)
        self.assertEqual(result[3].count, 2)
    def test_invalid_withdraw(self):
        # Test insufficient funds scenario
        withdraw_quantity = 10000 #atm amount is 8880. request is higher then atm amount
        with self.assertRaises(ValueError) as context:
            self.atm.withdraw(withdraw_quantity)
        # Assert that the specific exception (ValueError) was raised
        self.assertEqual(str(context.exception), "The ATM machine has not enough money, please go to the nearest atm machine.")
        
    def test_balance_after_multi_withdrawals(self):
        first_balance = self.atm.check_balance()
        self.assertEqual(first_balance, 8880)
        withdrawals = [400, 554, 399, 979]
        for amount in withdrawals:
            self.atm.withdraw(amount)
        initial_balance = first_balance - sum(withdrawals)
        self.assertEqual(self.atm.check_balance(), initial_balance)
""" the if __name__ == '__main__': block allows you to control the behavior of your script based on whether it is being run directly or imported as a module, ensuring the correct execution of your tests. """
if __name__ == '__main__':
    unittest.main()