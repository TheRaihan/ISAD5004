import unittest, sys,os, io
from unittest.mock import Mock

from main import Person, Helper


class TestHelper(unittest.TestCase):
    
    def test_valid_birthday(self):
        # Test case 1: valid input in "DD-MM-YYYY" format
        sys.stdin = io.StringIO("01-01-2000\n")
        result = Helper.get_valid_birthday_input()
        self.assertEqual(result, "01012000")
        sys.stdin = sys.__stdin__

        # Test case 2: valid input in "DD Month YYYY" format
        sys.stdin = io.StringIO("15 June 1995\n")
        result = Helper.get_valid_birthday_input()
        self.assertEqual(result, "15061995")
        sys.stdin = sys.__stdin__

        # Test case 3: invalid input followed by valid input
        sys.stdin = io.StringIO("invalid\n10-20-2000\n30 February 2022\n05 May 2023\n")
        result = Helper.get_valid_birthday_input()
        self.assertEqual(result, "05052023")
        sys.stdin = sys.__stdin__
        
    def testSumDigits(self):
        # Test case 1: sum of digits of a single digit number
        self.assertEqual(Helper.sum_digits(5), 5)

        # Test case 2: sum of digits of a multi-digit number
        self.assertEqual(Helper.sum_digits(123), 6)  # 1 + 2 + 3 = 6
        
        # Test case 3: sum of digits of a large number
        self.assertEqual(Helper.sum_digits(987654321), 45) # 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
        
        # Test case 4: sum of digits of zero
        self.assertEqual(Helper.sum_digits(0), 0)

    def testIsMasterNumber(self):
        
        # Test case 1: num is a master number (33)
        self.assertTrue(Helper.is_master_number(33))
        
        # Test case 2: num is not a master number (10)
        self.assertFalse(Helper.is_master_number(10))
        
        # Test case 3: num is a string
        self.assertFalse(Helper.is_master_number("eleven"))
        
        # Test case 4: num is None
        self.assertFalse(Helper.is_master_number(None))
        
        # Test case 5: num is a list
        self.assertFalse(Helper.is_master_number([11]))

    def testLifePathCompare(self):
        # Test case 1: num is a master number (11)
        person1 = Mock()
        person2 = Mock()

        # Test case 1: Same life path number
        person1.life_path_num = 5
        person2.life_path_num = 5
        self.assertTrue(Helper.lifePathCompare(person1, person2))

        # Test case 2: Different life path numbers
        person1.life_path_num = 1
        person2.life_path_num = 9
        self.assertFalse(Helper.lifePathCompare(person1, person2))

        # Test case 3: String life path number
        person1.life_path_num = "5"
        person2.life_path_num = 5
        self.assertFalse(Helper.lifePathCompare(person1, person2))

        # Test case 4: None as life path number
        person1.life_path_num = None
        person2.life_path_num = 5
        self.assertFalse(Helper.lifePathCompare(person1, person2))

if __name__ == '__main__':
    unittest.main()
