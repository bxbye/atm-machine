import os
import sys
current_script_path = os.path.abspath(__file__)
project_dir = os.path.dirname(os.path.dirname(current_script_path))
sys.path.append(project_dir)# add parent directory of classes
import unittest
from classes.atm import Money

class TestMoney(unittest.TestCase):
    def setUp(self) -> None:
        self.money = Money(100, 5, 'bill')
    def test_params(self):
        self.assertEqual(self.money.value, 100)
        self.assertEqual(self.money.count, 5)
        self.assertEqual(self.money.money_type, 'bill')


""" the if __name__ == '__main__': block allows you to control the behavior of your script based on whether it is being run directly or imported as a module, ensuring the correct execution of your tests. """
if __name__ == '__main__':
    unittest.main()