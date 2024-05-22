import unittest, sys,os, io
from main import Person, Helper


class TestHelper(unittest.TestCase):
    
    def testParseBirthday(self):
        # Test case 1: valid date format "dd-mm-yyyy"
        self.assertEqual(Helper.parse_birthday("25-12-2020"), "25122020")
        
        # Test case 2: valid date format "dd Month yyyy"
        self.assertEqual(Helper.parse_birthday("25 December 2020"), "25122020")
        
        # Test case 3: invalid date format
        self.assertFalse(Helper.parse_birthday("2020-12-25"))
        
        # Test case 4: invalid date with non-date string
        self.assertFalse(Helper.parse_birthday("not a date"))
        
        # # Test case 5: invalid date format with invalid day
        self.assertFalse(Helper.parse_birthday("32-12-2020"))
        
        # # Test case 6: invalid date format "Month dd, yyyy"
        self.assertFalse(Helper.parse_birthday("December 25, 2020"))
        
if __name__ == '__main__':
    unittest.main()
